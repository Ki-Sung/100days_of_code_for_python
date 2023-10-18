# 플라스크로 서버 구축
import random
from flask import Flask

# 플라스크 객체 생성 (__name__은 현재 실행 중인 모듈 이름을 전달)
app = Flask(__name__)

# 타겟 넘버 랜덤으로 생성
target_number = random.randint(0, 20)
print(target_number)

# main 페이지 - html 랜더링
@app.route('/')              # 기본 주소 체계 
def home():        # 위의 주소로 호출 시 웹에 보여지는 html
    html = '<h1>Guess a number between 0 and 20</h1>'\
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'
    return html

# URL에 컨버터 기능 추가 
@app.route("/<int:number>")            # 기본 주소 체계(컨버터 기능 사용)
def guess_number(number):             # 위의 주소로 호출 시 웹에 보여지는 html
    if number < target_number:         # 만약 입력한 숫자가 타겟 숫자보다 적으면 아래 html 반환
        html = '<h1 style="color:red">Too low, Try again!</h1>'\
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
        return html 
    
    elif number > target_number:        # 만약 입력한 숫자가 타겟 숫자보다 크면 아래 html 반환
        html = '<h1 style="color:purple">Too Hight, Try again!</h1>'\
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
        return html 
    
    else:                               # 만약 입력한 숫자와 타겟 숫자가 같으면
        html = '<h1 style="color:green">Congratulations! You founde me!</h1>'\
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
        return html

# 만약 실행하고자 하는 모듈 이름과 같다면 플라스크 실행
if __name__ == '__main__':
    app.run(debug=True)       # 실행시 디버그 모드 활성화