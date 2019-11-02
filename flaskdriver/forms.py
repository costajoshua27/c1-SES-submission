from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class SelectCategoriesForm(FlaskForm):
    select = SelectField("Choose a category", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Submit")