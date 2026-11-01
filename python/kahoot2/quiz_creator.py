import customtkinter as ctk
import pandas as pd

#TODO: bugfixes

class Quiz_Creator:

    def __init__(self, WIDTH : int, last_elements : list, FONT, frame, btn_list):

        #create width, font, output data and elements
        self.WIDTH = WIDTH
        self.FONT = FONT
        self.data_out = pd.DataFrame({"question" : [], "A" : [], "B" : [], "C" : [], "D" : [], "correct" : []})
        self.correct_ans = ctk.StringVar(value = "-")

        self.frame = frame
        self.last_elements = last_elements
        self.title_entry = ctk.CTkEntry(self.frame, placeholder_text = "Title of the quiz", width = self.WIDTH // 2.5, font = self.FONT)
        self.question_entry = ctk.CTkEntry(self.frame, placeholder_text = "Title of the question", width = self.WIDTH // 2.5, font = FONT)
        self.next_btn = ctk.CTkButton(self.frame, font = FONT)
        self.submit_btn = ctk.CTkButton(self.frame, font = FONT)
        self.btn_list = btn_list
        self.options_entry_list = [
        ctk.CTkEntry(self.frame, placeholder_text = '"A" option', width = self.WIDTH // 2, font = self.FONT),
        ctk.CTkEntry(self.frame, placeholder_text = '"B" option', width = self.WIDTH // 2, font = self.FONT),
        ctk.CTkEntry(self.frame, placeholder_text = '"C" option', width = self.WIDTH // 2, font = self.FONT),
        ctk.CTkEntry(self.frame, placeholder_text = '"D" option', width = self.WIDTH // 2, font = self.FONT)]

    #creating new quiz
    def new_question(self):

        #configure buttons
        self.btn_list[0].configure(fg_color = "#6AA647", hover_color = "#82BD60", text_color_disabled = "#B8B8B8", 
        text = "A Correct", command = lambda: self.set_correct_ans(0), state = "normal")

        self.btn_list[1].configure(fg_color = "#6AA647", hover_color = "#82BD60", text_color_disabled = "#B8B8B8", 
        text = "B Correct", command = lambda: self.set_correct_ans(1), state = "normal")

        self.btn_list[2].configure(fg_color = "#6AA647", hover_color = "#82BD60", text_color_disabled = "#B8B8B8", 
        text = "C Correct", command = lambda: self.set_correct_ans(2), state = "normal")

        self.btn_list[3].configure(fg_color = "#6AA647", hover_color = "#82BD60", text_color_disabled = "#B8B8B8", 
        text = "D Correct", command = lambda: self.set_correct_ans(3), state = "normal")

        self.next_btn.configure(text = "Next Question", command = lambda: self.save_question())
        
        self.submit_btn.configure(text = "Submit Quiz", command = lambda: self.submit_quiz())

        self.title_entry.configure(placeholder_text_color = "#52504e")
        self.question_entry.configure(placeholder_text_color = "#52504e")
        for entry in self.options_entry_list:
            entry.configure(placeholder_text_color = "#52504e")

        #place elements
        self.question_entry.place(relx = 0.05, rely = 0.05)

        for i in range(len(self.btn_list)):
            self.btn_list[i].place(relx = 0.6, rely = 0.25 + (i * 0.15))
            self.options_entry_list[i].place(relx = 0.05, rely = 0.25 + (i * 0.15))

        self.title_entry.place(relx = 0.05, rely = 0.9)
        self.submit_btn.place(relx = 0.5, rely = 0.9)

        self.next_btn.place(relx = 0.75, rely = 0.9)

        self.frame.tkraise()

    #save the correct answer and dissable all buttons letter : which button is the correct (A-D) index: button index (0-3)
    def set_correct_ans(self, index : int):
        self.correct_ans.set(index)

        for btn in self.btn_list:
            btn.configure(state = "disabled")
        self.btn_list[index].configure(text_color_disabled = "#ffffff")

    #save the question to DataFrame, and reset values
    def save_question(self):
        if not (
            self.question_entry.get() == ""
            or self.options_entry_list[0].get() == "" #A entry
            or self.options_entry_list[1].get() == "" #B entry
            or self.options_entry_list[2].get() == "" #C entry
            or self.options_entry_list[3].get() == "" #D entry
            or self.correct_ans.get() == ""
            ):
            
            self.data_out = pd.concat([self.data_out, pd.DataFrame({
            "question" : [self.question_entry.get()], 
            "A" : [self.options_entry_list[0].get()], #A entry
            "B" : [self.options_entry_list[1].get()], #B entry
            "C" : [self.options_entry_list[2].get()], #C entry
            "D" : [self.options_entry_list[3].get()], #D entry
            "correct" : [self.correct_ans.get()]})], 
            ignore_index=True)

            self.correct_ans.set("-")
            self.question_entry.set("")
            for entry in self.options_entry_list:
                entry.set("")

            return True, self.new_question()

        self.question_entry.configure(placeholder_text_color = "#FF9D9D")
        for entry in self.options_entry_list:
            entry.configure(placeholder_text_color = "#FF9D9D")
        return False, None

    #save quiz to file, and reset the data_out DataFrame
    def submit_quiz(self):
        is_valid, func = self.save_question()
        if is_valid and self.title_entry.get() != "":
            self.data_out.to_csv(f"{self.title_entry.get()}.csv")

            self.title_entry.set("")
            self.data_out = pd.DataFrame({"question" : [], "A" : [], "B" : [], "C" : [], "D" : [], "correct" : []})

            self.last_elements.tkraise()
        else:
            self.title_entry.configure(placeholder_text_color = "#FF9D9D")
