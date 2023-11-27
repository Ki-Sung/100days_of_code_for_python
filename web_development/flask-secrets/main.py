from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from form import LoginForm

# 플라스크 실행을 위해 객체 선언
app = Flask(__name__)

# 플라스크 부트스트랩 대입 
Bootstrap(app)

# CSRF 보호 기능을 위한 토큰울 위한 비밀키 생성 
app.secret_key = "secret"

# main 화면 체계 
@app.route("/")
def home():
    return render_template('index.html')      # index.html을 랜더링 함 

# login 화면 체계 
@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()                  # 로그인 정합성 검사를 위한 LoginForm 클래스 선언 
    if login_form.validate_on_submit():           # POST 메소드 요청에 응답후 데이터를 유효성 검사로 검증
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":  # 로그인 test를 위해 임시 아이디, 비밀번호 설정 만약 입력한 정보가 일치하면
            return render_template('success.html')                                                 # succes.html을 랜딩
        else:                                                                                      # 로그인이 실패하면 
            return render_template('denied.html')                                                  # denined.html을 랜딩
    return render_template('login.html', form=login_form)                                          # login.html을 랜더링

# 앱 실행 
if __name__ == '__main__':
    app.run(debug=True)