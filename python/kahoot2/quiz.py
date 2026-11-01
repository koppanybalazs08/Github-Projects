import customtkinter as ctk
import CTkMessagebox as ctk_msg_box
import pandas as pd

#TODO: bugfixes

class Quiz():

    def __init__(self, WIDTH : int, last_elements, FONT, frame, btn_list, menu_points_textbox):
        #create width, font, output data, points and elements
        self.WIDTH = WIDTH
        self.FONT = FONT
        self.quiz_data = None
        self.points = 0
        self.question_number = 0

        self.file = None

        self.frame = frame
        self.last_elements = last_elements
        self.btn_list = btn_list
        self.next_btn = ctk.CTkButton(frame, font = FONT, text = "Next")
        self.question_textbox = ctk.CTkTextbox(frame, width = self.WIDTH, height = 60, font = FONT, fg_color = "#dee2ee")
        self.points_textbox = ctk.CTkTextbox(frame, width = 100, height = 40, font = FONT, fg_color = "#dee2ee")
        self.menu_points_textbox = menu_points_textbox

    def do_quiz(self):

        #Kérdés felirata
        self.question_textbox.configure(state = "normal")
        self.question_textbox.delete("0.0", "end")
        self.question_textbox.insert("0.0", self.quiz_data["question"].iloc[self.question_number].strip())
        self.question_textbox.configure(state = "disabled")

        self.btn_list[0].configure(fg_color = "#6AA647", hover_color = "#82BD60", text_color_disabled = "#B8B8B8",
        text = self.quiz_data["A"].iloc[self.question_number], command = lambda: self.check_correct(0), state = "normal")

        self.btn_list[1].configure(fg_color = "#6AA647", hover_color = "#82BD60", text_color_disabled = "#B8B8B8",
        text = self.quiz_data["B"].iloc[self.question_number], command = lambda: self.check_correct(1), state = "normal")

        self.btn_list[2].configure(fg_color = "#6AA647", hover_color = "#82BD60", text_color_disabled = "#B8B8B8",
        text = self.quiz_data["C"].iloc[self.question_number], command = lambda: self.check_correct(2), state = "normal")

        self.btn_list[3].configure(fg_color = "#6AA647", hover_color = "#82BD60", text_color_disabled = "#B8B8B8",
        text = self.quiz_data["D"].iloc[self.question_number], command = lambda: self.check_correct(3), state = "normal")

        self.next_btn.configure(command = self.next_question)

        #place elements
        self.question_textbox.place(relx = 0)

        self.btn_list[0].place(relx = 0.4, rely = 0.25)
        self.btn_list[1].place(relx = 0.4, rely = 0.4)
        self.btn_list[2].place(relx = 0.4, rely = 0.55)
        self.btn_list[3].place(relx = 0.4, rely = 0.7)

        self.next_btn.place(relx = 0.75, rely = 0.9)

        self.frame.tkraise()


    def quiz_selector(self):
        selecting = False
        while not selecting:
            self.file = ctk.filedialog.askopenfilename(filetypes = [("All files", "*.csv")])

            if self.file != "":
                self.quiz_data = pd.read_csv(self.file, index_col = 0)

                if list(self.quiz_data.columns) == ["question", "A", "B", "C", "D", "correct"]:
                    selecting = True
                    self.do_quiz()

                else:
                    ctk_msg_box.CTkMessagebox(title = "Not valid file!", 
                                            message = "Please make sure to select a .csv file with the folowing format: question,A,B,C,D,correct",
                                            icon = "warning",
                                            fg_color = "#dee2ee",
                                            bg_color = "#dee2ee")
            else:
                self.back_to_menu()
                selecting = True


    def check_correct(self, answer):
        correct = self.quiz_data["correct"].iloc[self.question_number]

        for i in range(len(self.btn_list)):
            if i == correct:
                self.btn_list[i].configure(state = "disabled")
            else:
                self.btn_list[i].configure(fg_color = "#A64747", hover_color = "#BD6060", state = "disabled")

        if answer == correct:
            self.points += 1

        self.points_textbox.configure(state = "normal")
        self.points_textbox.delete("0.0", "end")
        self.points_textbox.insert("0.0", f"{self.points}/{self.question_number + 1}")
        self.points_textbox.configure(state = "disabled")

        self.points_textbox.place(relx = 0.75, rely = 0.7)

    def next_question(self):
        if len(self.quiz_data) > self.question_number + 1:
            self.question_number += 1
            self.do_quiz()

        else:
            data_out = pd.read_csv("quiz_points.csv", index_col = 0)
            data_out = pd.concat([data_out, pd.DataFrame({
                "quiz_name": [self.file.split("/")[-1]],
                "points" : [self.points],
                "max_points": [self.question_number + 1]
            })],
            ignore_index=True)
            data_out.to_csv("quiz_points.csv")

            self.back_to_menu()

    def back_to_menu(self):
        self.menu_points_textbox.configure(state = "normal")
        self.menu_points_textbox.delete("0.0", "end")

        if self.question_number > 0:
            self.menu_points_textbox.insert("0.0", f"Points in the last quiz: {self.points}/{self.question_number + 1}")
        else:
            self.menu_points_textbox.insert("0.0", "Points in the last quiz: 0/0")

        self.menu_points_textbox.configure(state = "disabled")

        self.points = 0
        self.question_number = 0
        self.last_elements.tkraise()
