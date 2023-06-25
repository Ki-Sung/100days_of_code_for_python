# 모듈 볼러오기 - tkinter
#import tkinter
from tkinter import *

# 윈도우 만들기 
window = Tk()   # 객체 선언 

# 기본 설정 
window.title("My First GUI Program")   # window 타이틀 지정
window.minsize(width=500, height=300)  # 실행시 기본사이즈 설정

# Label - text, font(폰트명, 크기, 굴기설정 등)설정 가능
my_label = Label(text="I am Label!!", font=("Arial", 24, "bold"))

# 컴포넌트(my_label)가 스크린에 보여지기 위해 명시하기 (꼭 해야 window에 출력됨)
my_label.pack()                     # 지정하지 않으면 맨위 중앙에 명시 
# my_label.pack(side="left")        # 지정한 label 왼쪽으로 명시 
# my_label.pack(side="bottom")      # 지정한 label 맨 아래로 명시 
# my_label.pack(expand=True)        # window 기준 정중에 명시 

# label안에 text 바꾸기
my_label['text'] = "New Text"       # 바꿀 텍스트 입력 
my_label.config(text="New Text")    # config를 사용해 키워드 인수로 text를 전달 

# Button 
# button 클릭시 이벤트가 나오게 하는 함수 - 클릭시 I got clicked 콘솔창에 출력 
def button_clicked():
    print("I got clicked")              # 버튼 클릭시 콘솔창에 출력 
    new_text = input.get()              # input 창에 입력한 str 반환             
    my_label.config(text=new_text)      # 버튼 클릭시 지정한 text로 Tkinter 창에 명시

button = Button(text="click Me", command=button_clicked)   # 버튼 설정 
button.pack()                                              # 버튼 명시 

# Entry 
input = Entry(width=10)                 # 입력창 생성 (크기 설정)
input.pack()                            # 입력창 명시 

window.mainloop()       # tkinter 스크린이 유지되도록 설정 