import requests

PLACES = ['London', 'SVO', 'Череповец']

<<<<<<< HEAD
def get_weather(url):   
    response = requests.get(url=url)
    print(response.raise_for_status())
=======
def get_weather(url):
    response = requests.get(url=url)
>>>>>>> a4654831d596ab6d06c5f768ff1234782dd8f463
    print(response.text)

def main():
    for place in PLACES:
<<<<<<< HEAD
        try:
            get_weather(f'https://wttr.in/{place}?nmMTqu&lang=ru')
        except Exception as e:
            print(e)
            
            

if __name__ == '__main__':
    main()
=======
        get_weather(f'https://wttr.in/{place}?nmMTqu&lang=ru')
    
if __name__=='__main__':
    main()
    
>>>>>>> a4654831d596ab6d06c5f768ff1234782dd8f463
