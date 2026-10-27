# Sammenligner extract.py med lagret utdata fra det gamle skriptet.
# bruk: python3 test_extract.py
import subprocess
import sys
import unittest
from pathlib import Path

HER = Path(__file__).parent
TILFELLER = {
    ("1990", "1999"): "old-1990-1999.txt",
    ("1990",): "old-1990.txt",
    ("2000", "2005"): "old-2000-2005.txt",
}


class TestExtract(unittest.TestCase):
    def test_samme_utdata_som_gammelt_skript(self):
        for args, fil in TILFELLER.items():
            with self.subTest(args=args):
                ut = subprocess.run(
                    [sys.executable, "extract.py", "cases.csv", *args],
                    cwd=HER, capture_output=True, text=True, encoding="utf-8", check=True,
                ).stdout
                self.assertEqual(ut, (HER / fil).read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
