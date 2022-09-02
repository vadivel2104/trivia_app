from data import question_data
from quiz_list import Quiz_list
from game_engine import Quiz_format
from quiz_ui import QuizUI
import tkinter as tk



datas = question_data
print(datas)

quiz_list = Quiz_list()
list_format = quiz_list.quiz_list_format(datas)
print(list_format)

game = Quiz_format(list_format)
print(game.ques)

quizui = QuizUI(game)































# if self.answer == self.ans_text:
#     print("You are correct")
#     self.score += 1
#     print(f"You got {self.score}/{len(question_bank)}")
# if self.answer != self.ans_text:
#     print(f"Sorry, the correct answer is {self.ans_text}")
#     print(f"You got {self.score}/{len(question_bank)}")





