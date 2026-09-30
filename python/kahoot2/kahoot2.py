import customtkinter as ctk
import pandas as pd

def do_quiz():
    pass

def new_quiz():
    data_out = pd.DataFrame({"question" : [], "A" : [], "B" : [], "C" : [], "D" : [], "correct" : []})
    question_text.configure(state = "active")
    correct_ans = "-"

    A_btn.configure(text = "Correct", command = lambda: correct_ans.replace("-", "A"))
    

def quiz_menu():
    pass

def correct():
    pass

def incorrect():
    pass


window = ctk.CTk()

start_btn = ctk.CTkButton(window, text = "Start", command = quiz_menu)
create_btn = ctk.CTkButton(window, text = "Create quiz", command = new_quiz)

question_text = ctk.CTkLabel(window)
A_btn = ctk.CTkLabel(window)
B_btn = ctk.CTkLabel(window)
C_btn = ctk.CTkLabel(window)
D_btn = ctk.CTkLabel(window)

A_entry = ctk.CTkEntry(window, placeholder_text = "A válasz")
B_entry = ctk.CTkEntry(window, placeholder_text = "B válasz")
C_entry = ctk.CTkEntry(window, placeholder_text = "C válasz")
D_entry = ctk.CTkEntry(window, placeholder_text = "D válasz")

new_quiz()