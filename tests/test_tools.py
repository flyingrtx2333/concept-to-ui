import tempfile
import unittest
from pathlib import Path

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


if __name__ == "__main__":
    unittest.main()
