from flask import Flask, render_template
from flask import flash, redirect, url_for
# flash - позволяет передавать сообщения между route-ами
# redirect - делает перенаправление пользователя на другую страницу
# url_for - помогает получить url по имени функции, которая этот url обрабатывает
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
# login_user - обработка формы логина
# current_user - объект текущего пользователя
# login_required -
import requests
from webapp.weather import weather_by_city
from webapp.model import db, News, User
from webapp.forms import LoginForm


# запуск фласк в командной строке: export FLASK_APP=webapp && export FLASK_ENV=development && flask run
# запуск фласк в командной строке win: set FLASK_APP=webapp && set FLASK_ENV=development && set DEBUG_MODE=1 && flask
# run



def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager() # создание экземпляра логина
    login_manager.init_app(app) # инициализация
    login_manager.login_view = 'login' # как будет называться функция, которая будет заниаться логином, она определена ниже


    # Проверка пользователя
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id) # запрос к базе данных

    @app.route('/')
    def index():
        page_title = 'Новости Python:'
        w = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        nws = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', page=page_title, weather=w, news_list=nws)

    @app.route('/login')
    def login():
        if current_user.is_authenticated: # проверка соответствия пользователя по логину и паролю и переадресация его в index
            return redirect(url_for('index'))

        title = 'Авторизация'
        login_form = LoginForm()
        return render_template('login.html', page=title, form=login_form)


    @app.route('/logout')
    def logout():
        logout_user()
        flash('вы успешно разлогинились')
        return redirect('index')


    @app.route('/process_login', methods=['Post'])
    def process_login():
        form = LoginForm()

        if form.validate_on_submit(): # проверка данных формы
            user = User.query.filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data): # Проверка пользователя и пароля из формы
                login_user(user) # залогинивание )
                flash('Вы успешно зашли на сайт') # сообщение пользователю
                return redirect(url_for('index'))

        flash('Неправильно введен логин или пароль.')
        return redirect(url_for('login'))


    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Привет админ!'
        else:
            return 'Ты не админ.'


    return app

if __name__ == '__main__':
    create_app().run(debug=True)

