#!/usr/bin/env python3
"""Measure a screenshot and optionally extract explicitly named crops."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

from PIL import Image


def _existing_image(path: Path) -> Path:
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(path)
    return path


def analyze_image(path: Path, top_colors: int = 8) -> dict[str, Any]:
    """Return deterministic source dimensions and dominant RGB colors."""
    source = _existing_image(path)
    if top_colors <= 0:
        raise ValueError("top_colors must be positive")

    with Image.open(source) as opened:
        rgb = opened.convert("RGB")
        width, height = rgb.size
        counts = Counter(rgb.get_flattened_data())

    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    colors = [
        {
            "rgb": list(color),
            "hex": "#{:02x}{:02x}{:02x}".format(*color),
            "count": count,
        }
        for color, count in ranked[:top_colors]
    ]
    return {
        "source": str(source.resolve()),
        "size": {"width": width, "height": height},
        "aspect_ratio": width / height,
        "top_colors": colors,
    }


def crop_image(
    path: Path,
    box: tuple[int, int, int, int],
    output: Path,
) -> None:
    """Crop an exact ``(x, y, width, height)`` rectangle."""
    source = _existing_image(path)
    x, y, width, height = box
    if x < 0 or y < 0 or width <= 0 or height <= 0:
        raise ValueError("crop must use non-negative x/y and positive width/height")

    with Image.open(source) as opened:
        source_width, source_height = opened.size
        if x + width > source_width or y + height > source_height:
            raise ValueError("crop is outside image bounds")
        cropped = opened.crop((x, y, x + width, y + height))
        destination = Path(output)
        destination.parent.mkdir(parents=True, exist_ok=True)
        cropped.save(destination)


def _parse_crop(value: str) -> tuple[str, tuple[int, int, int, int]]:
    try:
        name, raw_box = value.split(":", 1)
        coordinates = tuple(int(part) for part in raw_box.split(","))
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            "crop must be NAME:X,Y,W,H using integer coordinates"
        ) from exc
    if not name or len(coordinates) != 4:
        raise argparse.ArgumentTypeError("crop must be NAME:X,Y,W,H")
    return name, coordinates  # type: ignore[return-value]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--top-colors", type=int, default=8)
    parser.add_argument("--crop", action="append", type=_parse_crop, default=[])
    parser.add_argument("--crop-dir", type=Path)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    report = analyze_image(args.image, top_colors=args.top_colors)

    if args.crop and args.crop_dir is None:
        raise SystemExit("--crop-dir is required when --crop is used")

    crops: list[dict[str, Any]] = []
    for name, box in args.crop:
        output = args.crop_dir / f"{name}.png"
        crop_image(args.image, box, output)
        crops.append({"name": name, "box": list(box), "output": str(output.resolve())})
    if crops:
        report["crops"] = crops

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
