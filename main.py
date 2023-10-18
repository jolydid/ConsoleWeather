import requests

PLACES = ['London', 'SVO', 'Череповец']

def get_weather(url):   
    response = requests.get(url=url)
    print(response.raise_for_status())
    print(response.text)

def main():
    for place in PLACES:
        try:
            get_weather(f'https://wttr.in/{place}?nmMTqu&lang=ru')
        except Exception as e:
            print(e)
            
            

if __name__ == '__main__':
    main()