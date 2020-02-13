from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash #для шифрования пароля

db = SQLAlchemy()

class News(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<News {} {}>'.format(self.title, self.url)


class User(db.Model, UserMixin):

        ## UserMixin - класс, который наследует здесь User добавляет атрибуты и модули, необходимые для работы
        # flask_login. Основные это: is_active, is_authentificated, is_anonimus, get_id() и некоторые магические методы.

    id = db.Column(db.Integer, primary_key=True, index=True,)
    username = db.Column(db.String(64), nullable=False, index=True, unique=True)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String, index=True) # роль пользователя admin или user

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
