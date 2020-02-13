import os

basedir = os.path.abspath(os.path.dirname(__file__))

WEATHER_DEFAULT_CITY = 'Moscow,Russia'
WEATHER_API_KEY = 'd9b34babc42f453c9c635222190110'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
SECRET_KEY = 'asdkljfh&^HlKHS*H' # защита от подмены формы
