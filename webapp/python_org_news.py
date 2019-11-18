from datetime import datetime
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from webapp.model import db, News

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    
    except (result.RequestException, ValueError):
        print('Сайт недоступен')
        return False


def get_python_news():

    html = get_html('http://www.python.org/blogs/')
    
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
        result_news = []

        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text
            try:
                print('Перевод в стандартный временной формат')
                published = datetime.strptime(published, '%Y-%m-%d') # Перевод текстовое время в стандартный
                # временной формат
            except(ValueError):
                published = datetime.now() # если данные published не получается вернем сегодняшнюю дату

            save_news(title, url, published) # сохраняет в базе данных db

def save_news(title, url, published):
    print('Запуск save_news')
    # проверка наличия повторяющихся новостей
    news_exists = News.query.filter(News.url == url).count()

    if not news_exists:
        news_news = News(title=title, url=url, published=published)
        db.session.add(news_news)
        db.session.commit()

if __name__ == '__main__':

    from webapp import create_app
    app = create_app()
    with app.app_context():
        print('Запуск python_get_news')
        get_python_news()

