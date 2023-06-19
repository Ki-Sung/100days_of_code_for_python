# 모듈 불러오기 
import turtle                           # turtle 불러오기 
import pandas as pd                     # pandas 불러오기 

# turtle screen 설정 
screen = turtle.Screen()                # turtle screen 객체 선언 
screen.title("U.S. States Game")        # turtle title 설정 

# U.S 지도 삽입 
image = "us_state_game_options/blank_states_img.gif"  # 지도 이미지 파일 경로 
screen.addshape(image)                  # 파일 경로에 있는 이미지 불러와서 이미지 추가 
turtle.shape(image)                     # turtle 모양 설정 

# 데이터 불러오기
data_path = "./us_state_game_options/50_states.csv"  # 데이터 Path 지정 
data = pd.read_csv(data_path)           # 불러온 데이터 데이터프레임으로 저장 
all_states = data['state'].to_list()    # 데이터프레임 'state' 컬럼에 있는 row 데이터 list로 저장
guessed_states = []                     # 정답을 맞춘 데이터 리스트에 넣기 위해 빈 리스트 선언 

# turtle screen 내 pormpt 입력창 생성 
while len(guessed_states) < 50:             # 50개주 모두 맞추기 전까지 반복문 계속 돌아가기 
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Sates Correct", 
                                    prompt="What's another state's name?").title()   # 입려창 설정

    # hidden key 설정 - list comprehension으로 변환 
    if answer_state == 'Exit': 
        missig_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missig_states)
        new_data.to_csv('us_state_game_options/states_to_learn.csv')
        break
    
    # if answer_state == 'Exit':                    # 만약 "Exit"를 입력하면 
    #     missig_states = []                        # "Exit"를 누르고, 맞추지 못한 states 이름을  저장하기 위해 빈 리스트 선언  
    #     for state in all_states:                  # 반복문 사용 - all_states에 있는 데이터 state로 하나씩 저장
    #         if state not in guessed_states:       # 만약 state가 guessed_states에 있지 않으면,
    #             missig_states.append(state)       # missing_states 빈 리스트에 저장 
    #     new_data = pd.DataFrame(missig_states)    # 저장된 missing_states를 데이터프레임으로 저장
    #     new_data.to_csv('us_state_game_options/states_to_learn.csv')   # 저장된 데이터 csv로 저장 
    #     break                                     # 게임종료 
    
    # answer_state는 입력 값이 50_states.csv에 있는 주인지 확인하기 
    if answer_state in all_states:                # 만약 answer_state 데이터가 all_states 안에 있다면,
        guessed_states.append(answer_state)       # guessed_states 빈 리스트로 저장 
        t = turtle.Turtle()                       # turtle 객체 선언 
        t.hideturtle()                            # turtle 숨기기 
        t.penup()                                 # turtle 선 숨기기 
        state_data = data[data['state'] == answer_state]    # answer_state 데이터에 부합되는 state_data 불러오기 
        t.goto(int(state_data['x']), int(state_data['y']))  # state_data의 x, y 값 위치로 가기 
        t.write(answer_state)                               # x, y 값에 state 이름 지정하기 

## screen x, y 좌표를 설정하기 위한 함수 설정 
# def get_mouse_click_coor(x, y):                 # 두 개의 입력값 x, y를 갖는다.
#     print(x, y)                                 # x, y 값을 출력한다. 
    
# turtle.onscreenclick(get_mouse_click_coor)      # 클릭 위치의 x, y 좌표 전달 aa
# turtle.mainloop()                               # turtle screen이 계속 열려있도록 해주는 설정 

