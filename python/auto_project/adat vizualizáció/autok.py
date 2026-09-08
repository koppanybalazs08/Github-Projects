import matplotlib.pyplot as plt
from pandas import read_excel as excel
from pandas import read_csv as csv
import seaborn as sns

#Adatok begyűjtése
data1 = excel('autok.xlsx')
data2 = csv('Termékek.txt', sep = ';')
print(data2)
print(data1)

#kördiagram adatainak előkészítése
def pie_prep(search_by,data):
    output = {}
    for x in data[search_by]:
        if not x in output:
            output[x] = list(data[search_by]).count(x)

    return output

#Hajtáslánc adatok
sns.countplot(data1, x = 'üzemanyag típus', hue = 'hajtáslánc')
plt.title('autok.xlsx')
plt.show()

sns.countplot(data2, x = 'évjárat', hue = 'hajtáslánc')
plt.title('Termékek.txt')
plt.show()

#Márkák megoszlása a két adathalmazban kördiagrammal
figure, axis = plt.subplots(1, 2,figsize=(12,8))
markak1 = pie_prep('márka',data1)
axis[0].pie(markak1.values(),labels = markak1.keys())
axis[0].set_title('autok.xlsx')

markak2 = pie_prep('márka',data2)
axis[1].pie(markak2.values(),labels = markak2.keys())
axis[1].set_title('Termékek.txt')
plt.show()

#Autók besorolása kördiagrammal
besorolas = pie_prep('besorolás',data2)
plt.pie(besorolas.values(),labels = besorolas.keys())
plt.title('Termékek.txt')
plt.show()

#Szín választék összehasonlítása kördiagrammal
figure, axis = plt.subplots(1, 2,figsize=(12,8))
szin1 = pie_prep('szín',data1)
axis[0].pie(szin1.values(), labels = szin1.keys())
axis[0].set_title('autok.xlsx')

szin2 = pie_prep('szín',data2)
axis[1].pie(szin2.values(), labels = szin2.keys())
axis[1].set_title('Termékek.txt')
plt.show()