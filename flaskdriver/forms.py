from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, SubmitField
from wtforms.validators import DataRequired

class SelectCategoriesForm(FlaskForm):
    select = SelectField("Choose a category", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Submit")

class RefineForm(FlaskForm):
    min_date = DateField("Minimum Airdate (YYYY-MM-DD)", format='%Y-%m-%d')
    max_date = DateField("Maximum Airdate (YYYY-MM-DD)", format='%Y-%m-%d')
    value = SelectField("Value", coerce=int, choices=[(200,"200"),(400, "400"),(600, "600"),(800, "800"),(1000, "1000")])
    submit = SubmitField("Refine")

