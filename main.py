import requests

PLACES = ['London', 'SVO', 'Череповец']

def get_weather(url):
    response = requests.get(url=url)
    print(response.text)

def main():
    for place in PLACES:
        get_weather(f'https://wttr.in/{place}?nmMTqu&lang=ru')
    
if __name__=='__main__':
    main()
    
