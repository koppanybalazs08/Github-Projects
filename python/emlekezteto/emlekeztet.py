import pandas as pd
from time import sleep
import customtkinter as ctk

adat = pd.read_json("adat.json")
sleeps = []

for i, ido in enumerate(adat.loc[:,"ido"]):
    if i > 0:
        sleeps.append((ido - sum(sleeps)))
    else:
        sleeps.append(ido)

for i, szoveg in enumerate(adat.loc[:,"szoveg"]):
    sleep(sleeps[i])
    window = ctk.CTk()
    pop_up = ctk.CTkTextbox(window)
    pop_up.insert("0.0",szoveg)
    window.mainloop()