# 모듈 불러오기 
from random import choice, randint, shuffle
from tkinter import *            # 모든 클래스와 상수만을 임포트 함
from tkinter import messagebox   # messagebox는 또다른 코드 모듈이기 때문에 따로 임포트 해야함. 
import pyperclip                 # 클리보드 생성기 
import json                      # json 모듈 불러오기 

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
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    
    # 유효성 검사 
    if len(website) == 0 or len(password) == 0:       # 만약 website, password가 입력되지 않았다면,
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")   # 메시지 출력
    
    # 그외 
    else:
        try:                                                             # 만약 json 파일이 있다면 
            with open("data/data.json", "r") as data_file:               # "Read"모드로 json 파일에 읽기
                # Reading old data
                data = json.load(data_file)                              # json 데이터 읽기 -> 위에 with문에 "read" 모드인 "r"지정 
        except FileNotFoundError:                                        # 만약 json 파일이 없다면, - 예외 처리 부분 
            with open("data/daya.json", "w") as data_file:               # json 데이터 생성 
                json.dump(new_data, data_file, indent=4)
        else:                                                            # 위 코드블록이 모두 실행되면 
            # Update old data
            data.update(new_data)                                        # 새로운 데이터로 업데이트 
            
            with open("data/data.json", "w") as data_file:               # "Write"모드로 json 파일에 읽기
                # Saving update data
                json.dump(data, data_file, indent=4)                     # json 데이터 쓰기 -> json.dump - new_data 형식으로, 지정한 json 데이터 파일 쓰기, 4칸씩 들여쓰기 옵션으로
        finally:    
            website_input.delete(0, END)                             # 파일 저장 후 이전에 입력한 website 명을 삭제 
            password_input.delete(0, END)                            # 파일 저장 후 이전에 입력한 password 삭제 
            
# ---------------------------- FIND PASSWORD ------------------------------- #
# 저장된 Password 정보 검색 기능 함수 
def find_password():
    website = website_input.get()                                           # 저장된 website 명 입력 후 변수에 저장 
    try:                                                                    # 만약 json 데이터가 있다면 
        with open("data/data.json") as data_file:                           # json 데이터 불러오기 
            data = json.load(data_file)                                          
    except FileNotFoundError:                                               # 예외 처리 - 파일를 찾을 수 없다라는 에러가 발생하면  
        messagebox.showinfo(title="Error", message="No Data File Found.")   # 에러 메시지 출력 
    else:                                                                   # 위 코드 블록이 모두 실행되었다면 실행
        if website in data:                                                 # 데이터 안에 입력한 웹사이트 정보가 있다면 
            email = data[website]["email"]                                  # 이메일 변수에 저장 
            password = data[website]["password"]                            # 비밀번호 변수에 저장 
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")  # 이메일, 비밀번호 팝업창에 출력 
        else:                                                                               # 만약 입력된 웹사이트 정보가 없다면 
            messagebox.showinfo(title="Error", message=f"No detail for {website} exists.")  # 정보가 없다는 에러 메시지 출력

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
website_input = Entry(width=21)                       # input 1 설정 
website_input.grid(row=1, column=1)                   # input 1 명시
website_input.focus()                                 # 시작시 webside input box에 커서 자동 생성

userid_input = Entry(width=36)                           # input 2 설정 
userid_input.grid(row=2, column=1, columnspan=2)         # input 2 설정 
userid_input.insert(0, "kisung.kim@a1mediagroup.co.kr")  # 시작시 user_id를 미리 채워넣기


password_input = Entry(width=21)                      # input 3 설정 
password_input.grid(row=3, column=1)                  # input 3 설정 

# buttons
search_button = Button(width=11, text="Search", command=find_password)       # website 검색을 위한 Search 버튼 추가 
search_button.grid(row=1, column=2)                                          # Search 버튼 위치 설정 
generate_button = Button(width=11, text="Generate Password", command=generate_password)   # button 1 설정 
generate_button.grid(row=3, column=2)                          # button 2 명시  

add_button = Button(width=34, text="Add", command=save)        # button 2 설정 - Add 버튼 클릭시 save 함수 동작
add_button.grid(row=4, column=1, columnspan=2)                 # button 2 명시 

# 닫기 버튼을 누르기 전까지 계속 구동
window.mainloop()