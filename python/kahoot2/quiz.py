import customtkinter as ctk
import pandas as pd

class Quiz():

    def __init__(self, WIDTH : int, last_elements : list, FONT, frame, btn_list):
        #create width, font, output data, points and elements
        self.WIDTH = WIDTH
        self.FONT = FONT
        self.quiz_data = None
        self.points = 0

        self.frame = frame
        self.last_elements = last_elements
        self.btn_list = btn_list
        self.next_btn = ctk.CTkButton(frame, font = FONT, text = "Next")
        self.question_textbox = ctk.CTkTextbox(frame, width = WIDTH, height = 60, font = FONT)

    def do_quiz(self, question_number):

        #Kérdés felirata
        self.question_textbox.configure(state = "normal")
        self.question_textbox.delete("0.0", "end")
        self.question_textbox.insert("0.0", self.quiz_data["question"].iloc[question_number].strip())
        self.question_textbox.configure(state = "disabled")

        self.btn_list[0].configure(fg_color = "#6AA647", hover_color = "#82BD60", text_color_disabled = "#B8B8B8",
        text = self.quiz_data["A"].iloc[question_number], command = lambda: self.check_correct(question_number, 0), state = "normal")

        self.btn_list[1].configure(fg_color = "#6AA647", hover_color = "#82BD60", text_color_disabled = "#B8B8B8",
        text = self.quiz_data["B"].iloc[question_number], command = lambda: self.check_correct(question_number, 1), state = "normal")

        self.btn_list[2].configure(fg_color = "#6AA647", hover_color = "#82BD60", text_color_disabled = "#B8B8B8",
        text = self.quiz_data["C"].iloc[question_number], command = lambda: self.check_correct(question_number, 2), state = "normal")

        self.btn_list[3].configure(fg_color = "#6AA647", hover_color = "#82BD60", text_color_disabled = "#B8B8B8",
        text = self.quiz_data["D"].iloc[question_number], command = lambda: self.check_correct(question_number, 3), state = "normal")

        self.next_btn.configure(command = lambda: self.next_question(question_number))

        #place elements
        self.question_textbox.place(relx = 0)

        self.btn_list[0].place(relx = 0.4, rely = 0.25)
        self.btn_list[1].place(relx = 0.4, rely = 0.4)
        self.btn_list[2].place(relx = 0.4, rely = 0.55)
        self.btn_list[3].place(relx = 0.4, rely = 0.7)

        self.next_btn.place(relx = 0.75, rely = 0.9)

        self.frame.tkraise()


    def quiz_selector(self):
        self.quiz_data = pd.read_csv(ctk.filedialog.askopenfilename(), index_col = 0)
        self.do_quiz(0)

    def check_correct(self, question_number, answer):
        correct = self.quiz_data["correct"].iloc[question_number]

        for i in range(len(self.btn_list)):
            if i == correct:
                self.btn_list[i].configure(state = "disabled")
            else:
                self.btn_list[i].configure(fg_color = "#A64747", hover_color = "#BD6060", state = "disabled")

        if answer == correct:
            self.points += 1

    def next_question(self, question_number):
        if len(self.quiz_data) > question_number + 1:
            self.do_quiz(question_number + 1)
        else:
            self.last_elements.tkraise()
