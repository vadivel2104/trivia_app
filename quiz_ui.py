import tkinter as tk
from game_engine import Quiz_format
WINDOWS_BG = "gray19"
from game_engine import Quiz_format


class QuizUI:

    def __init__(self, game_engine: Quiz_format):
        self.game = game_engine
        self.answer_received = ""
        self.score_update = 0
        self.ques = "Some Text"

        self.windows = tk.Tk()
        self.windows.title("Trivia Quiz")
        # self.windows.minsize(width=250,height=350)
        self.windows.config(padx=10, pady=10, bg=WINDOWS_BG)

        self.question_remaining_label = tk.Label(text=f"Questions Left:", font=("Courier", 10, "bold"), fg="white", bg=WINDOWS_BG)
        self.question_remaining_label.grid(row=0, column=1)

        self.score_label = tk.Label(text=f"Score:{self.score_update}", font=("Courier", 10, "bold"), fg="white", bg=WINDOWS_BG)
        self.score_label.grid(row=0, column=2)

        self.canvas = tk.Canvas(width=250, height=225, bg="white")
        self.canvas_question = self.canvas.create_text(125, 112, text="hello", width=200)
        self.canvas.grid(row=1, column=1, columnspan=2, pady=50)

        self.right_img = tk.PhotoImage(file="check_resized.png")
        self.right_button = tk.Button(width=90, height=100, bg="white", highlightthickness=0, image=self.right_img, command=self.answer_true)
        self.right_button.grid(row=2, column=1)

        self.wrong_img = tk.PhotoImage(file="cross_resized.png")
        self.wrong_button = tk.Button(width=90,height=100, bg=WINDOWS_BG, highlightthickness=0, image=self.wrong_img, command=self.answer_false)
        self.wrong_button.grid(row=2, column=2)

        self.to_display_question()

        self.no_questions_left()

        self.windows.mainloop()

    def to_display_question(self):
        if self.game.still_question_left():
            question = self.game.current_question()
            print(question)
            self.canvas.itemconfig(self.canvas_question, text=question)
            self.canvas.config(bg="white")
            self.windows.after(1000, self.no_questions_left)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.canvas_question, text="Game Over")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def no_questions_left(self):
        question_left = self.game.no_question
        self.question_remaining_label.config(text=f"Questions Left:{question_left -1}")

    def answer_true(self):
        if self.game.ans == "True":
            print("Correct")
            print(self.game.no_question)
            self.game.remove_ques()
            self.canvas.config(bg="green")
            self.score_update += 1
            self.score_label.config(text=f"Score:{self.score_update}")
        if self.game.ans != "True":
            print("Incorrect")
            print(self.game.no_question)
            self.canvas.config(bg="red")
            self.game.remove_ques()
            self.score_update += 0
            self.score_label.config(text=f"Score:{self.score_update}")
        self.windows.after(3000,self.to_display_question)
        self.windows.after(1000,self.no_questions_left)


    def answer_false(self):
        if self.game.ans == "False":
            print("Correct")
            print(self.game.no_question)
            self.score_update += 1
            self.canvas.config(bg="green")
            self.game.remove_ques()
            self.score_label.config(text=f"Score:{self.score_update}")
        if self.game.ans != "False":
            print("Incorrect")
            print(self.game.no_question)
            self.score_update += 0
            self.canvas.config(bg="red")
            self.game.remove_ques()
            self.score_label.config(text=f"Score:{self.score_update}")
        self.windows.after(3000,self.to_display_question)
        self.windows.after(1000,self.no_questions_left)













