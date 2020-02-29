from flask import Blueprint, current_app, render_template
from webapp.news.models import News
from webapp.weather import weather_by_city

blueprint = Blueprint('news', __name__)

@blueprint.route('/index')
def index():
    page_title = 'Новости Python:'
    w = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    nws = News.query.order_by(News.published.desc()).all()
    return render_template('index.html', page=page_title, weather=w, news_list=nws)