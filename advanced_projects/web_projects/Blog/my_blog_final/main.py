from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from flask_gravatar import Gravatar
from functools import wraps

## --- 웹 서버 정의 --
app = Flask(__name__)                                           # flaks 객체 선언 
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'   # 애플리케이션 비밀키 설정 - 비밀 키는 세션 및 CSRF(Cross-Site Request Forgery) 보호 및 Flask 기능을 보호하는데 사용
ckeditor = CKEditor(app)                                        # 블로그 포스트 에디터인 CKEditor 객체 선언
Bootstrap(app)                                                  # flask 웹의 Bootstrap 초기화 

## --- DB 연결 ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'     # SQLALCHEMY DB URL 설정 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False            # SQLALCHEMY의 트랙 수정 -> 추가적인 메모리를 필요로 하므로 False를 지정하여 끔
db = SQLAlchemy(app)                                            # SQLALCHEMY 객체 선언

## --- Flask Login 설정 ---
login_manager = LoginManager()                                  # Flask-Login 설정 
login_manager.init_app(app)                                     # 설정된 Login을 Flask App과 연결

## --- 사용자 아바타를 추가하기 위한 Flask-Gravatar 설정 ---
gravatar = Gravatar(app,                                        # Gravatar 확장자를 Flask에 추가
                    size=100,                                   # Gravatar 이미지 크기 설정 (픽셀 단위)
                    rating='g',                                 # Gravatar 이미지 콘텐츠 등급 설정 (g: 모든 오디언스에게 적합 )
                    default='retro',                            # Gravatar 기본 이미지 설정 (Retro 타입)
                    force_default=False)                        # Gravatar 이미지가  지정된 이미지 강제 사용 Off 

## --- SQLAlchemy ORM을 사용하여 User 테이블 구성 ---
class User(UserMixin, db.Model):                                        # 상속되는 UserMixin는 상요자 인증을 위해 Flask-Login으로 작업할 때 사용됨
    __tablename__ = "users"                                             # 테이블 병 지정 - users
    id = db.Column(db.Integer, primary_key=True)                        # id(정수형(Integer)의 기본 키(primary key) 컬럼), 테이블에서 기본 키로 사용
    email = db.Column(db.String(100), unique=True)                      # 유저 ID 인 email(최대 길이 100인 string), 고유값 설정
    password = db.Column(db.String(100))                                # 비밀번호(최대 길이 100인 string)
    name = db.Column(db.String(100))                                    # 유저 이름(최대 길이 100인 string)
    
    # 각 사용자에게 첨부된 BlogPost 개체 목록처럼 동작, "author"는 BlogPost 클래스의 작성자 속성을 나타냄(즉, author 속성을 통해 연결하여 BlogPost 테이블과 일대다 관계 설정)
    # "author"는 BlogPost 클래스의 작성자 속성을 나타낸다.
    # 해당 코드는 "User' 클래스와 "BlogPost" 클래스 사이에 일대다 관계를 설정 -> 한 사용자가 여러 블로그 게시물을 가질 수 있지만, 각 블로그 게시물은 한명의 사용자에게만 속한다는 의미 
    # 1) 관계 대상 지정 -> "BlogPost" 클래스 
    # 2) back_populates 속성 -> 관계의 반대편(children)을 나타내는 대상 클래스의 속성을 나타냄 -> "author" 속성  
    posts = relationship("BlogPost", back_populates="author")        
    
    # comment_author 속성을 통해 연결하여 'Comment' 테이블과 일대다 관계를 설정
    # "comment_author"는 Comment 클래스의 comment_author 속성을 나타냄
    comments = relationship("Comment", back_populates="comment_author")

