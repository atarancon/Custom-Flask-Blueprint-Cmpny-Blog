from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField, SubmitField
from wtforms.validators import DataRequired,Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed

from flask_login import current_user
from puppycompanyblog.models import User

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = StringField('Password',validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired()])
    username = StringField('UserName',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo("pass_conf",message="Password must match")])
    pass_conf=PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField("Register")

    #validate for email 
    def validate_email(self,field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError("Your Email has been already register")

    def validate_username(self,field):
         if User.query.filter_by(username = field.data).first():
            raise ValidationError("Your username has been already register")
        
class UpdateUserForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(),Email()])
    username=StringField("Username",validators=[DataRequired()])
    picture = FileField("Update profile picture" , validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField("Update")

    #validate for email 
    def check_email(self,field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError("Your Email has been already register")

    def check_username(self,field):
         if User.query.filter_by(username = field.data).first():
            raise ValidationError("Your username has been already register")
     