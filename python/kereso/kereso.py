import pandas as pd
import sqlalchemy as sqla
import tkinter as tk
import customtkinter as ctk

#output mező módosítása a keresés eredményével
def insert_to_output(result):
    output.configure(state = "normal")
    output.delete("1.0","end")
    output.insert(tk.INSERT, result)
    output.see("end")
    output.configure(state = "disabled")

    #output mező méretezése
    output.configure(height = (len(df) + 2) * 15, width = 30 * 15)

#keresés név alapján
def Search_by_name(name:str):
    #pandas keresés
    df_temp = df[df["vezeteknev"].str.contains(name, case = False, na = False, regex = False) | df["keresztnev"].str.contains(name, case = False, na = False, regex = False)]

    #output kezelés
    if len(df_temp) < 1:
        #nincs találat
        df_str = ""
        insert_to_output(df_str)
    else:
        #van találat
        df_str = df_temp.to_string(index = False)
        insert_to_output(df_str)

#keresés beosztás alapján
def Search_by_role(role:str):
    #pandas keresés
    df_temp = df[df["beosztas"].str.contains(role, case = False, na = False, regex = False)]

    #output kezelés
    if len(df_temp) < 1:
        #nincs találat
        df_str = ""
        insert_to_output(df_str)
    else:
        #van találat
        df_str = df_temp.to_string(index = False)
        insert_to_output(df_str)

#keresés fizetés alapján
def Search_by_salary(salary:str, operation:str):

    df_temp = []
    try:
        salary = float(salary)

        #"kisebb mint" keresés
        if operation == "<":
            df_temp = df[df["netto_ber"] < salary]

        #"nagyobb mint" keresés
        elif operation == ">":
            df_temp = df[df["netto_ber"] > salary]
    except:
        pass

    #output kezelés
    if len(df_temp) < 1:
        #nincs találat
        df_str = ""
        insert_to_output(df_str)
    else:
        #van találat
        df_str = df_temp.to_string(index = False)
        insert_to_output(df_str)

#MySQL adatbázis keresése
ENGINE = sqla.create_engine("mysql+pymysql://felhasznalo:jelszo@localhost/kereso_db")#módosítsd saját felhasználónév:jelszóra

global df
df = pd.read_sql("SELECT szemelyek.id, szemelyek.vezeteknev, szemelyek.keresztnev, szemelyek.beosztas, fizetes.netto AS netto_ber FROM szemelyek LEFT JOIN fizetes ON szemelyek.id = fizetes.id", ENGINE)

#adatbázis str-é alakítása az outputhoz
global df_str
df_str = df.to_string(index = False)

#customtkinter setup
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")
window = ctk.CTk()
window.geometry("550x550")
window.title("Adatbázis kereső 1.0")

#konstans változók: corner radius, font
C_RAD = 5
FONT = ("Roboto", 12)

#kereső sáv
search_label = ctk.CTkLabel(master = window, text = "Keresés a felhasználók között:", font = FONT)
search_bar = ctk.CTkEntry(master = window, font = FONT)

#gombok
search_by_name = ctk.CTkButton(master = window, text = "keresés név alapján", command = lambda: Search_by_name(search_bar.get()), cursor = "hand2", font = FONT, corner_radius = C_RAD)
search_by_role = ctk.CTkButton(master = window, text = "keresés beosztás alapján", command = lambda: Search_by_role(search_bar.get()), cursor = "hand2", font = FONT, corner_radius = C_RAD)
search_by_salary_lower = ctk.CTkButton(master = window, text = "keresés fizetés alapján (kisebb mint)", command = lambda: Search_by_salary(search_bar.get(), "<"), cursor = "hand2", font = FONT, corner_radius = C_RAD)
search_by_salary_higher = ctk.CTkButton(master = window, text = "keresés fizetés alapján (nagyobb mint)", command = lambda: Search_by_salary(search_bar.get(), ">"), cursor = "hand2", font = FONT, corner_radius = C_RAD)

#output beállítása
output_label = ctk.CTkLabel(master = window, text = "Eredmény:", font = FONT)
global output
output = ctk.CTkTextbox(master = window, font = FONT)
insert_to_output(df_str)

#elemek elhelyezése
search_label.place(rely = 0, relx = 0.5, anchor = "n")
search_bar.place(rely = 0.1, relx = 0.5, anchor = "n")

search_by_name.place(rely = 0.25, relx = 0.3, anchor = "n")
search_by_role.place(rely = 0.25, relx = 0.7, anchor = "n")

search_by_salary_lower.place(rely = 0.35, relx = 0.25, anchor = "n")
search_by_salary_higher.place(rely = 0.35, relx = 0.75, anchor = "n")

output_label.place(rely = 0.5, relx = 0.5, anchor = "n")
output.place(rely = 0.6, relx = 0.5, anchor = "n")

window.mainloop()