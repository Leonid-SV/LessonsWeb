from getpass import getpass # позволяет что-то вводить в коммандной строке не выводя текст
import sys
from webapp import create_app
from webapp.model import db, User
app = create_app()

with app.app_context():

    username = input('Введите имя: ')

    if User.query.filter(User.username == username).count(): # Поиск в базе данных
        print('Пользователь с таким именем уже существует.')
        sys.exit(0)  # Выходим из программы

    password_1 = getpass('Введите пароль')
    password_2 = getpass('Повторите пароль')

    if not password_1 == password_2:
        print('Пароли не совпадают.')
        sys.exit(0)  # Выходим из программы
    else:
        password = password_1

    new_user = User(username=username, role='admin')
    new_user.set_password(password) #  шифрование пароля

    db.session.add(new_user) # добавление юзера в базу
    db.session.commit() # подтверждения операций с базой

    print('Создан пользователь с ID={}'.format(new_user.id))