## --- SQLAlchemy ORM을 사용하여 BlogPost 테이블 구성 (Parent) ---
class BlogPost(db.Model):
    __tablename__ = "blog_posts"                                        # 테이블 명 지정 - blog_posts
    id = db.Column(db.Integer, primary_key=True)                        # id(정수형(Integer)의 기본 키(primary key) 컬럼), 테이블에서 기본 키로 사용
    
    # 외래키 생성, "user.id" 사용자는 사용자의 테이블 이름을 참조 - 외래키의 역할은 두 개의 테이블을 연결해주는 역할을 함 (외래키와 연결하려면 먼저 Primary Key를 생성해줘야함)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    # User 개체에 대한 참조를 만듬, "posts"은 User 클래스의 게시물 속성을 참조 
    # 해당 코드는 "BlogPost"에서 "User"로의 역관계를 설정함, 이는 각 "BlogPost"에 연결된 "author"이 있음을 나타낸다.
    # 1) 관계 대상 지정 -> "User" 클래스 
    # 2) back_populates 속성 -> 관계의 반대편(Parent)을 나타내는 대상 클래스의 속성을 나타냄 -> posts 속성
    author = relationship("User", back_populates="posts")
    
    title = db.Column(db.String(250), unique=True, nullable=False)      # 블로그 제목(최대 길이 250인 string), 고유값 설정, not null 설정 
    subtitle = db.Column(db.String(250), nullable=False)                # 블로그 부제목(최대 길이 250인 string), not null 설정 
    date = db.Column(db.String(250), nullable=False)                    # 블로그 게시날짜(최대 길이 250인 string), not null 설정
    body = db.Column(db.Text, nullable=False)                           # 블로그 본문(Text), not null 설정
    img_url = db.Column(db.String(250), nullable=False)                 # 블로그 이미지 URL(최대 길이 250인 string), not null 설정
    
    # Parent Relation
    comments = relationship("Comment", back_populates="parent_post")    # Comment 개체에 대한 참조를 만듬, "parent_post"은 Comment 클래스의 게시물 속성을 참조 

## --- SQLAlchemy ORM을 사용하여 Comment 테이블 구성 (Children) ---
class Comment(db.Model):
    __tablename__ = "comments"                                          # 테이블 명 지정 - comments
    id = db.Column(db.Integer, primary_key=True)                        # id(정수형(Integer)의 기본 키(primary key) 컬럼), 테이블에서 기본 키로 사용
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))        # "users.id" 사용자는 Users 클래스의 테이블 이름을 참조 -> id열을 참조하는 왜래키     
    comment_author = relationship("User", back_populates="comments")    # "comments"는 User 클래스의 comments 속성을 나타냄 -> comments 속성을 통해 연결하여 "User" 테이블과 다대일 관계를 설정
    
    # Chlidren Realtion
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))     # 외래키 생성, "blog_posts.id" 블로그 포스트는 blog_posts의 테이블 이름을 참조 - 외래키의 역할은 두 개의 테이블을 연결해주는 역할을 함
    parent_post = relationship("BlogPost", back_populates="comments")   # BlogPost 개체에 대한 참조를 만듬, "comments"은 BlogPost 클래스의 게시물 속성을 참조 
    text = db.Column(db.Text, nullable=False)                           # 블로그 게시물 댓글(Text), not null 설정

## --- DB내 테이브르 생성 및 Flask-Login 기능 정의 ---
# DB에 있는 모든 테이블 생성
db.create_all()

# Flask-Login에 대한 사용자 로더 기능 정의 - 사용자 ID를 기준으로 DB에서 사용자 로드
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

## --- admin-only라는 데코레이터 작성 ---
def admin_only(f):
    @wraps(f)                                                           # 데코레이터 함수가 원래 이름과 독스트링을 유지하도록 보장
    def decorated_function(*args, **kwargs):                            # 위치 및 키워드 인수를 원하는 만큼 취하므로 모든 함수와 함꼐 사용 가능                         
        if current_user.id != 1:                                        # 로그인 상태인지 확인 - 만약 id가 1이 아닐 경우 
            return abort(403)                                           # 403 에러 호출
        return f(*args, **kwargs)                                       # 3단계의 조건이 충족되지 않으면(사용자 ID가 1임) 제공된 인수와 키워드를 사용하여 원래 함수 f()가 호출 됨
    return decorated_function                                           # 데코레이터는 경로 정의의 원래 함수를 대체하는데 사용되는 래퍼 함수를 반환 


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
        
        if User.query.filter_by(email=form.email.data).first():         # 만약 이미 존재하는 email이 입력되었다면
            flash("You've already signed up with that email, log in instead!")  # 경고 메시지 출력
            return redirect(url_for('login'))                                   # 로그인 페이지로 리다이렉트
        
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
        
        login_user(new_user)                                            # 사용자 등록이 완료된 경우, Flask-Login으로 사용자 인증 후 자동 로그인
        
        return redirect(url_for("get_all_posts"))                       # 등록 완료 후 get_all_posts 함수(home)로 리디렉션
        
    return render_template("register.html", form=form)                  # 지정한 url 체계로 register.html 템플릿 랜더링 

