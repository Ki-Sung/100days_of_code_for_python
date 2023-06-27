# Make Mile to Km Converter

# 모듈 볼러오기 
from tkinter import *

# Mile 단위에서 Km단위로 변환 기능이 있는 함수 
def miles_to_km():
    miles = float(miles_input.get())         # 입력된 miles 실수형태로 저장 
    km = round(miles * 1.609)                # 실수의 miles를 km 계산법으로 계산(소수점 없애기)
    km_result_label.config(text=f'{km}')     # 계산된 km을 km_result_label에 명시 (버튼 클릭시)

# 윈도우 만들기 
window = Tk() 

# 기본설정 
window.title("Mile to Km Converter")       # 타이틀 지정 
window.config(padx=20, pady=20)            # pad 추가 

# input
miles_input = Entry(width=7)               # 입력창 설정 
miles_input.grid(column=1, row=0)          # 입력창 위치 설정 

# label 1 - miles label
miles_label = Label(text="Miles",  font=("Arial", 16, "bold"))       # miles_label 설정 
miles_label.grid(column=2, row=0)                                    # miles_label 위치 설정 

# label 2 - equal_label
equal_label = Label(text="is equal",  font=("Arial", 16, "bold"))    # equal_label 설정 
equal_label.grid(column=0, row=1)                                    # equal_label 위치 설정 

# label 3 - km_result_label
km_result_label = Label(text="Km",  font=("Arial", 16, "bold"))      # km_result_label 설정
km_result_label.grid(column=1, row=1)                                # km_result_label 위치 설정 

# label 4 - km_label
km_label = Label(text="Km",  font=("Arial", 16, "bold"))             # km_label 설정
km_label.grid(column=2, row=1)                                       # km_label 위치 설정 

# button 
calculate_button = Button(text="Calculate", command=miles_to_km)     # button 및 botton 클릭시 이벤트 설정 
calculate_button.grid(column=1, row=2)                               # button 위치 설정 

window.mainloop()                                                    # tkinter 스크린이 유지되도록 설정 