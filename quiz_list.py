import html
import random as rn

class Quiz_list:

    def quiz_list_format(self, question_data):
        return [{"question" : html.unescape(data["question"]), "answer": data["correct_answer"]} for data in question_data]







