from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from src.db import db_session
from src.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(message='username is empty.')])
    password = StringField('Password', validators=[
                           DataRequired(message='password is wrong.')])
    submit = SubmitField('submit')
