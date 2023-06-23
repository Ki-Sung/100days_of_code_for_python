# 모듈 볼러오기 - tkinter
import tkinter

# 윈도우 만들기 
window = tkinter.Tk()   # 객체 선언 

window.title("My First GUI Program")   # window 타이틀 지정
window.minsize(width=500, height=300)  # 실행시 기본사이즈 설정

# Label - text, font(폰트명, 크기, 굴기설정 등)설정 가능
my_label = tkinter.Label(text="I am Label!!", font=("Arial", 24, "bold"))

# 컴포넌트(my_label)가 스크린에 보여지기 위해 명시하기 (꼭 해야 window에 출력됨)
my_label.pack()                     # 지정하지 않으면 맨위 중앙에 명시 
# my_label.pack(side="left")        # 지정한 label 왼쪽으로 명시 
# my_label.pack(side="bottom")      # 지정한 label 맨 아래로 명시 
# my_label.pack(expand=True)        # window 기준 정중에 명시 


window.mainloop()       # tkinter 스크린이 유지되도록 설정 