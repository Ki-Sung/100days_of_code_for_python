from datetime import date
from flask import Flask, render_template, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField

## --- 웹 서버 정의 ---
app = Flask(__name__)                                           # flask 객체 선언 
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'   # 애플리케이션 비밀키 설정 - 비밀 키는 세션 및 CSRF(Cross-Site Request Forgery) 보호 및 Flask 기능을 보호하는데 사용
ckeditor = CKEditor(app)                                        # 블로그 포스트 에디터인 CKEditor 객체 선언
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
    posts = BlogPost.query.order_by(BlogPost.date.desc()).all()                     # DB에 있는 모든 블로그 게시물을 날짜 기준으로 내림차순으로 조회
    return render_template("index.html", all_posts=posts)                           # 조회된 모든 블로그 게시물 index.html 템플릿 렌더링 

# 2. index 기준으로 게시된 블로그 글 조회 page - url 체계: http://127.0.0.1:5000/post/<index> -> CRUD 중 READ
@app.route("/post/<int:index>")
def show_post(index):
    requested_post = BlogPost.query.get(index)                                      # index 기준 특정 게시물 조회 
    return render_template("post.html", post=requested_post)                        # 요청된 게시물과 같이 post.html 템필릿 렌더링

# 3. 새로운 게시글 추가 page - url 체계: http://127.0.0.1:5000/new-post -> CRUD 중 CREATE
@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    form = CreatePostForm()                                                         # WTForm 양식 초기화 
    if form.validate_on_submit():                                                   # 만약 WTForm 양식이 제출되었다면
        new_post = BlogPost(                                                        # BlogPost 객체를 생성, 생성과 동시에 post 페이지에 기록한 데이터들 받기
            title = form.title.data,                                                    # 게시글 제목 
            subtitle = form.subtitle.data,                                              # 게시글 부제목
            body = form.body.data,                                                      # 게시글 본문 
            author = form.author.data,                                                  # 게시자 
            img_url = form.img_url.data,                                                # 블로그에 사용할 Img_URL
            date = date.today().strftime("%B %d, %Y")                                   # 게시 날짜 
        )
        
        db.session.add(new_post)                                                    # 이력한 내용들 DB에 추가 
        db.session.commit()                                                         # DB 변경사항 커밋 
        
        return redirect(url_for("get_all_posts"))                                   # 새 게시물을 성공적으로 추가한 후 get_all_posts(home에 있는 게시글 목록) 함수를 트리거하여 root URL로 리다이렉션
    
    return render_template("make-post.html", form=form)                             # 만약 양식이 제출되지 않거나 유효성 검사를 통과 못했을 경우 make-post.html 템플릿을 생성하기 위한 양식으로 렌더링

# 4. 기존 게시글 수정 page - url 체계: http://127.0.0.1:5000/edit-post/<post_id> -> CRUD 중 UPDATE
@app.route("/edit-post/<int:index>", methods=["GET", "POST"])
def edit_post(index):
    # 수정할 게시글 불러오기 부분
    post = BlogPost.query.get(index)                                                # index 기준 수정할 특정 게시물 조회 
    edit_form = CreatePostForm(                                                     # index 기준 수정할 특정 게시물 게시글 수정을 위해 WTForm에 필드 자동으로 채우기 
        title=post.title,                                                               # 게시글 제목 
        subtitle=post.subtitle,                                                         # 게시글 부제목 
        img_url=post.img_url,                                                           # 블로그에 사용할 Img_URL
        author=post.author,                                                             # 게시자 
        body=post.body                                                                  # 게시글 본문
    )
    
    # 게시글 수정 데이터 대입 부분
    if edit_form.validate_on_submit():                                              # 만약 WTForm 양식(edit_form)이 제출되었다면
        post.title = edit_form.title.data                                               # 수정할 게시글 제목 
        post.subtitle = edit_form.subtitle.data                                         # 수정할 게시글 부제목
        post.img_url = edit_form.img_url.data                                           # 수정할 Img_URL
        post.author = edit_form.author.data                                             # 수정할 게시자 
        post.body = edit_form.body.data                                                 # 수정할 게시글 
        
        db.session.commit()                                                         # 수정완료 후 DB 변경사항 커밋  
        return redirect(url_for("show_post", index=post.id))                      # 수정한 해당 게시글로 리다이렉션
    
    return render_template("make-post.html", form=edit_form, is_edit=True)          # make-post.html 템플릿을 생성하기 위한 양식으로 렌더링, form은 edit_form 지정, edit 허용

# 5. 게시글 삭제 - url 체계: http://127.0.0.1:5000/delete/<post_id> -> CRUD 중 DELTE
@app.route("/delete/<int:index>")
def delete_post(index):
    post = BlogPost.query.get(index)                                                  # 해당 게시글 찾기
    db.session.delete(post)                                                           # 해당 게시글 삭제
    db.session.commit()                                                               # 삭제 후 변경사항 커밋
    return redirect(url_for('get_all_posts'))                                         # 삭제 완료 후 Home으로 리다이렉션

# 블로그 관리자 소개 page - url 체계: http://127.0.0.1:5000/about
@app.route("/about")
def about():
    return render_template("about.html")

# 블로그 관리자 연락 page - url 체계: http://127.0.0.1:5000/contact
@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)