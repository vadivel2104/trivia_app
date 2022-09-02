import random as rn


class Quiz_format:

    def __init__(self, quiz_list):
        self.quiz_list = quiz_list
        self.no_question = len(self.quiz_list)
        self.current_set = {}
        self.ques = ""
        self.ans = ""
        self.received_answer = ""
        self.score = 0
        self.current_question()


    def current_question(self):
        self.current_set = rn.choice(self.quiz_list)
        self.ques = self.current_set["question"]
        self.ans = self.current_set["answer"]
        self.no_question = len(self.quiz_list)
        return self.ques

    def to_check(self):
        if self.received_answer == self.ans:
            self.score += 1
        if self.received_answer != self.ans:
            self.score += 0

        return self.score

    def remove_ques(self):
        for data in self.quiz_list:
            if data == self.current_set:
                self.quiz_list.remove(self.current_set)

    def still_question_left(self):
        if len(self.quiz_list) > 0:
            return True









