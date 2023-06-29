# pomodoro timer를 만들어보자!

# 모듈 불러오기 
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
# color
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
# word font
FONT_NAME = "Courier"
# timer 
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# global variable
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
# 타이머 리셋 
def reset_timer():
    window.after_cancel(timer)                    # timer 정지 
    canvas.itemconfig(timer_text, text="00:00")   # 정지 후 "00:00"로 표시 
    title_label.config(text="Timer")              # 타이틀 "Timer"로 표시 
    check_mark.config(text="")                    # 체크 박스 없애기 
    global reps                                   # global 변수 불러와서 
    reps = 0                                      # 0으로 설정 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
# 타이머 함수 설정 
def start_timer():
    global reps                        # 전역 변수 불러오기 
    reps += 1                          # 전역 변수에서 1 더하기 
    
    # 시간 설정 
    work_sec = WORK_MIN * 60                 # work time -> 25분 
    short_break_sec = SHORT_BREAK_MIN * 60   # short break time -> 5분 
    long_break_sec = LONG_BREAK_MIN * 60     # long break time -> 20분 
    
    # reps 마다 타이머 설정 
    if reps % 8 == 0:                                 # 만약 8번째 reps이면 
        count_down(long_break_sec)                    # 20분 출력 
        title_label.config(text="Break", fg=RED)      # title "Break" 출력 
    elif reps % 2 == 0:                               # 만약 2/4/6 번째 reps이면 
        count_down(short_break_sec)                   # 5분 출력 
        title_label.config(text="Break", fg=PINK)     # title "Break" 출력 
    else:                                             # 나머지 
        count_down(work_sec)                          # 25분 출력 
        title_label.config(text="Working", fg=GREEN)  # title "Working" 출력 
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# count_down 함수 설정 
def count_down(count):
    # 카운트다운 시작 시간 설정 
    count_min = math.floor(count / 60)                                    # 분 계산 - count(초) / 60(초)
    count_sec = count % 60                                                # 초 계산 - count(초) % 60(초) -> 나머지 
    if count_sec < 10:                                                    # 만약 count_sec이 10 미만일 겨우 
        count_sec = f"0{count_sec}"                                       # count_sec을 00 형식으로 설정 (예:09)
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")        # canvas.itemconfig() - tkinter를 동적으로 나타낼 수 있는 메소드 
    if count > 0:                                                         # 만약 count가 0 보다 크면
        global timer                                                      # global 변수 timer 불러오기 (None)
        timer = window.after(1000, count_down, count - 1)                 # 1초 뒤에 say_somthing 함수를 이용하여 카운트다운 호출 (1씩 줄어듬)
    else:                                                                 # 나머지 
        start_timer()                                                     # 타이머 다시 시작 (start_timer 함수 재가동)
        marks = ""                                                        
        work_session = math.floor(reps/2)                                 # work session 설정 0, 2, 4
        for _ in range(work_session):                                     # work session 마다 반복 
            marks += "✔"                                                  # 체크 마크 표시 
        check_mark.config(text=marks)                                     # 체크 마크 명시 
# ---------------------------- UI SETUP ------------------------------- #
# 기본 설정 
window = Tk()                                   # tkinter 객체 선언 
window.title('Pomodoro')                        # tkinter title 지정 
window.config(padx=100, pady=50, bg=YELLOW)     # pad(간격) 및 배경색 설정

# label 1 - Title 
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'bold'))   # 타이틀 설정 - text, 글자색상, 폰트
title_label.grid(column=1, row=0)                                                      # 타이틀 label 명시 

# canvas - img, background color, etc
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)                  # Canvas 객체 선언 - 선언시 윈도우 사이즈, 배경색, 이미지 경계선 설정 추가 
tomato_img = PhotoImage(file='./img/tomato.png')                                         # 이미지 불러오기 
canvas.create_image(100, 112, image=tomato_img)                                          # 이미지 생성 - 생성시 크기 설정 
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))   # 이미지 위에 들어갈 타이머(text) 설정 
canvas.grid(column=1, row=1)                                                             # 설정한 cancas 명시 

# button 1 - start 
start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)   # start 버튼 설정 - 버튼 이름, 색상, 두깨 설정 
start_button.grid(column=0, row=2)                                                          # start 버튼 명시

# button 2 - Reset 
reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)   # reset 버튼 설정 - 버튼 이름, 색상, 두깨 설정 
reset_button.grid(column=2, row=2)                                                          # reset 버튼 명시

# label 2 - checkmark 
check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, 'bold'))                   # 체크마크 설정 - 체크마크, 색상, 폰트 설정 
check_mark.grid(column=1, row=3)                                                        # 체크마크 label 명시 


# 닫기 버튼 누르기 전까지 계속 구동
window.mainloop()