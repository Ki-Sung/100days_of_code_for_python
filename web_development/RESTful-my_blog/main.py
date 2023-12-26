from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField

## --- 웹 서버 정의 ---
app = Flask(__name__)                                           # flask 객체 선언 
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'   # 애플리케이션 비밀키 설정 - 비밀 키는 세션 및 CSRF(Cross-Site Request Forgery) 보호 및 Flask 기능을 보호하는데 사용
ckeditor = CKEditor(app)                                        # 블로그 포스티 에디터인 CKEditor 객체 선언
Bootstrap(app)                                                  # flask 웹의 Bootstrap 초기화

## --- DB 연결 ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

## --- SQLAlchemy ORM을 사용하여 Cafe 테이블 구성 ---
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)                        # id는 정수형(Integer)의 기본 키(primary key) 컬럼, 각 카페는 고유한 ID를 가지고 있으며, 이 열은 테이블에서 기본 키로 사용
    title = db.Column(db.String(250), unique=True, nullable=False)      # title은 문자열(String) 형식의 최대 길이가 250인 컬럼, 각 블로그 제목은 고유한 값을 가져야하며, not null 설정
    subtitle = db.Column(db.String(250), nullable=False)                # subtitle은 문자열(String) 형식의 최대 길이가 250인 컬럼, 각 블로그의 부제목을 의미하며, not null 설정
    date = db.Column(db.String(250), nullable=False)                    # date는 문자열(String) 형식의 최대 길이가 250인 컬럼, 블로그 게시 날짜를 의미하며, not null 설정
    body = db.Column(db.Text, nullable=False)                           # bodt는 text 형식, not null 설정, 게시할 블로그 글을 의미하며, not null 설정 
    author = db.Column(db.String(250), nullable=False)                  # author는 문자열(String) 형식의 최대 길이가 250인 컬럼, 블로그 게시자를 의미하며, not null 설정 
    img_url = db.Column(db.String(250), nullable=False)                 # img_url는 문자열(String) 형식의 최대 길이가 250인 컬럼, 블로그 게시글 이미지 url를 의미하며, not null 설정

## --- New Post를 위한 WTForm 및 CKEditor 정의 클래스 정의 ---
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])             # 블로그 제목 텍스트 입력 필드 - 값이 비어있는지 유효성 검사
    subtitle = StringField("Subtitle", validators=[DataRequired()])                 # 블로그 부제목 텍스트 입력 필드 - 값이 비어있는지 유효성 검사
    author = StringField("Your Name", validators=[DataRequired()])                  # 블로그 글쓴이 텍스트 입력 필드 - 값이 비어있는지 유효성 검사
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])     # 블로그 이미지 URL 텍스트 입력 필드 - 값이 비어있는지 유효성 검사
    body = CKEditorField("Blog Content", validators=[DataRequired()])               # 블로그 게시글 텍스트 입력 필드 - CKEditorField 사용, 유효성 검사 
    submit = SubmitField("Submit Post")                                             # 제출 버튼
    
## --- 모든 라우터 정의 ---
# 1. home page - url 체계: http://127.0.0.1:5000/
@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)

# 2. index 기준으로 게시된 블로그 글 조회 page - http://127.0.0.1:5000/post/<index>
@app.route("/post/<int:index>")
def show_post(index):
    requested_post = BlogPost.query.get(index)
    return render_template("post.html", post=requested_post)

# 3. 새로운 게시글 추가 page - http://127.0.0.1:5000/new-post
@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    form = CreatePostForm() 
    return render_template("make-post.html", form=form)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)