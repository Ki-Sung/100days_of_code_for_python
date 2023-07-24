# REST API를 이용하여 킨예 명언 제조기 만들기 

# 모듈 불러오기 
from tkinter import *   # Tkinter 모듈 
import requests         # requests 모듈 

# API에서 명언을 얻기 위한 get_quote 함수 선언 
def get_quote():
    response = requests.get(url="https://api.kanye.rest/")     # 앤드포인트로 요청 받기 
    response.raise_for_status()                                # 200이 아니면 예외 발생 시킴 
    
    data = response.json()                                     # JSON 형식으로 데이터 응답 받기 
    quote = data["quote"]                                      # 응답 받은 데이터 중 명언만 추출 
    canvas.itemconfig(quote_text, text=quote)                  # canvas 항목 동적으로 구성 - quote_text에서 text를 API로 응답 받은 명언으로 추출 

# UI 부분 
window = Tk()                                                  # tkinter 객체 선언 
window.title("Kanye Says...")                                  # tkinter title 지정
window.config(padx=50, pady=50)                                # pad(간격) 설정 

# Canvas 사용 
canvas = Canvas(width=300, height=414)                         # canvas 객체 선언 - 선언시 크기 설정
background_img = PhotoImage(file="./img/background.png")       # 배경 이미지 불러오기 
canvas.create_image(150, 207, image=background_img)            # 이미지 명시하기 
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes Here!", width=250, font=("Arial", 30, "bold"), fill="white") # 이미지 위에 들어갈 Text 설정 
canvas.grid(row=0, column=0)                                   # 설정한 canvas 명시 

# 버튼 설정 
kanye_img = PhotoImage(file="./img/kanye.png")                 # 버튼에 사용할 이미지 불러오기 
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)   # 이미지에 버튼 설정 (버튼을 누르면, 랜덤하게 명언 생성)
kanye_button.grid(row=1, column=0)                             # 버튼 명시


# 닫기 버튼 누르기 전까지 계속 구동
window.mainloop()