from flask import Flask, render_template
from form import LoginForm

# 플라스크 실행을 위해 객체 선언
app = Flask(__name__)
# CSRF 보호 기능을 위한 토큰울 위한 비밀키 생성 
app.secret_key = "secret"

# main 화면 체계 
@app.route("/")
def home():
    return render_template('index.html')      # index.html을 랜더링 함 

# login 화면 체계 
@app.route("/login")
def login():
    login_form = LoginForm()                  # 로그인 정합성 검사를 위한 LoginForm 클래스 선언 
    return render_template('login.html', form=login_form)   # login.html을 랜더링

# 앱 실행 
if __name__ == '__main__':
    app.run(debug=True)