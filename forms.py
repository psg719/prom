from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email
import re



class MyForm(FlaskForm):
    date = StringField('Month Date ex. August 2020')
    city = StringField('City ex. Toronto')
    submit = SubmitField('Submit')
