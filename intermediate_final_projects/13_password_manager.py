# 모듈 불러오기 
from random import choice, randint, shuffle
from tkinter import *            # 모든 클래스와 상수만을 임포트 함
from tkinter import messagebox   # messagebox는 또다른 코드 모듈이기 때문에 따로 임포트 해야함. 
import pyperclip                 # 클리보드 생성기 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# 비밀번호 생성 기능 만들기
def generate_password():
    # 비밀번호 조합을 위한 알파벳, 숫자, 기호들 
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # password random 조합
    password_letters = [choice(letters) for _ in range(randint(8, 10))]     # 알파벳 (대,소문자 상관 X) 8 ~ 10 글자 랜덤으로 추출 
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]      # 기호 2 ~ 4 글자 랜덤으로 추출 
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]      # 숫자 2 ~ 4 글자 랜덤으로 추출  

    password_list = password_letters + password_symbols + password_numbers    # 알파벳, 기호, 숫자 조합하기 
    shuffle(password_list)                                                    # 조합한 passwordlist 섞기 

    password = "".join(password_list)                                       # list 형식을 join 함수를 사용하여 구분자("") 기준으로 문자열 형식으로 합치기 
    password_input.insert(0, password)                                      # password Etry에 출력하기 
    pyperclip.copy(password)                                                # 생성된 password를 복사 하기 위해 클립보드 생성 
    # password = ""
    # for char in password_list:
    #     password += char
# ---------------------------- SAVE PASSWORD ------------------------------- #
# 입력한 정보 저장 기능 함수 
def save():
    # get 메소드 사용 - 입력한 내용을 전달하는 역할
    website = website_input.get()        # website 명 
    email = userid_input.get()           # user_id
    password = password_input.get()      # password 명 
    
    # 유효성 검사 
    if len(website) == 0 or len(password) == 0:       # 만약 website, password가 입력되지 않았다면,
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")   # 메시지 출력
    
    # 그외 
    else:
        # messagebox 기능 추가 - 입려창에 입력 후 확인 팝업 생성 
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                            f"\nPassword: {password} \nIs it Ok to save?")
        if is_ok:
            with open("data/data.txt", "a") as data_file:                # "append"모드로 text 파일에 저장 
                data_file.write(f"{website} | {email} | {password}\n")   # "write"모드로 data.text 파일 저장
                website_input.delete(0, END)                             # 파일 저장 후 이전에 입력한 website 명을 삭제 
                password_input.delete(0, END)                            # 파일 저장 후 이전에 입력한 password 삭제 

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
website_input.focus()                                 # 시작시 webside input box에 커서 자동 생성

userid_input = Entry(width=36)                           # input 2 설정 
userid_input.grid(row=2, column=1, columnspan=2)         # input 2 설정 
userid_input.insert(0, "kisung.kim@a1mediagroup.co.kr")  # 시작시 user_id를 미리 채워넣기


password_input = Entry(width=21)                      # input 3 설정 
password_input.grid(row=3, column=1)                  # input 3 설정 

# buttons
generate_button = Button(width=11, text="Generate Password", command=generate_password)   # button 1 설정 
generate_button.grid(row=3, column=2)                          # button 2 명시  

add_button = Button(width=34, text="Add", command=save)        # button 2 설정 - Add 버튼 클릭시 save 함수 동작
add_button.grid(row=4, column=1, columnspan=2)                 # button 2 명시 

# 닫기 버튼을 누르기 전까지 계속 구동
window.mainloop()
