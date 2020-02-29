from flask import Flask, render_template
    # flash - позволяет передавать сообщения между route-ами
    # redirect - делает перенаправление пользователя на другую страницу
    # url_for - помогает получить url по имени функции, которая этот url обрабатывает
from flask_login import LoginManager, current_user, login_required
    # login_user - обработка формы логина
    # current_user - объект текущего пользователя
    # login_required - декоратор
    # import requests
from webapp.weather import weather_by_city
from webapp.db import db  # импорт модулей для связик с базой данных, создания экземпляров классов
from webapp.news.models import News
from webapp.user.models import User  # импорт модулей для связик с базой данных, создания экземпляров классов
from webapp.user.forms import LoginForm  # импорт форм для ввода данных пользователя

from webapp.admin.views import blueprint as admin_blueprint
from webapp.user.views import blueprint as user_blueprint
from webapp.news.views import blueprint as news_blueprint

# запуск фласк в командной строке unix: export FLASK_APP=webapp && export FLASK_ENV=development && flask run
# запуск фласк в командной строке win: set FLASK_APP=webapp && set FLASK_ENV=development && set DEBUG_MODE=1 && flask
# run


def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()  # создание экземпляра логина менеджера
    login_manager.init_app(app)  # инициализация (передаем ему app)
    login_manager.login_view = 'user.login'  # как будет называться функция, которая будет заниматься логином

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(news_blueprint)
    app.register_blueprint(user_blueprint)

    # Проверка пользователя
    @login_manager.user_loader
    # функция, которая будет получать по id (user_id) нужного пользователя. Т.е при каждом заходе на страницу  Логин-
    # менеджер будет обращаться к базе данных
    # возвращает объект User, которы далее будет использоваться.
    def load_user(user_id):
        return User.query.get(user_id)  # запрос к базе данных

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
