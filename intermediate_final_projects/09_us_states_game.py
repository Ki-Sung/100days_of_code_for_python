# 모듈 불러오기 
import turtle

# turtle screen 설정 
screen = turtle.Screen()            # turtle screen 객체 선언 
screen.title("U.S. States Game")    # turtle title 설정 

# U.S 지도 삽입 
image = "us_state_game_options/blank_states_img.gif"  # 지도 이미지 파일 경로 
screen.addshape(image)               # 파일 경로에 있는 이미지 불러와서 이미지 추가 
turtle.shape(image)                  # turtle 모양 설정 

# turtle screen 내 pormpt 입력창 생성 
answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
print(answer_state)


## screen x, y 좌표를 설정하기 위한 함수 설정 
# def get_mouse_click_coor(x, y):                 # 두 개의 입력값 x, y를 갖는다.
#     print(x, y)                                 # x, y 값을 출력한다. 
    
# turtle.onscreenclick(get_mouse_click_coor)      # 클릭 위치의 x, y 좌표 전달 
# turtle.mainloop()                               # turtle screen이 계속 열려있도록 해주는 설정 

