import customtkinter as ctk
import quiz_creator
import quiz

#Globals
WIDTH = 750
window = ctk.CTk()
window.geometry(f"{WIDTH}x{WIDTH // 3 * 2}")
window.resizable(False, False)
window.title("Kahoot 2")

FONT_FAMILY = "Roboto"
FONT_SIZE = 20
FONT = ctk.CTkFont(FONT_FAMILY, FONT_SIZE)

#Elements
start_btn = ctk.CTkButton(window, text = "Start")
create_btn = ctk.CTkButton(window, text = "Create quiz")

A_btn = ctk.CTkButton(window, font = FONT)
B_btn = ctk.CTkButton(window, font = FONT)
C_btn = ctk.CTkButton(window, font = FONT)
D_btn = ctk.CTkButton(window, font = FONT)

#Create quiz
new_quiz = quiz_creator.Quiz_Creator(WIDTH, [start_btn, create_btn], FONT, window, [A_btn, B_btn, C_btn, D_btn])
create_btn.configure(command = lambda: new_quiz.new_question())

solve_quiz = quiz.Quiz(WIDTH, [start_btn, create_btn], FONT, window, [A_btn, B_btn, C_btn, D_btn])
start_btn.configure(command = lambda: solve_quiz.quiz_selector())


#place button on temporary location for tests
start_btn.place(relx = 0.6, rely = 0.7)
create_btn.place(relx = 0.1, rely = 0.5)

window.mainloop()