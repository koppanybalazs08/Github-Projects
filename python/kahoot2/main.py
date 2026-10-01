import customtkinter as ctk
import quiz_creator

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

new_quiz = quiz_creator.Quiz_Creator(WIDTH, FONT, window, [A_btn, B_btn, C_btn, D_btn])

create_btn.configure(command = lambda: new_quiz.new_question())

create_btn.place(relx = 0.6, rely = 0.7)

window.mainloop()