from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm, RegisterForm
from flask_gravatar import Gravatar

## --- 웹 서버 정의 --
app = Flask(__name__)                                           # flaks 객체 선언 
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'   # 애플리케이션 비밀키 설정 - 비밀 키는 세션 및 CSRF(Cross-Site Request Forgery) 보호 및 Flask 기능을 보호하는데 사용
ckeditor = CKEditor(app)                                        # 블로그 포스트 에디터인 CKEditor 객체 선언
Bootstrap(app)                                                  # flask 웹의 Bootstrap 초기화 

## --- DB 연결 ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'     # SQLALCHEMY DB URL 설정 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False            # SQLALCHEMY의 트랙 수정 -> 추가적인 메모리를 필요로 하므로 False를 지정하여 끔
db = SQLAlchemy(app)                                            # SQLALCHEMY 객체 선언

## --- SQLAlchemy ORM을 사용하여 BlogPost 테이블 구성 ---
class BlogPost(db.Model):
    __tablename__ = "blog_posts"                                        # 테이블 명 지정 - blog_posts
    id = db.Column(db.Integer, primary_key=True)                        # id(정수형(Integer)의 기본 키(primary key) 컬럼), 테이블에서 기본 키로 사용
    author = db.Column(db.String(250), nullable=False)                  # 블로그 글쓴이(최대 길이 250인 string), not null 설정
    title = db.Column(db.String(250), unique=True, nullable=False)      # 블로그 제목(최대 길이 250인 string), 고유값 설정, not null 설정 
    subtitle = db.Column(db.String(250), nullable=False)                # 블로그 부제목(최대 길이 250인 string), not null 설정 
    date = db.Column(db.String(250), nullable=False)                    # 블로그 게시날짜(최대 길이 250인 string), not null 설정
    body = db.Column(db.Text, nullable=False)                           # 블로그 본문(Text), not null 설정
    img_url = db.Column(db.String(250), nullable=False)                 # 블로그 이미지 URL(최대 길이 250인 string), not null 설정

## --- SQLAlchemy ORM을 사용하여 User 테이블 구성 ---
class User(UserMixin, db.Model):                                        # 상속되는 UserMixin는 상요자 인증을 위해 Flask-Login으로 작업할 때 사용됨
    __tablename__ = "users"                                             # 테이블 병 지정 - users
    id = db.Column(db.Integer, primary_key=True)                        # id(정수형(Integer)의 기본 키(primary key) 컬럼), 테이블에서 기본 키로 사용
    email = db.Column(db.String(100), unique=True)                      # 유저 ID 인 email(최대 길이 100인 string), 고유값 설정
    password = db.Column(db.String(100))                                # 비밀번호(최대 길이 100인 string)
    name = db.Column(db.String(100))                                    # 유저 이름(최대 길이 100인 string)
    
# DB에 있는 모든 테이블 생성
db.create_all()

## --- 모든 라우터 정의 ---
# 1. home 페이지 - URL 체계: http://127.0.0.1:5000/
@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()                                        # blog DB 내 blog_posts 테이블에 있는 모든 블로그 정보 조회
    return render_template("index.html", all_posts=posts)               # 조회된 모든 블로그 게시물 index.html 템플릿 렌더링

# 2. 유저 등록 페이지 - URL 체계: http://127.0.0.1:5000/register
@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()                                               # WTForm 양식 RegisterForm으로 초기화 
    if form.validate_on_submit():                                       # 만약 WTForm 양식이 제출되었다면
        
        hash_and_salted_password = generate_password_hash(                  # 해시와 솔트 방식으로 비밀번호 암호화 설정 
            form.password.data,                                             # WTForm의 paaword 필드에 입력한 값에 액세스
            method='pbkdf2:sha256',                                         # 단방향 해시 함수의 다이제스트 방식 설정 
            salt_length=8                                                   # 솔트 길이 8로 설정 
        )
        new_user = User(                                                # User 모델을 이용하여 새로운 유저 데이터 생성 
            email=form.email.data,                                          # WTForm의 email 필드에 입력한 값에 액세스 (입력한 값 저장)
            name=form.name.data,                                            # WTForm의 name 필드에 입력한 값에 액세스 (입력한 값 저장)
            password=hash_and_salted_password,                              # WTForm의 password 필드에 입력한 값을 해시 솔트로 암호화한 비밀번호로 바꿔서 저장
        )
        db.session.add(new_user)                                        # SQLAlchemy의 세션에 새로운 유저 데이터 추가
        db.session.commit()                                             # 변동 사항 DB에 커밋 
        
        return redirect(url_for("get_all_posts"))                       # 등록 완료 후 get_all_posts 함수(home)로 리디렉션
        
    return render_template("register.html", form=form)                  # 지정한 url 체계로 register.html 템플릿 랜더링 


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/logout')
def logout():
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post")
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>")
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(debug=True)
