# extract.py - lag rapport over saksmapper
# bruk: python3 extract.py cases.csv 1990 [1999]
import csv
import sys
from collections import defaultdict

INGEN_SLUTT = 9999
STREK = "=" * 40
GRADERT = {"J", "j", "ja"}


def les_rader(filnavn):
    with open(filnavn, encoding="utf-8") as fil:
        return [r for r in csv.reader(fil, delimiter=";") if r[0] != "id"]


def kort_tittel(tittel):
    return tittel if len(tittel) <= 40 else tittel[:37] + "..."


def main(filnavn, fra, til):
    grupper = defaultdict(list)
    antall = 0
    hoppet = 0
    for r in les_rader(filnavn):
        try:
            aar = int(r[3][:4])
        except ValueError:
            hoppet += 1
            continue
        if fra <= aar <= til:
            arkivdel = r[5].strip().upper() if r[5] else "UKJENT"
            grupper[arkivdel].append(r)
            antall += 1

    slutt = str(til) if til != INGEN_SLUTT else ""
    print(f"Rapport saksmapper {fra}-{slutt}")
    print(STREK)
    for arkivdel in sorted(grupper):
        print(f"{arkivdel} ({len(grupper[arkivdel])})")
        for r in sorted(grupper[arkivdel], key=lambda r: r[3]):
            gradert = " [GRADERT]" if r[4] in GRADERT else ""
            print(f"  {r[1]}  {r[3]}  {kort_tittel(r[2])}{gradert}")
    print(STREK)
    print(f"Totalt: {antall}")
    if hoppet:
        print(f"Hoppet over (mangler dato): {hoppet}")


if __name__ == "__main__":
    try:
        til = int(sys.argv[3])
    except (IndexError, ValueError):
        til = INGEN_SLUTT
    main(sys.argv[1], int(sys.argv[2]), til)
