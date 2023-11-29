from flask_wtf import FlaskForm                             # Flask-WTForm 클래스 
from wtforms import StringField, SubmitField, SelectField   # Flask-WTForm의 텍스트 입력, 양식 제출, 드롭다운 목록에 사용
from wtforms.validators import DataRequired, URL            # 유효성 검사기 - DataRequired: 필드가 비었는지 확인, URL - url 형식 검사

# Add Cafe를 위한 WTForm 클래스 정의 - 추후 html에  wtf.quick_form(form)에 대입 
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])                # 카페 이름 텍스트 입력 필드 - 값이 비어있는지 유효성 검사
    location = StringField('Location URL', validators=[DataRequired(), URL()])  # 카페 위치 텍스트 입력 필드 - 값이 비었는지, URL 형식인지 유효성 검사
    open_time = StringField('Open', validators=[DataRequired()])                # 카페 오픈 시간 텍스트 입력 필드 - 값이 비었는지 유효성 검사 
    close_time = StringField('Close', validators=[DataRequired()])              # 카페 클로즈 시간 텍스트 입력 필드  - 값이 비었는지 유효성 검사 
    coffee_rating = SelectField('Coffee Rating', 
                                choices=[('☕', '☕'), ('☕☕', '☕☕'), ('☕☕☕', '☕☕☕'), ('☕☕☕☕', '☕☕☕☕'), ('☕☕☕☕☕', '☕☕☕☕☕')], 
                                validators=[DataRequired()])                    # 카페 커피 등급 드롭다운 선택 필드 - 값이 비었는지 유효성 검사 
    wifi_rating = SelectField('Wifi Rating', 
                              choices=[('✘', '✘'), ('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪'), ('💪💪💪💪', '💪💪💪💪'), ('💪💪💪💪💪', '💪💪💪💪💪')], 
                              validators=[DataRequired()])                      # 카페 와이파이 등급 드롭다운 선택 필드 - 값이 비었는지 유효성 검사 
    power_rating = SelectField('Power Rating', 
                               choices=[('✘', '✘'), ('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'), ('🔌🔌🔌🔌', '🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')], 
                               validators=[DataRequired()])                     # 카페 전력 등급 드롭다운 선택 필드 - 값이 비었는지 유효성 검사 
    submit = SubmitField(label='Submit')                                        # 제출 버튼
