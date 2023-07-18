# 모듈 불러오기 
from random import choice, randint, shuffle
from tkinter import *

# ---------------------------- 상수 설정 ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# ---------------------------- UI SETUP ------------------------------- #
# 기본 설정 
window = Tk()                                                # tkinter 객체 선언 
window.title("Flashy")                                       # tkinter title 지정 
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)         # pad(간격) 및 배경색 설정

# canvas 사용 
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)      # canvas 객체 선언 - 선언시 크기 설정
card_front_image = PhotoImage(file="./img/card_front.png")                             # 배경 이미지 불러오기 - 카드 앞면 이미지 
canvas.create_image(400, 263, image=card_front_image)                                  # 이미지 명시 
canvas.create_text(400, 150, text="English", fill="black", font=(FONT_NAME, 40, "italic"))  # 이미지 위에 들어갈 text 설정 
canvas.create_text(400, 263, text="you", fill="black", font=(FONT_NAME, 60, "bold"))        # 이미지 위에 들어갈 text 설정 
canvas.grid(column=0, row=0, columnspan=2)                                             # 설정한 canvas 명시 

# button 1 - wrong 버튼 
cross_img = PhotoImage(file="./img/wrong.png")                  # 이미지 불러오기 
unknown_button = Button(image=cross_img, highlightthickness=0)    # 이미지에 버튼 설정 
unknown_button.grid(column=0, row=1)                                # 버튼 명시 

# button 2 - right 버튼 
check_img = PhotoImage(file="./img/right.png")                  # 이미지 불러오기 
known_button = Button(image=check_img, highlightthickness=0)    # 이미지에 버튼 설정
known_button.grid(column=1, row=1)                                # 버튼 명시 

# 닫기 버튼 누르기 전까지 계속 구동
window.mainloop()