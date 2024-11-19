## 154. How to create your own class in python, ## 155. Working with attributes, class contructors and the init function,
## 156. Adding methods to a class, 
# """User class is created"""
# class User:
#     """init function is created"""
#     def __init__(self, id, name):
#         self.userId = id
#         self.userName = name
#         self.followers = 0
#         self.following = 0
    
#     """method declared"""
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1


# """user1 object is created"""
# user1 = User("001", "Anshu Sinha")
# print(user1.userId)
# print(user1.userName)
# print(user1.followers)

# """user2 object is created"""
# user2 = User("002", "Sahil Kumar Sinha")
# print(f"{user2.userId}\n{user2.userName}")

# user1.follow(user2)
# print(user1.followers)
# print(user1.following)
# print(user2.followers)
# print(user2.following)

#####

## Day 17: The quiz project
# Quiz

import data
from question_model import Question
from quiz_brain import QuizBrain


# switch to True to use the original questions
use_original = False

question_bank = []
# fill up the question bank list with Question objects
if use_original:
    for dic in data.original_question_data:
        question_bank.append(Question(dic["text"], dic["answer"]))
else:
    for dic in data.question_data:
        question_bank.append(Question(dic["question"], dic["correct_answer"]))

qb = QuizBrain(question_bank)
# repeat while there are still questions remaining
while qb.still_has_questions():
    qb.next_question()
# no need for a + 1 to the question_number here, as it gets increased after the last question is completed
print(f"Your final score is: {qb.score}/{qb.question_number}.")


