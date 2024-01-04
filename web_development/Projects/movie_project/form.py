from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Flask-WTF으로 영화 평점 수정 양식 만들기 
class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")   # 평점 기입 Form
    review = StringField("Your Review")                      # 리뷰 기입 Form
    submit = SubmitField("Done")                             # 등록 Form

# Flask-WTF로 영화 제목 추가 양식 만들기 
class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])    # 영화 타이틀 검색 Form
    submit = SubmitField("Add Movie")                                  # 등록 Form