#!/usr/bin/env python3
"""Compare two same-size screenshots and preserve auditable artifacts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from PIL import Image, ImageChops


def _open_rgb(path: Path) -> Image.Image:
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(path)
    with Image.open(path) as opened:
        return opened.convert("RGB")


def _metrics(diff: Image.Image, tolerance: int) -> dict[str, float]:
    width, height = diff.size
    pixel_count = width * height
    histogram = diff.histogram()
    absolute_error = sum(
        (index % 256) * count for index, count in enumerate(histogram)
    )
    normalized_mae = absolute_error / (pixel_count * 3 * 255)

    red, green, blue = diff.split()
    max_channel = ImageChops.lighter(ImageChops.lighter(red, green), blue)
    max_histogram = max_channel.histogram()
    within_tolerance = sum(max_histogram[: tolerance + 1]) / pixel_count

    return {
        "normalized_mae": normalized_mae,
        "pixel_similarity": 1.0 - normalized_mae,
        "within_tolerance_ratio": within_tolerance,
    }


def _validate_region(
    name: str,
    box: list[int],
    image_size: tuple[int, int],
) -> tuple[int, int, int, int]:
    if len(box) != 4 or not all(isinstance(value, int) for value in box):
        raise ValueError(f"region {name!r} must be [x, y, width, height]")
    x, y, width, height = box
    image_width, image_height = image_size
    if x < 0 or y < 0 or width <= 0 or height <= 0:
        raise ValueError(f"region {name!r} has invalid coordinates")
    if x + width > image_width or y + height > image_height:
        raise ValueError(f"region {name!r} is outside image bounds")
    return x, y, x + width, y + height


def compare_images(
    reference: Path,
    actual: Path,
    tolerance: int = 24,
    regions: dict[str, list[int]] | None = None,
) -> dict[str, Any]:
    """Return full-image and optional named-region difference metrics."""
    if not 0 <= tolerance <= 255:
        raise ValueError("tolerance must be between 0 and 255")

    reference_image = _open_rgb(reference)
    actual_image = _open_rgb(actual)
    if reference_image.size != actual_image.size:
        raise ValueError(
            "image dimensions differ: "
            f"reference={reference_image.size}, actual={actual_image.size}"
        )

    diff = ImageChops.difference(reference_image, actual_image)
    width, height = reference_image.size
    report: dict[str, Any] = {
        "reference": str(Path(reference).resolve()),
        "actual": str(Path(actual).resolve()),
        "size": {"width": width, "height": height},
        "tolerance": tolerance,
        **_metrics(diff, tolerance),
        "regions": {},
    }

    for name, box in (regions or {}).items():
        crop_box = _validate_region(name, box, reference_image.size)
        region_diff = diff.crop(crop_box)
        report["regions"][name] = {
            "box": box,
            **_metrics(region_diff, tolerance),
        }
    return report


def _write_image_artifacts(
    reference: Path,
    actual: Path,
    diff_path: Path,
    overlay_path: Path,
) -> None:
    reference_image = _open_rgb(reference)
    actual_image = _open_rgb(actual)
    diff = ImageChops.difference(reference_image, actual_image)
    amplified = diff.point(lambda value: min(255, value * 4))
    overlay = Image.blend(reference_image, actual_image, 0.5)

    diff_path.parent.mkdir(parents=True, exist_ok=True)
    overlay_path.parent.mkdir(parents=True, exist_ok=True)
    amplified.save(diff_path)
    overlay.save(overlay_path)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference", type=Path)
    parser.add_argument("actual", type=Path)
    parser.add_argument("--report", required=True, type=Path)
    parser.add_argument("--diff", required=True, type=Path)
    parser.add_argument("--overlay", required=True, type=Path)
    parser.add_argument("--regions", type=Path)
    parser.add_argument("--tolerance", type=int, default=24)
    parser.add_argument("--max-mae", type=float, default=0.035)
    parser.add_argument("--min-within-tolerance", type=float, default=0.90)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    regions = None
    if args.regions:
        regions = json.loads(args.regions.read_text(encoding="utf-8"))
        if not isinstance(regions, dict):
            raise ValueError("regions JSON must be an object")

    report = compare_images(
        args.reference,
        args.actual,
        tolerance=args.tolerance,
        regions=regions,
    )
    violations: list[str] = []
    if report["normalized_mae"] > args.max_mae:
        violations.append(
            f"normalized_mae {report['normalized_mae']:.6f} > {args.max_mae:.6f}"
        )
    if report["within_tolerance_ratio"] < args.min_within_tolerance:
        violations.append(
            "within_tolerance_ratio "
            f"{report['within_tolerance_ratio']:.6f} < "
            f"{args.min_within_tolerance:.6f}"
        )

    report["thresholds"] = {
        "max_mae": args.max_mae,
        "min_within_tolerance": args.min_within_tolerance,
    }
    report["passed"] = not violations
    report["violations"] = violations

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    _write_image_artifacts(args.reference, args.actual, args.diff, args.overlay)
    print(json.dumps(report, ensure_ascii=False))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
