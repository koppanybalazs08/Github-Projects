import pandas as pd

def open(path):
    data = pd.read_excel(path)
    data.rename(columns = {"Sorozat" : "sorozat",
                            "Kibocsátás\ndátuma" : "kibocsatas",
                            "Lejárat\ndátuma" : "lejarat",
                            "Kamatfizetés" : "kamatfizetes",
                            "Kamatozási időszak" : "kamatozasi_idoszak",
                            "Kamat\nmértéke" : "kamat",
                            "Féléves\nkamatok" : "kamat_feleves"}, inplace = True)
    
    data = data[data["sorozat"] != "Sorozat"]
    data.drop(columns = ["kamat_feleves"], inplace = True)

    data.loc[:,["sorozat", "kibocsatas", "lejarat", "kamatfizetes"]] = data.loc[:,["sorozat", "kibocsatas", "lejarat", "kamatfizetes"]].ffill()
    data.dropna(inplace = True)
    data.reset_index(drop = True, inplace = True)
    return data


babakotveny = open("excel/babakotveny.xlsx")
babakotveny.to_excel("excel/babakotveny_formatted.xlsx")
print(babakotveny.head(40))
