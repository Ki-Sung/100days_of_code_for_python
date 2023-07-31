# QuizeBrain -> 퀴즈의 모든 질문과 퀴즈의 기능을 위한 Class 
# 기능 1: 사용자에게 다음 질문을 제시 
# 기능 2: 퀴즈의 정답을 맞췄는지 여부 확인 
# 기능 3: 퀴즈의 마지막 문제까지 도달했는지 여부 확인 

# 필요 속성: quetion_number - 퀴즈 문제 순서 / question_list - 질문 리스트  / score - 문제 점수
# 필요한 메소드 1: next_question() - 현재 퀴즈 질문 호출 및 입력할 정답 호출 기능
# 필요한 메소드 2: still_has_questions() - 뒤에 퀴즈가 남았는지 여부를 확인하는 기능
# 필요한 메소드 3: check_score() - 퀴즈 점수 체크를 위한 기능 
import html                                             # html 모듈 불러오기 

class QuizBrain:                                        # QuizBrain 이라는 클래스 생성 
    # 초기화 메소드 
    def __init__(self, q_list):                         # question_number, score(기본값이 0이기 때문에 여기서 생략), question_list, 두 속성을 초기화 하는 init 메소드 (입력 값 입력)
        self.question_number = 0                        # 속성 설정 1. 문제 번호를 위한 "question_number"
        self.score = 0                                  # 속성 설정 2. 점수를 메기기 위한 "score" 
        self.question_list = q_list                     # 속성 설정 3. quiz 데이터를 뽑기 위한 "question_list"
        self.current_question = None                    # 속성 설정 4. currenct_question = None 설정

    # still_has_questions() - 뒤에 퀴즈가 남았는지 여부를 확인하는 기능
    def still_has_questions(self):                               
        return self.question_number < len(self.question_list)    # 아래의 구조를 하나로 작성 
        # if self.question_number < len(self.question_list):                     # 리스트에 있는 질문의 개수만큼 반복 실행되길 원함 - question_number가 question_list의 길이 보다 적다면,
        #     return True                                                        # True를 반환 
        # else:                                                                  # question_number가 question_list의 길이 보다 크다면,
        #     return False                                                       # False를 반환 
    
    # next_question 메소드 - question_list에서 현재 질문 번호의 항목을 가져오고, input 함수를 이용해서 입력한 정답을 호출하는 기능
    def next_question(self):
        self.current_question = self.question_list[self.question_number]            # 현재 퀴즈 질문 - question_list[question_number]
        self.question_number += 1                                                   # 문제 번호 더하기 - 해당 설정을 하지 않으면, Q.0으로 넘버링이 됨 
        q_text = html.unescape(self.current_question.text)                          # question text 선언 후 html 언이스케이프
        
        return f"Q.{self.question_number}: {q_text} (True/False): "                 # 입력할 정답 호출 
    
        # 콘솔창에 질문 출력용 
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")   # 입력할 정답 호출 
        # self.check_answer(user_answer)                                              # 입력할 정답의 값들을 check_answer로 전달 

    # check_answer 메소드 - 유저가 입력한 값과 정답을 비교하여 점수를 체크하는 기능 
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer          
        if user_answer.lower() == correct_answer.lower():          # 만약 유저가 입력한 정답과, 문제 정답이 같으면
            self.score += 1                                        # 점수 1씩 증가 
            print("You got it right!")                             # 결과 출력 
        else:                                                      # 만약 다르다면
            print("That's wrong.")                                 # 결과 출력 

        print(f"The correct answer was: {correct_answer}")                     # 문제의 정답 출력 
        print(f"Your current score is: {self.score}/{self.question_number}")   # 점수 출력 
        print("\n")                                                            # 다음 문제를 위해 줄 바꾸기 
