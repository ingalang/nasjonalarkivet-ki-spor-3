# extract.py - lag rapport over saksmapper
# bruk: python3 extract.py cases.csv 1990 [1999]
import csv
import sys
from collections import defaultdict

UTEN_SLUTT = 9999
GRADERT = {"J", "j", "ja"}
LINJE = "=" * 40


def les_rader(sti):
    with open(sti, encoding="utf-8") as f:
        return [r for r in csv.reader(f, delimiter=";") if r[0] != "id"]


def grupper(rader, fra, til):
    """Returnerer (saker per arkivdel, antall saker, antall uten gyldig dato)."""
    per_arkivdel = defaultdict(list)
    antall = hoppet = 0
    for r in rader:
        try:
            aar = int(r[3][:4])
        except ValueError:
            hoppet += 1
            continue
        if fra <= aar <= til:
            arkivdel = r[5].strip().upper() if r[5] else "UKJENT"
            per_arkivdel[arkivdel].append(r)
            antall += 1
    return per_arkivdel, antall, hoppet


def kort_tittel(tittel):
    return tittel[:37] + "..." if len(tittel) > 40 else tittel


def rapport(per_arkivdel, antall, hoppet, fra, til):
    slutt = "" if til == UTEN_SLUTT else str(til)
    linjer = [f"Rapport saksmapper {fra}-{slutt}", LINJE]
    for arkivdel in sorted(per_arkivdel):
        saker = per_arkivdel[arkivdel]
        linjer.append(f"{arkivdel} ({len(saker)})")
        for r in sorted(saker, key=lambda r: r[3]):
            gradert = " [GRADERT]" if r[4] in GRADERT else ""
            linjer.append(f"  {r[1]}  {r[3]}  {kort_tittel(r[2])}{gradert}")
    linjer += [LINJE, f"Totalt: {antall}"]
    if hoppet:
        linjer.append(f"Hoppet over (mangler dato): {hoppet}")
    return "\n".join(linjer)


def main(args):
    fra = int(args[1])
    try:
        til = int(args[2])
    except (IndexError, ValueError):
        til = UTEN_SLUTT
    print(rapport(*grupper(les_rader(args[0]), fra, til), fra, til))


if __name__ == "__main__":
    main(sys.argv[1:])
