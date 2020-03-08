from flask import render_template, redirect, url_for, flash
from flask import Blueprint
from flask_login import current_user, login_user, logout_user
from webapp.user.models import User  # импорт модулей для связик с базой данных, создания экземпляров классов
from webapp.user.forms import LoginForm  # импорт форм для ввода данных пользователя


blueprint = Blueprint('user', __name__, url_prefix='/users')
    # 'user' - это название Blueprint'а
    # __name__ - имя модуля. Отсавляем так.
    # '/users' - то, с чего будут начинаться роуты

@blueprint.route('/login')
def login():
    # проверка соответствия пользователя по логину и паролю и переадресация его в index
    if current_user.is_authenticated: # is_authenticated добавлен из UserMixin, который унаследован при создании
        # класса User
        return redirect(url_for('news.index'))

    title = 'Авторизация'
    login_form = LoginForm()

    return render_template('user/login.html', page=title, form=login_form)


@blueprint.route('/process_login', methods=['Post'])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():  # проверка данных формы
        user = User.query.filter(User.username == form.username.data).first()  # получение пользователя из базы
        # данных
        if user and user.check_password(form.password.data):  # Проверка пользователя и пароля из формы
            login_user(user, remember=form.rememberme.data)  # залогинивание и запоминанеи пользователя
            flash('Вы успешно зашли на сайт')  # сообщение пользователю
            return redirect(url_for('news.index'))

    flash('Неправильно введен логин или пароль.')
    return redirect(url_for('user.login')) ## т.к. это blueprint, то добавлен "user." к "login"

@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно разлогинились')
    return redirect(url_for('news.index'))
