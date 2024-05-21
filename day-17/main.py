from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in range(0,12):
    q = Question(question_data[i]["question"], question_data[i]["correct_answer"])
    question_bank.append(q)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    next_question = quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is {quiz.score}/{len(quiz.question_list)}")


