from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Length, Email, EqualTo

from src.db import db_session
from src.models import Users


class RegisterForm(FlaskForm):
    fullname = StringField('Fullname', validators=[
                           DataRequired(message='Fullname is empty.')])
    username = StringField('Username',
                           validators=[DataRequired(message='Username is empty.'), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(message='Email is empty.'), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(message='Password is empty.'), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = db_session.query(Users).filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'That username is taken. Please choose a defferent one.')

    def validate_email(self, email):
        user = db_session.query(Users).filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is taken. Please choose a defferent one.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(message='username is empty.')])
    password = PasswordField('Password', validators=[
                           DataRequired(message='password is wrong.')])
    remember = BooleanField('Remember me')
    submit = SubmitField('submit')
