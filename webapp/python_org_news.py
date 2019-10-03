import requests
from pprint import pprint
from bs4 import BeautifulSoup

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
        all_news = soup.find('ul', class_ = 'list-recent-posts').findAll('li')
        
        result_news = []

        for news in all_news:
            text_ =     news.find('a').text
            published = news.find('time').text
            url =      news.find('a')['href']
            
            result_news.append({
                'text_' : text_,
                'url' : url,
                'published' : published  })

        # pprint(result_news)

        return result_news
    return False

if __name__ == '__main__':
    get_python_news()

