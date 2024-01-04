from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddCafeForm(FlaskForm):
    """
    Form for adding a new cafe
    """
    cafe_name = StringField('Cafe Name', validators=[DataRequired()])
    cafe_address = StringField('Cafe Address', validators=[DataRequired()])
    cafe_city = StringField('Cafe City', validators=[DataRequired()])
    cafe_state = StringField('Cafe State', validators=[DataRequired()])