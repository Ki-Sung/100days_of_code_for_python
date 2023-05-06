from quiz.question_mode import Question     # 퀴즈 문제에 대한 Question 클래스 불러오기 
from quiz.data import question_data         # 퀴즈 문제 및 정답에 대한 data

# 퀴즈 문제 및 정답 정보 처리 - quiz 폴더 안 data.py 안에 있는 딕셔너리 형태 데이터 불러오기
question_bank = []                                                  # 문제, 문제 정답을 담기 위한 빈 List  
for question in question_data:                                      # 반복문 처리                   
    question_text = question["question"]                            # 문제 key 값의 value 담기 
    question_answer = question["correct_answer"]                    # 정답 key 값의 value 담기 
    new_question = Question(question_text, question_answer)         # Question 클래스 객체 생성 및 파라미터 설정 
    question_bank.append(new_question)                              # 뽑은 정보들 question_bank에 저장

# 결과 출력    
print(question_bank[0].text)
print(question_bank[0].answer)

