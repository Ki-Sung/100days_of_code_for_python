from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

## Flask 객체 선언
app = Flask(__name__)

## 데이터 베이스 연결 
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

## SQLAlchemy ORM을 사용하여 User 테이블 구성
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)                # id는 정수형(Integer)의 기본 키(primary key) 컬럼, 각 유저는 고유한 ID를 가지고 있으며, 이 열은 테이블에서 기본 키로 사용
    email = db.Column(db.String(100), unique=True)              # email은 문자열(String) 형식의 최대 길이가 100인 컬럼, 각 이메일 이름은 고유한 값을 가짐
    password = db.Column(db.String(100))                        # password는 문자열(String) 형식의 최대 길이가 100인 컬럼
    name = db.Column(db.String(1000))                           # name은 문자열(String) 형식의 최대 길이가 1000인 컬럼
#Line below only required once, when creating DB. 
# db.create_all()

## 모든 라우터 정의 
# home page - URL 체계: http://127.0.0.1:5000/
@app.route('/')
def home():
    # 지정한 url 체계로 index.html 템플릿 랜더링
    return render_template("index.html")

# 새로운 유저 등록 - URL 체계: http://127.0.0.1:5000/register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':                            # 요청 방식이 POST일 경우 
        hash_and_salted_password = generate_password_hash(  # 해시와 솔트 방식으로 비밀번호 암호화 설정 
            request.form.get('password'),                       # "password"의 키 값을 가져와 "new_user"의 "password" 필드에 설정
            method='pbkdf2:sha256',                             # 단방향 해시 함수의 다이제스트 방식 설정 
            salt_length=8                                       # 솔트 길이 8로 설정
        )
        new_user = User(                                    # User 모델을 이용하여 새로운 유저 데이터 생성 
            email=request.form.get('email'),                    # "email"의 키 값을 가져와 "new_user"의 "email" 필드에 설정
            name=request.form.get('name'),                      # "name"의 키 값을 가져와 "new_user"의 "name" 필드에 설정 
            password=hash_and_salted_password                   # 해시와 솔트 방식으로 저장한 password로 필드 설정 
        )
        
        db.session.add(new_user)                            # SQLAlchemy의 세션에 새로운 유저 데이터 추가
        db.session.commit()                                 # 변동 사항 DB에 커밋
        
        # 등록 완료후 secrets 함수로 리다이렉션
        return redirect(url_for('secrets'))
    
    # 지정한 url 체계로 register.html 템플릿 랜더링   
    return render_template("register.html")

# 로그인 - URL 체계: http://127.0.0.1:5000/login 
@app.route('/login')
def login():
    # 지정한 url 체계로 login.html 템플릿 랜더링
    return render_template("login.html")

# 시크릿 페이지 - URL 체계: http://127.0.0.1:5000/secrets 
@app.route('/secrets')
def secrets():
    # 지정한 url 체계로 secrets.html 템플릿 랜더링
    return render_template("secrets.html")

# 로그아웃 - URL 체계: http://127.0.0.1:5000/logout 
@app.route('/logout')
def logout():
    pass

# 다운로드 - URL 체게: http://127.0.0.1:5000/download 
@app.route('/download')
def download():
    # 지정된 디렉토리로 PDF 파일 생성 
    return send_from_directory('static', filename="files/cheat_sheet.pdf")

if __name__ == "__main__":
    app.run(debug=True)