# 3. 유저 로그인 페이지 - URL 체계: http://127.0.0.1:5000/login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()                                                  # WTForm 양식 LoginForm으로 초기화 
    if form.validate_on_submit():                                       # 만약 WTForm 양식이 제출되었다면
        email = form.email.data                                             # email 값 가져오기 
        password = form.password.data                                       # password 값 가져오기 
        
        user = User.query.filter_by(email=email).first()                    # 유저 데이터 가져오기 
        
        # 사용자 데이터가 존재하는지, 비밀번호가 일치하는 지 확인 
        if not user:                                                        # 만약 유저 데이터가 존재하지 않는 경우 
            flash("That email does not exist, please try again.")           # 에러 메시지 출력 
            return redirect(url_for('login'))                               # 로그인 페이지로 리디렉션
        
        elif not check_password_hash(user.password, password):              # 만약 입력한 비밀번호와 해시+솔트 방식으로 저장된 비밀번호가 일치하지 않을 경우
            flash('Password incorrect, please try again.')                  # 에러 메시지 출력
            return redirect(url_for('login'))                               # 로그인 페이지로 리디렉션
        
        # 만약 등록된 유저 데이터가 모두 일치할 경우 
        else:
            login_user(user)                                                # 유저 로그인 
            return redirect(url_for('get_all_posts'))                       # get_all_posts 함수(home)로 리디렉션
    
    return render_template("login.html", form=form)                         # 지정된 URL 체계로 login.html 템플릿을 렌더링

# 4. 로그아웃 - URL 체계: http://127.0.0.1:5000/logout
@app.route('/logout')
def logout():
    logout_user()                                                       # Logout_user() 함수가 호출되어 현재 사용자를 로그아웃
    return redirect(url_for('get_all_posts'))                           # 로그아웃 후 get_all_posts 함수(home)로 리디렉션

# 5. post_id 기준으로 게시된 블로그 글 조회 page - url 체계: http://127.0.0.1:5000/post/<post_id> -> CRUD 중 READ
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    form = CommentForm()                                                # WTForm 양식 CommentForm으로 초기화 
    requested_post = BlogPost.query.get(post_id)                        # post_id 기준 특정 게시물 조회
    
    if form.validate_on_submit():                                       # 만약 WTForm 양식이 제출되었다면
        if not current_user.is_authenticated:                           # 만약 로그인 되어 있지 않다면         
            flash("You need to login or register to comment.")          # 메시지 출력 - "로그인을 하시거나 유저 등록을 하시고 난 뒤 댓글을 작성해주세요"
            return redirect(url_for("login"))                           # 로그인 페이지로 리디렉션 
        
        new_comment = Comment(                                          # Comment 모델을 이용하여 새로운 댓글 데이터 생성                                
            text=form.comment_text.data,                                        # WTForm의 comment text 필드에 입력한 값에 액세스 (입력한 값 저장)
            comment_author=current_user,                                        # 댓글 입력한 유저 정보 
            parent_post=requested_post                                         # 댓글 대상 포스팅 
        )
        
        db.session.add(new_comment)                                     # SQLAlchemy의 세션에 새로운 댓글 데이터 추가
        db.session.commit()                                             # 변동 사항 DB에 커밋 
        
    return render_template("post.html", post=requested_post, form=form, current_user=current_user)     # 요청된 게시물과 같이 post.html 템플릿 랜더링, 현재 유저 지정

# 6. 블로그 관리자 소개 page - url 체계: http://127.0.0.1:5000/about
@app.route("/about")
def about():
    return render_template("about.html")                                # about.html 템플릿 랜더링

# 7. 블로그 관리자 연락 page - url 체계: http://127.0.0.1:5000/contact
@app.route("/contact")
def contact():
    return render_template("contact.html")                              # contact.html 템플릿 랜더링

