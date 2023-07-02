# 모듈 불러오기 
from tkinter import * 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# 기본 설정 
window = Tk()                                     # tkinter 객체 선언 
window.title("Password Manager")                  # tkinter title 지정
window.config(padx=50, pady=50)                   # pad(간격) 및 배경색 설정

# canvas 사용 
canvas = Canvas(width=200, height=200)            # canvas 객체 선언 - 선언시 크기 설정 
lock_img = PhotoImage(file="./img/logo.png")      # 이미지 불러오기 
canvas.create_image(100, 100, image=lock_img)     # 이미지 생성 
canvas.grid(row=0, column=1)                      # canvas 명시 

# Labels
website_label = Label(text="Website:")            # label 1 설정 
website_label.grid(row=1, column=0)               # label 1 명시 

userid_label = Label(text="Email/Username:")      # label 2 설정 
userid_label.grid(row=2, column=0)                # label 2 명시 

password_label = Label(text="Password:")          # label 3 설정 
password_label.grid(row=3, column=0)              # label 3 명시 

# Entries
website_input = Entry(width=36)                       # input 1 설정 
website_input.grid(row=1, column=1, columnspan=2)     # input 1 명시

userid_input = Entry(width=36)                        # input 2 설정 
userid_input.grid(row=2, column=1, columnspan=2)      # input 2 설정 

password_input = Entry(width=21)                      # input 3 설정 
password_input.grid(row=3, column=1)                  # input 3 설정 

# buttons
generate_button = Button(width=11, text="Generate Password")   # button 1 설정 
generate_button.grid(row=3, column=2)                          # button 2 명시  

add_button = Button(width=34, text="Add")                      # button 2 설정 
add_button.grid(row=4, column=1, columnspan=2)                 # button 2 명시 

# 닫기 버튼을 누르기 전까지 계속 구동
window.mainloop()
