from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

# Flast-WTF으로 Login 양식 만들기 
class LoginForm(FlaskForm):
    email = StringField('Email')            # 유저명 - 이메일 형식(string)
    password = PasswordField('Password')    # 비밀번호 - string 형식 