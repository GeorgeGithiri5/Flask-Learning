from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,PasswordField,SubmitField,TextAreaField,BooleanField,ValidationError
from wtforms.validators import DataRequired,Length,EqualTo
from FlaskBlog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('That Username is takern')
    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('That email is takern')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('Sign In')

class updateAccountForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',validators=[DataRequired()])
    picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('update')
    

    def validate_username(self,username):
        if username.data != current_user.username:            
        user = User.query.filter_by(username = username.data).first()
        if username:
            raise ValidationError('That Username is takern')
    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        if email:
            raise ValidationError('That email is taken')

class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired])
    content = TextAreaField('Content',validators=[DataRequired])
    submit = SubmitField('Post')