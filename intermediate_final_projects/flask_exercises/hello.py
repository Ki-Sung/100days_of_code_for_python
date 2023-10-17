# 플라스크로 서버 구축
from flask import Flask
app = Flask(__name__)

# main 페이지 - html 랜더링
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'\
           '<p>This is a paragraph</p>'\
            '<img src="https://media.giphy.com/media/gyRWkLSQVqlPi/giphy.gif" width=400>'
            

# bye 페이지 
@app.route("/bye")
def say_bye():
    return 'Bye'

# username 페이지 - URL에 변수 섹션 추가
# @app.route("/username/<name>")
# def greet1(name):
#     return f"Hello, My name is {name}"

# username 페이지 - URL에 컨버터 기능 추가 1
# @app.route("/username/<path:name>/")
# def greet1(name):
#     return f"Hello, My name is {name}"

# username 페이지 - URL에 컨버터 기능 추가 2 
@app.route("/username/<name>/<int:number>")
def greet1(name, number):
    return f"Hello, My name is {name}, you are {number} years old"

if __name__ == '__main__':
    app.run(debug=True)       # 실행시 디버그 모드 활성화