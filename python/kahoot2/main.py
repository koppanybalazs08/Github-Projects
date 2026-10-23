import customtkinter as ctk
import pandas as pd
import quiz_creator
import quiz

#Varibles
WIDTH = 750
window = ctk.CTk()
window.geometry(f"{WIDTH}x{WIDTH // 3 * 2}")
window.resizable(False, False)
window.title("Kahoot 2")

FONT_FAMILY = "Roboto"
FONT_SIZE = 20
FONT = ctk.CTkFont(FONT_FAMILY, FONT_SIZE)
points_data = pd.read_csv("quiz_points.csv", index_col = 0)


#Menu frame
menu_frame = ctk.CTkFrame(window, fg_color = "#dee2ee")
start_btn = ctk.CTkButton(menu_frame, text = "Start")
create_btn = ctk.CTkButton(menu_frame, text = "Create quiz")

title_textbox = ctk.CTkTextbox(menu_frame, width = WIDTH, height = 60, font = FONT, fg_color = "#dee2ee")
title_textbox.insert("0.0", "Kahoot 2")
title_textbox.configure(state = "disabled")

points_textbox = ctk.CTkTextbox(menu_frame, width = WIDTH, height = 60, font = FONT, fg_color = "#dee2ee")
if len(points_data) > 0:
    points_textbox.insert("0.0", f"Legutolsó quiz pontjai: {points_data["points"].iloc[-1]}/{points_data["max_points"].iloc[-1]}")
else:
    points_textbox.insert("0.0", "Legutolsó quiz pontjai: 0/0")
points_textbox.configure(state = "disabled")

#Create quiz frame
new_quiz_frame = ctk.CTkFrame(window, fg_color = "#dee2ee")
new_quiz_btn_list = [ctk.CTkButton(new_quiz_frame, font=FONT) for _ in range(4)]
new_quiz = quiz_creator.Quiz_Creator(WIDTH, menu_frame, FONT, new_quiz_frame, new_quiz_btn_list)
create_btn.configure(command = lambda: new_quiz.new_question())

#Solve quiz frame
solve_quiz_frame = ctk.CTkFrame(window, fg_color = "#dee2ee")
solve_quiz_btn_list = [ctk.CTkButton(solve_quiz_frame, font=FONT) for _ in range(4)]
solve_quiz = quiz.Quiz(WIDTH, menu_frame, FONT, solve_quiz_frame, solve_quiz_btn_list, points_textbox)
start_btn.configure(command = lambda: solve_quiz.quiz_selector())

menu_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
menu_frame.tkraise()

title_textbox.place(relx = 0, rely = 0)
points_textbox.place(relx = 0.5, rely = 0)

create_btn.place(relx = 0.2, rely = 0.5)
start_btn.place(relx = 0.6, rely = 0.5)

new_quiz_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
solve_quiz_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

window.mainloop()