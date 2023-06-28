# pomodoro timer를 만들어보자!

# 모듈 불러오기 
from tkinter import *

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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

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
canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))   # 이미지 위에 들어갈 타이머(text) 설정 
canvas.grid(column=1, row=1)                                   # 설정한 cancas 명시 

# button 1 - start 
start_button = Button(text="Start", bg=YELLOW, highlightthickness=0)                     # start 버튼 설정 - 버튼 이름, 색상, 두깨 설정 
start_button.grid(column=0, row=2)                                                       # start 버튼 명시

# button 2 - Reset 
reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0)                     # reset 버튼 설정 - 버튼 이름, 색상, 두깨 설정 
reset_button.grid(column=2, row=2)                                                       # reset 버튼 명시

# label 2 - checkmark 
timer_label = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, 'bold'))         # 체크마크 설정 - 체크마크, 색상, 폰트 설정 
timer_label.grid(column=1, row=3)                                                        # 체크마크 label 명시 


# 닫기 버튼 누르기 전까지 계속 구동
window.mainloop()