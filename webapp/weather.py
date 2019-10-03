from flask import current_app
import requests

print('*'*30)

def weather_by_city(city_name):
    
    url_adr = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'

    prms = {
            'key':         current_app.config['WEATHER_API_KEY'],
            'q':           city_name,
            'format':     'json',
            'num_of_days': 1,
            'lang':       'ru',
            }
    try:
        result = requests.get(url_adr, params = prms)
        result.raise_for_status()
        weather = result.json()
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except (IndexError, TypeError):
                    return False
    except (requests.RequestException, ValueError):
        print('Сетевая ошибка.')
        return False

print('*'*30)

if __name__ == '__main__':
    print('*'*30)
    print(weather_by_city('Moscow,Russia'))

    




