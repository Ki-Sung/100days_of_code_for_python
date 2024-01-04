from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

# Flast-WTF으로 Login 양식 만들기 
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])            # 유저명 - 이메일 형식(string), 유효성 검사 (이메일 형식으로 할 것)
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])    # 비밀번호 - string 형식, 유효성 검사
    submit = SubmitField(label='Log In')                                       # 로그인 버튼 