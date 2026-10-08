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
menu_frame = ctk.CTkFrame(window)
start_btn = ctk.CTkButton(menu_frame, text = "Start")
create_btn = ctk.CTkButton(menu_frame, text = "Create quiz")

#Create quiz
new_quiz_frame = ctk.CTkFrame(window)
new_quiz_btn_list = [ctk.CTkButton(new_quiz_frame, font=FONT) for _ in range(4)]
new_quiz = quiz_creator.Quiz_Creator(WIDTH, menu_frame, FONT, new_quiz_frame, new_quiz_btn_list)
create_btn.configure(command = lambda: new_quiz.new_question())

solve_quiz_frame = ctk.CTkFrame(window)
solve_quiz_btn_list = [ctk.CTkButton(solve_quiz_frame, font=FONT) for _ in range(4)]
solve_quiz = quiz.Quiz(WIDTH, menu_frame, FONT, solve_quiz_frame, solve_quiz_btn_list)
start_btn.configure(command = lambda: solve_quiz.quiz_selector())


#place button on temporary location for tests
start_btn.place(relx = 0.6, rely = 0.7)
create_btn.place(relx = 0.1, rely = 0.5)
menu_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
menu_frame.tkraise()

new_quiz_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
solve_quiz_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

window.mainloop()