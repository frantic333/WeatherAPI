import requests
import json
from pprint import pprint

WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'

CITY = str(input('City is:'))
WEATHER_TOKEN = 'e1dcdd65fca0c95c3e4b86de08ccdcca'

url = WEATHER_URL.format(city=CITY,
                        token=WEATHER_TOKEN)
response = requests.get(url)
if response.status_code != 200:
    print('city not found')
data = json.loads(response.content)
#pprint(data)
#print(data['weather'])
print(data['main']['temp'])
