import pandas as pd
from pathlib import Path

adat = pd.read_json("adat.json")
print(adat.to_string())

def uj_emlekeztetes(szoveg, ido, adat):
    uj_sor = pd.DataFrame({"szoveg" : [szoveg], "ido" : [ido]})
    adat = pd.concat([adat, uj_sor], ignore_index = True)

    adat.to_json("adat.json", index = False)

def emlekeztetes_szerkesztese(szoveg, ido, index, adat):
    pass


print("Válasszon a lehetőségek közül:\n" \
        "\t 1 - Új emlékeztetés\n" \
        "\t 2 - Emlékeztetés szerkesztése\n" \
        "\t 3 - Emlékeztetés törlése\n" \
        "\t ex - Kilépés\n")
valasztas = input("A válassz(1, 2, 3, ex): ")

if valasztas == "1":
    uj_emlekeztetes(input("emlékeztetés címe: "), int(input("emlékeztetés időzítése (mennyivel indítás után jelenjen meg) : ")), adat)