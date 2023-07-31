from quiz_module.question_model import Question
from quiz_module.data import question_data
from quiz_module.quiz_brain import QuizBrain
from quiz_module.ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface()       # UI의 QuizInterface 클래스 불러오기

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")