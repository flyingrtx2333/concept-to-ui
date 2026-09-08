import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from PIL import Image

from scripts.analyze_reference import analyze_image, crop_image
from scripts.compare_screenshots import compare_images


class ToolTests(unittest.TestCase):
    def test_analyze_and_crop_are_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "source.png"
            Image.new("RGB", (4, 3), (10, 20, 30)).save(source)

            report = analyze_image(source)
            self.assertEqual(report["size"], {"width": 4, "height": 3})
            self.assertEqual(report["top_colors"][0]["rgb"], [10, 20, 30])

            crop = root / "crop.png"
            crop_image(source, (1, 1, 2, 2), crop)
            with Image.open(crop) as opened:
                self.assertEqual(opened.size, (2, 2))

    def test_analyze_falls_back_for_older_pillow(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "source.png"
            Image.new("RGB", (2, 1), (4, 5, 6)).save(source)

            with patch.object(
                Image.Image, "get_flattened_data", None, create=True
            ):
                report = analyze_image(source)

            self.assertEqual(report["top_colors"][0]["rgb"], [4, 5, 6])

    def test_analyze_rejects_non_positive_color_count(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "source.png"
            Image.new("RGB", (1, 1), (0, 0, 0)).save(source)
            with self.assertRaisesRegex(ValueError, "top_colors must be positive"):
                analyze_image(source, top_colors=0)

    def test_analyze_orders_tied_colors_deterministically(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "source.png"
            image = Image.new("RGB", (2, 1))
            image.putdata([(9, 9, 9), (1, 1, 1)])
            image.save(source)

            report = analyze_image(source, top_colors=2)
            self.assertEqual(
                [item["rgb"] for item in report["top_colors"]],
                [[1, 1, 1], [9, 9, 9]],
            )

    def test_crop_rejects_out_of_bounds_box(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "source.png"
            Image.new("RGB", (2, 2), (0, 0, 0)).save(source)
            with self.assertRaisesRegex(ValueError, "outside image bounds"):
                crop_image(source, (1, 1, 2, 2), root / "crop.png")

    def test_compare_reports_pass_and_fail(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            reference = root / "reference.png"
            actual = root / "actual.png"
            Image.new("RGB", (2, 2), (0, 0, 0)).save(reference)
            Image.new("RGB", (2, 2), (255, 255, 255)).save(actual)

            passed = compare_images(reference, reference)
            failed = compare_images(reference, actual)
            self.assertEqual(passed["normalized_mae"], 0)
            self.assertGreater(failed["normalized_mae"], 0)

    def test_compare_reports_named_regions(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            reference = root / "reference.png"
            actual = root / "actual.png"
            Image.new("RGB", (4, 4), (0, 0, 0)).save(reference)
            Image.new("RGB", (4, 4), (0, 0, 0)).save(actual)

            report = compare_images(
                reference, actual, regions={"header": [0, 0, 4, 1]}
            )
            self.assertEqual(report["regions"]["header"]["box"], [0, 0, 4, 1])
            self.assertEqual(report["regions"]["header"]["normalized_mae"], 0)

    def test_compare_rejects_different_dimensions(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            reference = root / "reference.png"
            actual = root / "actual.png"
            Image.new("RGB", (2, 2), (0, 0, 0)).save(reference)
            Image.new("RGB", (3, 2), (0, 0, 0)).save(actual)
            with self.assertRaisesRegex(ValueError, "image dimensions differ"):
                compare_images(reference, actual)

    def test_compare_rejects_invalid_tolerance(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "source.png"
            Image.new("RGB", (1, 1), (0, 0, 0)).save(source)
            with self.assertRaisesRegex(ValueError, "between 0 and 255"):
                compare_images(source, source, tolerance=256)


if __name__ == "__main__":
    unittest.main()
