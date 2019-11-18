from flask import Flask, render_template
import requests
from webapp.weather import weather_by_city
from webapp.model import db, News

# запуск фласк в командной строке: export FLASK_APP=webapp && export FLASK_ENV=development && flask run
# запуск фласк в командной строке win: set FLASK_APP=webapp && set FLASK_ENV=development && set DEBUG_MODE=1 && flask
# run

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        page_title = 'Новости Python:'
        w = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        nws = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', page=page_title, weather=w, news_list=nws)
        
    return app