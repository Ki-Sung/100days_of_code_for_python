# 모듈 불러오기 
from tkinter import * 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# 기본 설정 
window = Tk()                                     # tkinter 객체 선언 
window.title("Password Manager")                  # tkinter title 지정
window.config(padx=20, pady=20)                   # pad(간격) 및 배경색 설정

# canvas 사용 
canvas = Canvas(width=200, height=200)            # canvas 객체 선언 - 선언시 크기 설정 
lock_img = PhotoImage(file="./img/logo.png")      # 이미지 불러오기 
canvas.create_image(100, 100, image=lock_img)     # 이미지 생성 
canvas.pack()                                     # canvas 명시 


# 닫기 버튼을 누르기 전까지 계속 구동
window.mainloop()
