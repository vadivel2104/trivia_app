import requests


URL = "https://opentdb.com/api.php?"
PARAMETERS = {
            "amount": 10,
            "type": "boolean",
        }

response = requests.get(url=URL, params=PARAMETERS)
data = response.json()
question_data = data["results"]


# quiz_list = [{"question" : data["question"], "answer": data["correct_answer"]} for data in question_data]
#
# print(question_data)
# print(quiz_list)
#
# question = ""
# answer = ""
# no_question = len(quiz_list)
# score = 0
#
#
# for data in range(no_question):
#     question = quiz_list[data]["question"]
#     answer = quiz_list[data]["answer"]
#     print(question)
#     if input("True or False: ") == answer:
#         score += 1
#         print(f"{score}/{no_question}")
#     else:
#         score += 0
#         print(f"{score}/{no_question}")



