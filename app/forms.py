from flask_wtf import FlaskForm
from wtforms import (
    BooleanField, PasswordField, StringField, SubmitField, TextAreaField)
from wtforms.validators import (
    DataRequired, Email, EqualTo, Length, ValidationError)

from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Name of Interviewee', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember')
    submit = SubmitField('Find')

class RegistrationForm(FlaskForm):
    username = StringField('Name of Interviewee', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different name.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email.')

class EditProfileForm(FlaskForm):
    username = StringField('Interviewee Name', validators=[DataRequired()])
    about_me = TextAreaField('Abstract', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')