from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired #класс, который позволяет избежать ручных проверокы


class LoginForm(FlaskForm):

    # ниже перечислены поля форм:
    username = StringField('Имя Пользователя', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={'class': 'form-control'})
    ### render_kw={'class': 'form-control'} --- значение render_kw добавит к полю формы class со значением
    # form-control, что позволит украсить форму из bs4
    # кнопка:
    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-primary'})



