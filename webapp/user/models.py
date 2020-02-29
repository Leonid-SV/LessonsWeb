from flask_login import UserMixin
    # UserMixin - класс, который наследует здесь User добавляет атрибуты и модули, необходимые для работы
    # flask_login. Основные это: is_active, is_authentificated, is_anonimus, get_id() и некоторые магические методы.
from werkzeug.security import generate_password_hash, check_password_hash #для шифрования пароля
from webapp.db import db


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True, index=True, )
    username = db.Column(db.String(64), nullable=False, index=True, unique=True)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String, index=True)  # роль пользователя admin или user

    def set_password(self, password):
        # модуль односторонне зашифровывает пароль
        self.password = generate_password_hash(password)

    def check_password(self, password):
        # модуль проверяет зашифрованый пароль
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return f'<User name = {self.username}, user_id = {id}>'

