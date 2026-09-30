import customtkinter as ctk
import pandas as pd

def do_quiz():
    pass

#creating new quiz
def new_question():
    correct_ans = "-"

    #set elements
    question_Textbox.configure(state = "normal")
    question_Textbox.delete("0.0", "end")
    question_Textbox.insert("0.0", "Írj ide egy címet!")

    A_btn.configure(text = "Correct", command = lambda: correct_ans.replace("-", "A"))
    B_btn.configure(text = "Correct", command = lambda: correct_ans.replace("-", "B"))
    C_btn.configure(text = "Correct", command = lambda: correct_ans.replace("-", "C"))
    D_btn.configure(text = "Correct", command = lambda: correct_ans.replace("-", "D"))

    next_btn.configure(text = "Next Question", command = lambda: save_question(
        question_Textbox.get("0.0","end"),
        A_entry.get(),
        B_entry.get(),
        C_entry.get(),
        D_entry.get(),
        correct_ans
        ))
    
    submit_btn.configure(text = "Submit Quiz", command = lambda: submit_quiz(title_entry.get()))

    #place elements
    question_Textbox.place(relx = 0)

    A_entry.place(relx = 0.05, rely = 0.25)
    A_btn.place(relx = 0.6, rely = 0.25)

    B_entry.place(relx = 0.05, rely = 0.4)
    B_btn.place(relx = 0.6, rely = 0.4)

    C_entry.place(relx = 0.05, rely = 0.55)
    C_btn.place(relx = 0.6, rely = 0.55)

    D_entry.place(relx = 0.05, rely = 0.7)
    D_btn.place(relx = 0.6, rely = 0.7)

    title_entry.place(relx = 0.05, rely = 0.9)
    submit_btn.place(relx = 0.5, rely = 0.9)

    next_btn.place(relx = 0.75, rely = 0.9)
    

def quiz_menu():
    pass

def correct():
    pass

def incorrect():
    pass

def save_question(question : str, A : str, B : str, C : str, D : str, correct : str):
    global data_out
    data_out = pd.concat([data_out, pd.DataFrame({"question" : [question], "A" : [A], "B" : [B], "C" : [C], "D" : [D], "correct" : [correct]})], ignore_index=True)
    print(data_out)
    new_question()

def submit_quiz(title):
    data_out.to_csv(f"{title}.csv")
    data_out = pd.DataFrame({"question" : [], "A" : [], "B" : [], "C" : [], "D" : [], "correct" : []})
    main()

def main():
    print("lefut")


#global variables
WIDTH = 750
window = ctk.CTk()
window.geometry(f"{WIDTH}x{WIDTH // 3 * 2}")
window.resizable(False, False)
window.title("Kahoot 2")

FONT_FAMILY = "Roboto"
FONT_SIZE = 20
FONT = ctk.CTkFont(FONT_FAMILY, FONT_SIZE)


data_out = pd.DataFrame({"question" : [], "A" : [], "B" : [], "C" : [], "D" : [], "correct" : []})

#Elements
question_Textbox = ctk.CTkTextbox(window, width = WIDTH, height = 60, font = FONT)

start_btn = ctk.CTkButton(window, text = "Start", command = quiz_menu)
create_btn = ctk.CTkButton(window, text = "Create quiz", command = new_question)

A_btn = ctk.CTkButton(window, font = FONT)
B_btn = ctk.CTkButton(window, font = FONT)
C_btn = ctk.CTkButton(window, font = FONT)
D_btn = ctk.CTkButton(window, font = FONT)

next_btn = ctk.CTkButton(window, font = FONT)
submit_btn = ctk.CTkButton(window, font = FONT)

A_entry = ctk.CTkEntry(window, placeholder_text = '"A" option', width = WIDTH // 2, font = FONT)
B_entry = ctk.CTkEntry(window, placeholder_text = '"B" option', width = WIDTH // 2, font = FONT)
C_entry = ctk.CTkEntry(window, placeholder_text = '"C" option', width = WIDTH // 2, font = FONT)
D_entry = ctk.CTkEntry(window, placeholder_text = '"D" option', width = WIDTH // 2, font = FONT)
title_entry = ctk.CTkEntry(window, placeholder_text = 'Title of the quiz', width = WIDTH // 2.5, font = FONT)

new_question()
window.mainloop()