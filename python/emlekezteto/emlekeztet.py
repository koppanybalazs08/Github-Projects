import pandas as pd
from time import sleep
import customtkinter as ctk

adat = pd.read_json("adat.json")
sleeps = []
FONT_SIZE = 25

for i, ido in enumerate(adat.loc[:,"ido"]):
    if i > 0:
        sleeps.append((ido - sum(sleeps)))
    else:
        sleeps.append(ido)

for i, szoveg in enumerate(adat.loc[:,"szoveg"]):
    sleep(sleeps[i])
    window = ctk.CTk()
    window.geometry("450x300")
    window.resizable(False, False)
    window.title("Új emlékeztető!")
    window.configure(fg_color = "#C1CFDA")
    
    szoveg_text = ctk.CTkTextbox(window, font = ("Roboto",FONT_SIZE), width = len(szoveg) * FONT_SIZE, fg_color = "#C1CFDA", wrap = "word")
    szoveg_text.tag_config("center", justify = "center")
    szoveg_text.insert("end", szoveg, "center")
    szoveg_text.configure(state = "disabled")
    szoveg_text.pack(padx = 5, pady = 5)
    

    window.mainloop()