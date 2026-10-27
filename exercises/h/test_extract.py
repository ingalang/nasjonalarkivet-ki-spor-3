# Sammenligner utdata fra extract.py med de lagrede old-*.txt-filene.
# Kjør: python3 test_extract.py
import subprocess
import sys
from pathlib import Path

HER = Path(__file__).parent
TILFELLER = {
    "old-1990-1999.txt": ["1990", "1999"],
    "old-1990.txt": ["1990"],
    "old-2000-2005.txt": ["2000", "2005"],
}

feil = 0
for fil, args in TILFELLER.items():
    ut = subprocess.run(
        [sys.executable, "extract.py", "cases.csv", *args],
        cwd=HER, capture_output=True, text=True, encoding="utf-8", check=True,
    ).stdout
    ok = ut == (HER / fil).read_text(encoding="utf-8")
    feil += not ok
    print(("OK   " if ok else "FEIL ") + fil)
sys.exit(feil)
