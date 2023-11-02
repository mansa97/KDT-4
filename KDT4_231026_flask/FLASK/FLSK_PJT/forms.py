from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수 입력 항목')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수 입력 항목')])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수 입력 항목')])

class UserCreateForm(FlaskForm):
    username = StringField('사용자 이름',
                            validators=[DataRequired('이름은 필수 입력 항목'),
                                         Length(min=3,max=25)])
    password1 = PasswordField('비밀번호',
                               validators=[DataRequired('비밀번호는 필수 입력 항목'),
                                           EqualTo('password2','비밀번호가 일치하지 않음')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired('비밀번호 확인은 필수 입력 항목')])
    email = EmailField('이메일', [DataRequired('이메일은 필수 입력 항목'),Email()])

class UserLoginForm(FlaskForm):
    username = StringField('사용자 이름', validators=[DataRequired(), Length(min=3,max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])