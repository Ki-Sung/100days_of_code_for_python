# 모듈 불러오기 
from tkinter import *
import pandas as pd
import time
from random import choice, randint, shuffle

# ----------------------------- 상수 설정 ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# ------------------------- WORD GENERATOR ---------------------------- #
# 데이터 불러오기 
data = pd.read_csv("./data/English_Words.csv")            # 빈도 단어집 데이터 불러오기 
to_learn = data.to_dict(orient="records")                 # 데이터 프레임을 딕셔너리 형태로 변환 - [{열 : 값}] 형태로 
current_card = {}                                         # next_card와 flib_card 두 함수에 사용할 현재 카드 빈 딕셔너리 형태

# Random하게 단어 카드 생성 함수 
def next_card():
    global current_card, flip_timer                       # 위에 설정한 current_card와 flip_timer 전역 변수 설정 
    window.after_cancel(flip_timer)                       # 새로운 카드로 넘어갈 때 마다 타미어 무효로 만들기 위해 다음 버튼을 누르면 해당 타이머 다시 동작 
    current_card = choice(to_learn)                                           # 단어 Random하게 생성   
    canvas.itemconfig(card_title, text="English", fill="black")               # 캔버스 위젯에 대한 옵션 수행 (title인 English 명시 )
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")  # 캔버스 위젯에 대한 옵션 수행 (단어인 current_card에 있는 단어 명시) 
    canvas.itemconfig(card_background, image=card_front_image)                # 앞 쪽 카드 이미지로 전환
    flip_timer = window.after(3000, func=flip_card)        # 새로웈 카드 설정 후 3초 동안 가디로도록 새로운 flip_timer 설정 
    
# 뒤 집은 카드 설정 함수 
def flip_card():
    canvas.itemconfig(card_title, text="Korean", fill="white")                # 캔버스 위젯에 대한 옵션 수행 (title인 English 명시 )
    canvas.itemconfig(card_word, text=current_card["Korean"], fill="white")   # 캔버스 위젯에 대한 옵션 수행 (단어인 current_card에 있는 단어의 한국어 뜻 명시) 
    canvas.itemconfig(card_background, image=card_back_image)                 # 뒤 집은 카드 이미지로 전환 

# ---------------------------- UI SETUP ------------------------------- #
# 기본 설정 
window = Tk()                                                # tkinter 객체 선언 
window.title("Flashy")                                       # tkinter title 지정 
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)         # pad(간격) 및 배경색 설정

flip_timer = window.after(3000, func=flip_card)              # 3초가 지나면 카드를 뒤 집는 메커니즘 설정 

# canvas 사용 
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)      # canvas 객체 선언 - 선언시 크기 설정
card_front_image = PhotoImage(file="./img/card_front.png")                             # 배경 이미지 불러오기 - 카드 앞면 이미지 
card_back_image = PhotoImage(file="./img/card_back.png")                                 # 뒤집은 카드 배경 이미지 불러오기 
card_background = canvas.create_image(400, 263, image=card_front_image)                              # 이미지 명시 
card_title = canvas.create_text(400, 150, text="", fill="black", font=(FONT_NAME, 40, "italic"))     # 이미지 위에 들어갈 text 설정 
card_word = canvas.create_text(400, 263, text="", fill="black", font=(FONT_NAME, 60, "bold"))        # 이미지 위에 들어갈 text 설정 
canvas.grid(column=0, row=0, columnspan=2)                                             # 설정한 canvas 명시 

# button 1 - wrong 버튼 
cross_img = PhotoImage(file="./img/wrong.png")                  # 이미지 불러오기 
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_card)    # 이미지에 버튼 설정 (버튼을 누르면, 랜덤하게 단어 생성)
unknown_button.grid(column=0, row=1)                                # 버튼 명시 

# button 2 - right 버튼 
check_img = PhotoImage(file="./img/right.png")                  # 이미지 불러오기 
known_button = Button(image=check_img, highlightthickness=0, command=next_card)    # 이미지에 버튼 설정 (버튼을 누르면, 랜덤하게 단어 생성)
known_button.grid(column=1, row=1)                                # 버튼 명시 

# 위젯 화면에 바로 Title(English)과 단어가 보여질 수 있도록 명시 - 주의: mainloop() 전에 코드 작성
next_card()

# 닫기 버튼 누르기 전까지 계속 구동
window.mainloop()