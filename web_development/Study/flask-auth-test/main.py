from flask import Flask, render_template, request, url_for, redirect, flash, send_file
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

## Flask Login 설정 
login_manager = LoginManager()                                  # Flask-Login 설정 
login_manager.init_app(app)                                     # 설전된 Login을 Flask App과 연결

# Flask-Login에 대한 사용자 로더 기능 정의 - 사용자 ID를 기준으로 DB에서 사용자 로드
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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
    return render_template("index.html", logged_in=current_user.is_authenticated)   # 지정한 url 체계로 index.html 템플릿 랜더링 - 객체속성 추가: 사용자가 인증 결과 반환 (인증: True, 인증 X: False)

# 새로운 유저 등록 - URL 체계: http://127.0.0.1:5000/register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':                                                # 요청 방식이 POST일 경우 
        
        if User.query.filter_by(email=request.form.get('email')).first():           # 이미 존재하는 이메일 주소인지 확인
            flash("You've already signed up with that email, log in instead!")      # 이미 이메일 주소가 존재할 경우 에러 메시지 화면에 출력 
            return redirect(url_for('login'))                                       # 로그인 페이지로 리디렉션
        
        hash_and_salted_password = generate_password_hash(              # 해시와 솔트 방식으로 비밀번호 암호화 설정 
            request.form.get('password'),                                   # "password"의 키 값을 가져와 "new_user"의 "password" 필드에 설정
            method='pbkdf2:sha256',                                         # 단방향 해시 함수의 다이제스트 방식 설정 
            salt_length=8                                                   # 솔트 길이 8로 설정
        )
        
        new_user = User(                                    # User 모델을 이용하여 새로운 유저 데이터 생성 
            email=request.form.get('email'),                    # "email"의 키 값을 가져와 "new_user"의 "email" 필드에 설정
            name=request.form.get('name'),                      # "name"의 키 값을 가져와 "new_user"의 "name" 필드에 설정 
            password=hash_and_salted_password                   # 해시와 솔트 방식으로 저장한 password로 필드 설정 
        )
        
        db.session.add(new_user)                            # SQLAlchemy의 세션에 새로운 유저 데이터 추가
        db.session.commit()                                 # 변동 사항 DB에 커밋
        
        login_user(new_user)                                # 등록된 새로운 유저 로그인 
        
        return redirect(url_for('secrets'))                 # 등록 완료후 secrets 함수로 리디렉션
    
    return render_template("register.html", logged_in=current_user.is_authenticated)       # 지정한 url 체계로 register.html 템플릿 랜더링 - 객체속성 추가: 사용자가 인증 결과 반환

# 로그인 - URL 체계: http://127.0.0.1:5000/login 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":                                     # 요청 방식이 POST일 경우 
        email = request.form.get('email')                            # 'email' 값 가져오기 
        password = request.form.get('password')                      # 'password' 값 가져오기

        user = User.query.filter_by(email=email).first()             # 유저 데이터 가져오기 

        # 사용자 데이터가 존재하는지, 비밀번호가 일치하는지 확인
        if not user:                                                # 만약 유저 데이터가 존재하지 않는 경우 
            flash('That email does not exist, please try again.')   # 에러 메시지 출력 
            return redirect(url_for('login'))                       # 로그인 페이지로 리디렉션
        
        elif not check_password_hash(user.password, password):       # 입력한 비밀번호와 해시+솔트 방식으로 저장된 비밀번호가 일치하지 않을 경우
            flash('Password incorrect, please try again.')           # 에러 메시지 출력
            return redirect(url_for('login'))                        # 로그인 페이지로 리디렉션
        
        # 만약 등록된 유저 데이터가 일치할 경우 
        else:
            login_user(user)                                         # 유저 로그인  
            return redirect(url_for('secrets'))                      # secrets 페이지로 리디렉션
        
    return render_template("login.html", logged_in=current_user.is_authenticated)        # 지정된 URL 체계로 login.html 템플릿을 렌더링합니다. - 객체속성 추가: 사용자가 인증 결과 반환

# 시크릿 페이지 - URL 체계: http://127.0.0.1:5000/secrets 
@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)                                         # 로그인 된 사용자 콘솔에 출력
    return render_template("secrets.html", name=current_user.name, logged_in=True)   # 지정한 url 체계로 secrets.html 템플릿 랜더링 

# 로그아웃 - URL 체계: http://127.0.0.1:5000/logout 
@app.route('/logout')
def logout():
    logout_user()                                                   # logout_user() 함수가 호출되어 현재 사용자를 로그아웃
    return redirect(url_for('home'))                                # 로그아웃 후 메인 페이지로 리디렉션 

# 파일 다운로드 - URL 체게: http://127.0.0.1:5000/download 
@app.route('/download')
def download():
    file_path = "static/files/cheat_sheet.pdf"                      # 다운로드할 파일 경로 지정 
    return send_file(file_path, as_attachment=True)                 # 지정된 디렉토리로 PDF 파일 접근 후 생성, 사용자에게 파일을 다운로드하려는 메시지를 표시 

if __name__ == "__main__":
    app.run(debug=True)
