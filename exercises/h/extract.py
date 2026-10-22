# extract.py - lag rapport over saksmapper
# bruk: python3 extract.py cases.csv 1990 [1999]
# skrevet i all hast i 2016, endret litt etterpå
import sys, csv

f = sys.argv[1]
fra = int(sys.argv[2])
try:
    til = int(sys.argv[3])
except:
    til = 9999

rader = []
for r in csv.reader(open(f, encoding="utf-8"), delimiter=";"):
    if r[0] == "id":
        continue
    rader.append(r)

res = {}
antall = 0
hoppet = 0
for r in rader:
    try:
        aar = int(r[3][0:4])
    except:
        hoppet = hoppet + 1
        continue
    if aar >= fra:
        if aar <= til:
            if r[5] == "" or r[5] == None:
                ark = "UKJENT"
            else:
                ark = r[5].strip().upper()
            if ark in res:
                res[ark] = res[ark] + [r]
            else:
                res[ark] = [r]
            antall = antall + 1

print("Rapport saksmapper " + str(fra) + "-" + (str(til) if til != 9999 else ""))
print("=" * 40)
for k in sorted(res.keys()):
    print(k + " (" + str(len(res[k])) + ")")
    for r in sorted(res[k], key=lambda x: x[3]):
        tittel = r[2]
        if len(tittel) > 40:
            tittel = tittel[0:37] + "..."
        gradert = ""
        if r[4] == "J" or r[4] == "j" or r[4] == "ja":
            gradert = " [GRADERT]"
        print("  " + r[1] + "  " + r[3] + "  " + tittel + gradert)
print("=" * 40)
print("Totalt: " + str(antall))
if hoppet > 0:
    print("Hoppet over (mangler dato): " + str(hoppet))