# 8. 새로운 게시글 추가 page - url 체계: http://127.0.0.1:5000/new-post -> CRUD 중 CREATE
@app.route("/new-post", methods=['GET', 'POST'])
@admin_only                                                             # 데코레이터 표시
def add_new_post():
    form = CreatePostForm()                                             # WTForm 양식 초기화 
    if form.validate_on_submit():                                       # 만약 WTForm 양식이 제출되었다면
        new_post = BlogPost(                                            # BlogPost 객체를 생성, 생성과 동시에 post 페이지에 기록한 데이터들 받기
            title=form.title.data,                                          # 게시글 제목 
            subtitle=form.subtitle.data,                                    # 게시글 부제목 
            body=form.body.data,                                            # 게시글 본문 
            img_url=form.img_url.data,                                      # 블로그에 사용할 Img_URL
            author=current_user,                                            # 블로그 게시자
            date=date.today().strftime("%B %d, %Y")                         # 블로그 게시 날짜 
        )
        
        db.session.add(new_post)                                        # 입력한 내용 DB에 추가 
        db.session.commit()                                             # DB 변경사항 커밋 
        
        return redirect(url_for("get_all_posts"))                       # 새 게시물을 성공적으로 추가한 경우 get_all_posts(home에 있는 게시글 목록) 함수를 트리거하여 home URL로 리다이렉션
    
    return render_template("make-post.html", form=form, current_user=current_user) # 만약 양식이 제출되지 않거나 유효성 검사를 통과 못했을 경우 make-post.html 템플릿을 생성하기 위한 양식으로 렌더링, 현재 로그인한 사용자에 대한 정보를 템플릿에서 사용할 수 있음

# 9. 기존 게시글 수정 page - url 체계: http://127.0.0.1:5000/edit-post/<post_id> -> CRUD 중 UPDATE
@app.route("/edit-post/<int:post_id>", methods=['GET', 'POST'])
@admin_only                                                             # 데코레이터 표시
def edit_post(post_id):
    # 수정할 게시글 불러오는 부분
    post = BlogPost.query.get(post_id)                                  # post_id 기준 수정할 특정 게시물 조회
    edit_form = CreatePostForm(                                         # post_id 기준 수정할 특정 게시물 게시글 수정을 위해 WTForm에 필드 자동으로 채우기 
        title=post.title,                                                   # 게시글 제목 
        subtitle=post.subtitle,                                             # 게시글 부제목 
        img_url=post.img_url,                                               # 게시글 img URL 
        author=current_user,                                                # 게시자 
        body=post.body                                                      # 게시글 본문
    )
    
    # 게시글 수정 데이터 대입 부분
    if edit_form.validate_on_submit():                                  # 만약 WTForm 양식(edit_form)이 제출되었다면
        post.title = edit_form.title.data                                   # 수정할 게시글 제목 
        post.subtitle = edit_form.subtitle.data                             # 수정할 게시글 부제목 
        post.img_url = edit_form.img_url.data                               # 수정할 Img URL
        post.author = current_user                                  # 수정할 게시자 
        post.body = edit_form.body.data                                     # 수정할 게시글 
        
        db.session.commit()                                             # 수정완료 후 DB애 변경사항 커밋 
        return redirect(url_for("show_post", post_id=post.id))          # 수정한 해당 게시글로 리디렉션

    # make-post.html 템플릿을 생성하기 위한 양식으로 렌더링, form은 edit_form 지정, edit 허용, 현재 로그인한 사용자에 대한 정보를 템플릿에서 사용할 수 있음
    return render_template("make-post.html", form=edit_form, is_edit=True, current_user=current_user) 

# 10. 게시글 삭제 - url 체계: http://127.0.0.1:5000/delete/<post_id> -> CRUD 중 DELTE
@app.route("/delete/<int:post_id>")
@admin_only                                                             # 데코레이터 표시 
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)                        # 해당 게시글 찾기 
    db.session.delete(post_to_delete)                                   # 해당 게시글 삭제 
    db.session.commit()                                                 # 삭제 후 변경사항 커밋 
    return redirect(url_for('get_all_posts'))                           # 삭제 완료 후 Home으로 리디렉션

# 어플리케이션 실행 - 디버그 모드 
if __name__ == "__main__":
    app.run(debug=True)
