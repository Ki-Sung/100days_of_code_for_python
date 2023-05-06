# Question Model -> 퀴즈 문제에 대한 모델 
# 문제(qustion)객체가 있다면 객체의 속성은? 
# 1)문제(text) 2)문제의 답(answer)

class Question:                              # Question 이라는 클래스 생성
    def __init__(self, q_text, q_answer):    # text와 answer, 두 속성을 초기화 하는 init 메소드 (입력 값 입력)
        self.text = q_text                   # 속성 설정 1. 문제를 위한 "text"
        self.answer = q_answer               # 속성 설정 2. 정답을 위한  "answer"