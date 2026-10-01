import customtkinter as ctk
import pandas as pd

class Quiz_Creator:

    def __init__(self, WIDTH, FONT, window, btn_list):
        #create width, font, output data and elements
        print("lefut")
        self.WIDTH = WIDTH
        self.FONT = FONT
        self.data_out = pd.DataFrame({"question" : [], "A" : [], "B" : [], "C" : [], "D" : [], "correct" : []})
        self.correct_ans = "-"

        self.A_entry = ctk.CTkEntry(window, placeholder_text = '"A" option', width = self.WIDTH // 2, font = self.FONT)
        self.B_entry = ctk.CTkEntry(window, placeholder_text = '"B" option', width = self.WIDTH // 2, font = self.FONT)
        self.C_entry = ctk.CTkEntry(window, placeholder_text = '"C" option', width = self.WIDTH // 2, font = self.FONT)
        self.D_entry = ctk.CTkEntry(window, placeholder_text = '"D" option', width = self.WIDTH // 2, font = self.FONT)
        self.title_entry = ctk.CTkEntry(window, placeholder_text = 'Title of the quiz', width = self.WIDTH // 2.5, font = self.FONT)
        self.question_textbox = ctk.CTkTextbox(window, width = WIDTH, height = 60, font = FONT)
        self.next_btn = ctk.CTkButton(window, font = FONT)
        self.submit_btn = ctk.CTkButton(window, font = FONT)
        self.btn_list = btn_list


    #creating new quiz
    def new_question(self):

        #set elements
        self.question_textbox.configure(state = "normal")
        self.question_textbox.delete("0.0", "end")
        self.question_textbox.insert("0.0", "Írj ide egy címet!")

        self.btn_list[0].configure(text = "Correct", command = lambda: self.correct_ans.replace("-", "A"))
        self.btn_list[1].configure(text = "Correct", command = lambda: self.correct_ans.replace("-", "B"))
        self.btn_list[2].configure(text = "Correct", command = lambda: self.correct_ans.replace("-", "C"))
        self.btn_list[3].configure(text = "Correct", command = lambda: self.correct_ans.replace("-", "D"))

        self.next_btn.configure(text = "Next Question", command = lambda: self.save_question())
        
        self.submit_btn.configure(text = "Submit Quiz", command = lambda: self.submit_quiz(self.title_entry.get()))

        #place elements
        self.question_textbox.place(relx = 0)

        self.A_entry.place(relx = 0.05, rely = 0.25)
        self.btn_list[0].place(relx = 0.6, rely = 0.25)

        self.B_entry.place(relx = 0.05, rely = 0.4)
        self.btn_list[1].place(relx = 0.6, rely = 0.4)

        self.C_entry.place(relx = 0.05, rely = 0.55)
        self.btn_list[2].place(relx = 0.6, rely = 0.55)

        self.D_entry.place(relx = 0.05, rely = 0.7)
        self.btn_list[3].place(relx = 0.6, rely = 0.7)

        self.title_entry.place(relx = 0.05, rely = 0.9)
        self.submit_btn.place(relx = 0.5, rely = 0.9)

        self.next_btn.place(relx = 0.75, rely = 0.9)
        

    def save_question(self):
        self.data_out = pd.concat([self.data_out, pd.DataFrame({
        "question" : [self.question_textbox.get("0.0","end")], 
        "A" : [self.A_entry.get()], 
        "B" : [self.B_entry.get()], 
        "C" : [self.C_entry.get()], 
        "D" : [self.D_entry.get()], 
        "correct" : [self.correct_ans]})], 
        ignore_index=True)

        self.correct_ans = "-"
        self.new_question()

    def submit_quiz(self, title):
        self.data_out.to_csv(f"{title}.csv")
        self.data_out = pd.DataFrame({"question" : [], "A" : [], "B" : [], "C" : [], "D" : [], "correct" : []})