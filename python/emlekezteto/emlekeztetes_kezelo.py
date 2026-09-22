import pandas as pd
from pathlib import Path

def adat_mentes(adat : pd.DataFrame):
    adat = adat.sort_values(by = "ido").reset_index(drop = True)
    adat.to_json("adat.json", index = False)
    return adat

def uj_emlekeztetes(szoveg : str, ido : int, adat : pd.DataFrame):
    uj_sor = pd.DataFrame({"szoveg" : [szoveg], "ido" : [ido]})
    return adat_mentes(pd.concat([adat, uj_sor], ignore_index = True))

def emlekeztetes_szerkesztes(index : int, szoveg : str, ido : int, adat : pd.DataFrame):
    if index <= len(adat):
        sor_szoveg = adat["szoveg"][index]
        sor_ido = adat["ido"][index]
        adat = adat.replace(sor_szoveg, szoveg).replace(sor_ido, ido)

    return adat_mentes(adat)

def emlekeztetes_torles(index : int, adat : pd.DataFrame):
    if index <= len(adat):
        adat.drop(index = index, axis = "index", inplace = True)

    return adat_mentes(adat)


adat = pd.read_json("adat.json")

print("Válasszon a lehetőségek közül:\n" \
        "\t 1 - Új emlékeztetés\n" \
        "\t 2 - Emlékeztetés szerkesztése\n" \
        "\t 3 - Emlékeztetés törlése\n" \
        "\t ex - Kilépés\n")
valasztas = input("A válassz(1, 2, 3, ex): ")
print(adat.to_string())

if valasztas == "1":
    adat = uj_emlekeztetes(input("emlékeztetés címe: "), int(input("emlékeztetés időzítése (mennyivel indítás után jelenjen meg) : ")), adat)

elif valasztas == "2":
    adat = emlekeztetes_szerkesztes(int(input("Emlékeztetés index-e: ")), input("emlékeztetés új címe: "), int(input("emlékeztetés időzítése (mennyivel indítás után jelenjen meg) : ")), adat)

elif valasztas == "3":
    adat = emlekeztetes_torles(int(input("Emlékeztetés index-e: ")), adat)

print(adat.to_string())