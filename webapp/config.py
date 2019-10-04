import os

basedir = os.path.abspath(os.path.dirname(__file__))
sql_db_addr = os.path.join(basedir, '..', 'webapp.db')

WEATHER_DEFAULT_CITY = 'Moscow,Russia'
WEATHER_API_KEY = 'd9b34babc42f453c9c635222190110'
SQLALCHEMY_DATABASE_URI = 'qslite:///' + sql_db_addr