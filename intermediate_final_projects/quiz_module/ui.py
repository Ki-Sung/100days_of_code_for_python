# UI 설정을 위한 클래스 

# 모듈 불러오기 
from tkinter import *
from quiz_module.quiz_brain import QuizBrain

# 상수설정 - 테마 색상 
THEME_COLOR = "#375362"

# quiz UI를 위한 QuizInterface 클래스 선언 
class QuizInterface:
    
    # 초기값 설정
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain                                                    # 새로운 클래스를 선언해서 시작할 때 받은 quiz_brain과 같다고 설정
        self.window = Tk()                                                        # tkinter 객체 선언 
        self.window.title("Quizzler")                                             # tkinter title 지정
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)                      # pad(간격) 및 배경색 설정
        
        # Labels 
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)     # Label 1 - 점수판 설정 
        self.score_label.grid(row=0, column=1)                                    # grid로 명시 
        
        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")                   # canvas 객체 선언 - 선언시 크기 및 배경 색상 설정 
        self.question_text = self.canvas.create_text(                             # text판 선언 
                                                    150,                          # x값 
                                                    125,                          # y값 
                                                    width=280,                    # 넓이값 280
                                                    text="Some Question Text",    # Text 
                                                    fill=THEME_COLOR,             # 배경색상 
                                                    font=("Arial", 20, "italic")  # 폰트 설정 
                                                    )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)                  # grid로 명시 
        
        # buttons
        ture_image = PhotoImage(file="./img/true.png")                                                       # true 버튼에 사용할 이미지 불러오기 
        self.true_button = Button(image=ture_image, highlightthickness=0, command=self.true_pressed)         # 버튼 설정 - 이미지 설정 및 테두리 제거 
        self.true_button.grid(row=2, column=0)                                                               # grid로 명시 
        
        false_image = PhotoImage(file="./img/false.png")                                                    # false 버튼에 사용할 이미지 불러오기 
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)     # 버튼 설정 - 이미지 설정 및 테두리 제거 
        self.false_button.grid(row=2, column=1)                                                             # gird로 명시 
        
        self.get_next_question()                                                  # 버튼을 누르면 다음 문제로 넘어가기 
        
        # 닫기 버튼을 누르기 전까지 계속 구동
        self.window.mainloop()
    
    # 다음 질문을 출력하기 위한 메소드 
    def get_next_question(self):
        self.canvas.config(bg="white")                                             # 다음 문제로 넘어갈 시 배경 하얀색으로 계속 설정 
        if self.quiz.still_has_questions():                                        # 만약 뒤에 퀴즈가 남아 있다면
            self.score_label.config(text=f"Score: {self.quiz.score}")              # 점수 명시 
            q_text = self.quiz.next_question()                                     # 질문 text 변수에 저장 
            self.canvas.itemconfig(self.question_text, text=q_text)                # 질문 명시 
        else:                                                                      # 만약 다음 문제가 없다면 
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")   # 문제가 없다라는 문구 명시 
            self.true_button.config(state="disabled")                              # 체크 버튼 (True) 버튼 비활성화 
            self.false_button.config(state="disabled")                             # 엑스 버튼 (False) 버튼 비활성화 
    
    # True 버튼 동작 메소드 
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))                         # 버튼을 누른다면 True 출력 
    
    # False 버튼 동작 메소드 
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")                                 # 버튼을 누른다면 False 출력 
        self.give_feedback(is_right)
    
    # 화면에 피드백이 나오는 함수 
    def give_feedback(self, is_right):
        if is_right:                                                               # 만약 is_right(정답일 경우) 이면 
            self.canvas.config(bg="green")                                         # 문제 창에 초록색 명시 
        else:                                                                      # 만약 그 반대이면 
            self.canvas.config(bg="red")                                           # 문제 창에 빨간색 명시 
            
        self.window.after(1000, self.get_next_question)                            # 다음 문제 출력 