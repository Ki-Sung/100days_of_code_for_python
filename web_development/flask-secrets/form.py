from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

# Flast-WTF으로 Login 양식 만들기 
class LoginForm(FlaskForm):
    email = StringField(label='Email')            # 유저명 - 이메일 형식(string)
    password = PasswordField(label='Password')    # 비밀번호 - string 형식 
    submit = SubmitField(label='Log In')         # 로그인 버튼 