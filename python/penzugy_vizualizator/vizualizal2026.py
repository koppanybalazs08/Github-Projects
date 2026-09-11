import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Adat szerzés és tisztítás 
def fetch_data(sheet):
    table = pd.read_excel("konyveles.xlsx", sheet_name = sheet)
    
    #szumma táblázat
    sum_table = table.iloc[[0,2,3,4,5,6],list(range(14, len(table.columns), 14))]
    #iloc[hányadik sor, list(range(hányadik oszloptól,hányadik oszlopig,hány oszloponként))]

    #Összes adat összeállítása
    data_dict = {
            "kotveny":list(table.iloc[15,list(range(4, len(table.columns), 14))])
            ,"kp_be":list(table.iloc[15,list(range(6, len(table.columns), 14))])
            ,"kp_ki":list(table.iloc[15,list(range(8, len(table.columns), 14))])
            ,"bk_be":list(table.iloc[15,list(range(10, len(table.columns), 14))])
            ,"bk_ki":list(table.iloc[15,list(range(12, len(table.columns), 14))])
            ,"kp_záro":list(sum_table.loc[0,:])
            ,"bk_záro":list(sum_table.loc[2,:])
            ,"baba":list(sum_table.loc[3,:])
            ,"szumma":list(sum_table.loc[4,:])
            ,"szumma_likvid":list(sum_table.loc[5,:])
            ,"profit":list(sum_table.loc[6,:])}
    
    data_dict["honapok"] = ['Január','Február','Március', 'Április','Május','Június','Július','Augusztus','Szeptember','Október','November','December'][:len(data_dict["szumma"])]

    return pd.DataFrame.from_dict(data_dict)

#data_table exportálása excel fájlba
def write_data():
    data_table.to_excel("konyveles_pandas_format.xlsx")

#Záró étékek vizualizálása (babakötvény + szumma | készpénz + bankkártya + likvid szumma)
def zaro():

    #formázás
    fig, axes = plt.subplots(2, 1, sharex=True, figsize = (8,8))
    fig.suptitle("Záró összegek (Ft)")
    fig.supxlabel("Hónap")

    axes[0].set_ylabel("Millió forint")
    axes[1].set_ylabel("Forint")

    #felső plot
    sns.lineplot(ax = axes[0], data = data_table["baba"].loc[data_table["baba"] > 0], label = "Babakötvény", color = "purple")
    sns.lineplot(ax = axes[0], data = data_table["kotveny"].loc[data_table["kotveny"] > 0] , label = "Kötvény", color = "darkblue")
    sns.lineplot(ax = axes[0], data = data_table["szumma"], label = "Szumma", color = "red")

    #alsó plot
    sns.lineplot(ax = axes[1], data = data_table["szumma_likvid"], label = "Szumma (likvid)", color = "orange")
    sns.lineplot(ax = axes[1], data = data_table["kp_záro"], label = "Készpénz", color = "green")
    sns.lineplot(ax = axes[1], data = data_table["bk_záro"], label = "Bankkártya", color = "blue")

    #x tengely
    plt.xticks(ticks = list(range(0,12)), labels = data_table["honapok"], rotation = 30)

    plt.savefig(f"zaro_{sheet}.png")
    plt.show()

#bevétel és kiadás vizualizálása
def be_ki():

    plt.figure(figsize = (8,6))
    plt.title("Kiadások és bevételek(Ft)")

    sns.lineplot(data = data_table["kp_ki"], label = "Készpénz kiadás", color = "limegreen")
    sns.lineplot(data = data_table["kp_be"], label = "Készpénz bevétel", color = "green")

    sns.lineplot(data = data_table["bk_ki"], label = "Bankkártya kiadás", color = "cornflowerblue")
    sns.lineplot(data = data_table["bk_be"], label = "Bankkártya bevétel", color = "blue")

    #formázás
    plt.ylabel("Forint")
    plt.xlabel("Hónap")
    plt.xticks(ticks = list(range(0,12)), labels = data_table["honapok"], rotation = 30)
    plt.savefig(f"be_ki_{sheet}.png")
    plt.show()

#bankártya és készpénz használatának aránya (kiadás | bevétel)
def kp_bk_arany():
    kp_ki_mean = data_table["kp_ki"].mean()
    bk_ki_mean = data_table["bk_ki"].mean()
    kp_be_mean = data_table["kp_be"].mean()
    bk_be_mean = data_table["bk_be"].mean()

    ki_sum = kp_ki_mean + bk_ki_mean
    be_sum = kp_be_mean + bk_be_mean

    fig, axes = plt.subplots(2, 1, sharex=True, figsize = (8,8))
    fig.suptitle("Bankkártya és Készpénz használati aránya")

    #kördiagramok
    axes[0].pie([kp_be_mean, bk_be_mean], labels = [f"készpénz bevétel: {kp_be_mean / be_sum * 100 :.2f}%", f"bankkártya bevétel: {bk_be_mean / be_sum * 100 :.2f}%"], colors = ["green", "blue"], explode = [0.1, 0.1], shadow = True)
    axes[1].pie([kp_ki_mean, bk_ki_mean], labels = [f"készpénz kiadás: {kp_ki_mean / ki_sum * 100 :.2f}%", f"bankkártya kiadás: {bk_ki_mean / ki_sum * 100 :.2f}%"], colors = ["limegreen", "cornflowerblue"], explode = [0.1, 0.1], shadow = True)

    plt.savefig(f"kp_bk_arany_{sheet}.png")
    plt.show()

kimutatas_tipus = None

sheet = input("Év: ")
data_table = fetch_data(sheet)

#menü, mainloop
while kimutatas_tipus != "5":

    kimutatas_tipus = input("Kimutatás típusa:\n"
                            "1. Záró - 1\n"
                            "2. Bevétel és Kiadás - 2\n"
                            "3. Bankkártya és Készpénz használat - 3\n"
                            "4. Formázatlan adat kiadása - 4\n"
                            "5. Kilépés - 5\n"
                            ": ")

    if kimutatas_tipus == "1":
        zaro()
    elif kimutatas_tipus == "2":
        be_ki()
    elif kimutatas_tipus == "3":
        kp_bk_arany()
    elif kimutatas_tipus == "4":
        write_data()