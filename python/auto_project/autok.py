import pandas as pd

class Auto:
    '''
    innit: id, márka, modell, szín, üzemanyag típus, hajtáslánc lementése

    str: a print(auto) hatását változtatja
    így nem kell minden külön kiirogatni (majd a kerséshez lesz hasznos)

    példa:
    print(pelda)
        |
        |
        V

    'Azonosító: 10, Márka: Példa márka, Modell: Példa modell, szín: piros'
    'Részletek: benzin-es/os, hátsókerék meghajtásos-os'
    '--------------------------------'
    VAGY
    'Azonosító: 5'
    'KIKÖLCSÖNÖZVE'
    '--------------------------------'
    '''

    def __init__(self, id, marka, modell, szin, uzemanyag_tipus, hajtaslanc, kolcsonzott = False):
        self.id = id
        self.marka = marka
        self.modell = modell
        self.szin = szin
        self.uzemanyag_tipus = uzemanyag_tipus
        self.hajtaslanc = hajtaslanc
        self.kolcsonzott = kolcsonzott

    def __str__(self):
        if not self.kolcsonzott:
            return f'\nAzonosító: {self.id}, Márka: {self.marka}, Modell: {self.modell}, szín: {self.szin}\nRészletek: {self.uzemanyag_tipus}-es/os, {self.hajtaslanc}-os\n--------------------------------'
        return f'\nAzonosító: {self.id}\nKIKÖLCSÖNÖZVE\n--------------------------------'
    
#fontos változók:
autok = [] #ezt kell majd végig használni kereséshez stb
path_excel = './data/autok.xlsx' #excel fájl elérési útja
path_kolcsonzott = './data/kolcsonzott.txt'

excel = pd.read_excel(path_excel) #A pandas modullal olvastam be az excel fájlt, 
#egy listához hasonló dolgot ad vissza
#print(excel_fajl) ---> fájl tartalmának megtekintése

meret = excel.shape #pandas muvelet: kiadja, hogy melyik irányba hány cella az excel fájl (8, 6), tuple (magasság/mélység, szélesség)

with open(path_kolcsonzott, 'r') as f: #kolcsonzott.txt megnyitása a fönti változó segítségével
    kolcsonzott_autok = f.readlines()

    for i in range(meret[0]):
        '''
        Egy auto() objektum létrehozása az excel fájl adataival,
        és listába helyezése, ha nincs ki kölcsönözve

        '''
        if str(excel['id'][i]) + '\n' not in kolcsonzott_autok:
            uj_auto = Auto(str(excel['id'][i]), excel['márka'][i], excel['modell'][i], excel['szín'][i], excel['üzemanyag típus'][i], excel['hajtáslánc'][i])
        else:
            uj_auto = Auto(str(excel['id'][i]), excel['márka'][i], excel['modell'][i], excel['szín'][i], excel['üzemanyag típus'][i], excel['hajtáslánc'][i], kolcsonzott = True)

        autok.append(uj_auto)

def kereses(marka, szin, uzemanyag, hajtaslanc): # Megadott feltételek alapján keres elérhető autókat
    talalatok = []
    for auto in autok:
        # Csak akkor hasonlít, ha adott mező nincs üresen hagyva (Enter)
        if marka != '' and auto.marka.lower() != marka.lower():
            continue
        if szin != '' and auto.szin.lower() != szin.lower():
            continue
        if uzemanyag != '' and auto.uzemanyag_tipus.lower() != uzemanyag.lower():
            continue
        if hajtaslanc != '' and auto.hajtaslanc.lower() != hajtaslanc.lower():
            continue
        talalatok.append(auto) # ha minden stimmel, hozzáadjuk a találatokhoz

    return talalatok

def kolcsonzes(auto_id):

    for auto in autok :
        if auto.id == auto_id and not auto.kolcsonzott: # Ha megtaláltuk és nem kölcsönzött

            with open(path_kolcsonzott, 'a') as f:
                f.write(f"{auto_id}\n")

            auto.kolcsonzott = True # az objektumban is átállítjuk
            return f"\nSikeres kölcsönzés: {auto.marka} {auto.modell}\n"

    return "\nNincs ilyen ID-jű autó vagy már kölcsönözve van.\n" # Ha nincs ilyen ID vagy már kölcsönzött


while True:
    print("\n--- Autókölcsönző Menü ---")
    print("1. Összes elérhető autó kilistázása")
    print("2. Keresés")
    print("3. Autó kölcsönzése ID alapján")
    print("4. Kilépés")
    valasztas = input("Válassz egy opciót: ")

    if valasztas == '1': # Kiírjuk az összes autót
        
        for auto in autok: 
            print(auto)


    elif valasztas == '2': # Felhasználótól bekérjük a keresési szempontokat
        
        marka = input("Márka (Enter ha mindegy): ")
        szin = input("Szín (Enter ha mindegy): ")
        uzemanyag = input("Üzemanyag típus (Enter ha mindegy): ")
        hajtaslanc = input("Hajtáslánc (Enter ha mindegy): ")
        talalatok = kereses(marka, szin, uzemanyag, hajtaslanc)
        # Találatok kiírása
        if talalatok: 
            for auto in talalatok:
                print(auto)
        else:
            print("\nNincs találat a megadott feltételekre.\n")
    
    elif valasztas == '3': # Kölcsönzés indítása ID alapján
        auto_id = input("Add meg a kölcsönözni kívánt autó ID-jét: ")
        print(kolcsonzes(auto_id))


    elif valasztas == '4': # Kilépés a programból
        print("Viszlát!")
        break

    else:
        print("\n1-et, 2-et, 3-at, 4-et, vagy 5-öt írjon be.\n") # Hibás bemenet esetén figyelmeztetés
        