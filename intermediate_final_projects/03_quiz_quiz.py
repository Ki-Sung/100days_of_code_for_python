from quiz.question_mode import Question     # 퀴즈 문제에 대한 Question 클래스 불러오기 
from quiz.data import question_data         # 퀴즈 문제 및 정답에 대한 data 불러오기 
from quiz.quiz_brain import QuizBrain       # 퀴즈의 모든 질문과 퀴즈의 기능을 위한 QuizBrain 클래스 불러오기

# 퀴즈 문제 및 정답 정보 처리 - quiz 폴더 안 data.py 안에 있는 딕셔너리 형태 데이터 불러오기
question_bank = []                                                  # 문제, 문제 정답을 담기 위한 빈 List  
for question in question_data:                                      # 반복문 처리                   
    question_text = question["question"]                            # 문제 key 값의 value 담기 
    question_answer = question["correct_answer"]                    # 정답 key 값의 value 담기 
    new_question = Question(question_text, question_answer)         # Question 클래스 객체 생성 및 파라미터 설정 
    question_bank.append(new_question)                              # 뽑은 정보들 question_bank에 저장

# 퀴즈의 모든 질문과 퀴즈의 기능을 제어하기
quiz = QuizBrain(question_bank)        # QuizBrain 클래스 객체 생성 및 파미터 설정 

# 퀴즈가 남아있는지 확인 기능 제어
while quiz.stil_has_question():        # 문제가 남아있는지 체크 
    quiz.next_question()               # 만약 남아있다면(True이면) 다음 질문으로 넘어가고, 남아있지 않다면(False이면) 반복문 종료 
