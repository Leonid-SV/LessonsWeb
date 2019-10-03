from flask import Flask, render_template
import requests
from webapp.weather import weather_by_city
from webapp.python_org_news import get_python_news



def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def hello():
        
        page_title = 'прогноз погоды'
        w = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        nws = get_python_news()
        
        return render_template('index.html', page = page_title, weather = w, news_list = nws)
        
    return app