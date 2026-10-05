import customtkinter as ctk
import pandas as pd

class Quiz_Creator:

    def __init__(self, WIDTH : int, last_elements : list, FONT, window, btn_list):

        #create width, font, output data and elements
        self.WIDTH = WIDTH
        self.FONT = FONT
        self.data_out = pd.DataFrame({"question" : [], "A" : [], "B" : [], "C" : [], "D" : [], "correct" : []})
        self.correct_ans = ctk.StringVar(value = "-")

        self.last_elements = last_elements
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

        if self.last_elements[0].winfo_manager() != "":
            for element in self.last_elements:
                element.place_forget()

        #set elements
        self.question_textbox.configure(state = "normal")
        self.question_textbox.delete("0.0", "end")
        self.question_textbox.insert("0.0", "Írj ide egy címet!")

        #configure buttons
        self.btn_list[0].configure(fg_color = "#6AA647", hover_color = "#82BD60", text_color_disabled = "#B8B8B8", 
        text = "Correct", command = lambda: self.set_correct_ans(0), state = "normal")
        
        self.btn_list[1].configure(fg_color = "#6AA647", hover_color = "#82BD60", text_color_disabled = "#B8B8B8", 
        text = "Correct", command = lambda: self.set_correct_ans(1), state = "normal")
        
        self.btn_list[2].configure(fg_color = "#6AA647", hover_color = "#82BD60", text_color_disabled = "#B8B8B8", 
        text = "Correct", command = lambda: self.set_correct_ans(2), state = "normal")
        
        self.btn_list[3].configure(fg_color = "#6AA647", hover_color = "#82BD60", text_color_disabled = "#B8B8B8", 
        text = "Correct", command = lambda: self.set_correct_ans(3), state = "normal")

        self.next_btn.configure(text = "Next Question", command = lambda: self.save_question())
        
        self.submit_btn.configure(text = "Submit Quiz", command = lambda: self.submit_quiz())

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

    #save the correct answer and dissable all buttons letter : which button is the correct (A-D) index: button index (0-3)
    def set_correct_ans(self, index : int):
        self.correct_ans.set(index)
        self.btn_list[0].configure(state = "disabled")
        self.btn_list[1].configure(state = "disabled")
        self.btn_list[2].configure(state = "disabled")
        self.btn_list[3].configure(state = "disabled")
        self.btn_list[index].configure(text_color_disabled = "#ffffff")

    #save the question to DataFrame, and reset values
    def save_question(self):
        self.data_out = pd.concat([self.data_out, pd.DataFrame({
        "question" : [self.question_textbox.get("0.0","end")], 
        "A" : [self.A_entry.get()], 
        "B" : [self.B_entry.get()], 
        "C" : [self.C_entry.get()], 
        "D" : [self.D_entry.get()], 
        "correct" : [self.correct_ans.get()]})], 
        ignore_index=True)

        self.correct_ans.set("-")
        self.A_entry.set("")
        self.B_entry.set("")
        self.C_entry.set("")
        self.D_entry.set("")

        self.new_question()

    #save quiz to file, and reset the data_out DataFrame
    def submit_quiz(self):
        self.data_out.to_csv(f"{self.title_entry.get()}.csv")

        self.title_entry.set("")
        self.data_out = pd.DataFrame({"question" : [], "A" : [], "B" : [], "C" : [], "D" : [], "correct" : []})

        self.A_entry.place_forget()
        self.B_entry.place_forget()
        self.C_entry.place_forget()
        self.D_entry.place_forget()
        self.title_entry.place_forget()
        self.question_textbox.place_forget()
        self.next_btn.place_forget()
        self.submit_btn.place_forget()

        for btn in self.btn_list:
            btn.place_forget()

        for element in self.last_elements:
            element.place_forget()
