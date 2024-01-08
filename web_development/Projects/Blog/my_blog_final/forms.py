from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

## --- New Post를 위한 WTForm 클래스 및 CKEditor 정의 ---
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])             # 블로그 제목 텍스트 입력 필드 - 빈 값 여부 유효성 검사
    subtitle = StringField("Subtitle", validators=[DataRequired()])                 # 블로그 부제목 텍스트 입력 필드 - 빈 값 여부 유효성 검사 
    author = StringField("Your Name", validators=[DataRequired()])                  # 블로그 글쓴이 텍스트 입력 필드 - 빈 값 여부 유효성 검사
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])     # 블로그 이미지 URL 입력 필드 - 빈 값 여부 유효성 검사 
    body = CKEditorField("Blog Content", validators=[DataRequired()])               # 블로그 게시글 텍스트 입력 필드 - CKEditorField 사용, 빈 값 여부 유효성 검사  
    submit = SubmitField("Submit Post")                                             # 재츌 버튼
    
## --- 유저 등록을 위한 WTForm 클래스 정의 ---
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])                       # 유저 등록 email 입력 필드 - 빈 값 여부 유효성 검사
    password = PasswordField("Password", validators=[DataRequired()])               # 유저 등록 password 입력 필드 - 빈 값 여부 유효성 검사 
    name = StringField("Name", validators=[DataRequired()])                         # 유저 등록 name 입력 필드 - 빈 값 여부 유효성 검사 
    submit = SubmitField("Sign Me Up!")                                             # 제출 버튼 
