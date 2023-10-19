import requests
import urllib.parse

PLACES = ['London', 'SVO', 'Череповец']  # Замените на нужные места

def get_weather(place):
    base_url = 'https://wttr.in/'
    params = {
        'n': '',    # узкая версия (только день и ночь)
        'q': '' ,    # тихая версия (без текста "Прогноз погоды")
        'T': '',    # отключить терминальные последовательности (без цветов)
        'u': 'C',    # Градусы Цельсия
        'lang': 'ru',  # Язык (русский)
    }

    response = requests.get(urllib.parse.urljoin(base_url, place), params=params)
    
    if response.status_code == 200:
        print(response.text)
    else:
        print("Не удалось получить данные о погоде")

for place in PLACES:
    get_weather(place)
       
