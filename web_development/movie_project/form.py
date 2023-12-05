from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

# Flast-WTF으로 Login 양식 만들기 
class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")   