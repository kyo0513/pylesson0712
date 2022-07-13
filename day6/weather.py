import requests
import json
from pprint import pprint

"""
url = ('https://api.openweathermap.org/data/2.5/weather'
'?q={city}&appid={key}&lang=ja&units=metric')
url=url.format(city='Tokyo,JP',key='2764aaf0fb10ddc4bd0cae3f14f05a12')
"""

url = ('https://api.openweathermap.org/data/2.5/weather'
'?zip={zip}&appid={key}&lang=ja&units=metric')

url=url.format(zip='160-0006,JP',key='2764aaf0fb10ddc4bd0cae3f14f05a12')

jsondata=requests.get(url).json()
#pprint(jsondata)

print('都市名:',jsondata['name'])
print('気温:',jsondata['main']['temp'])
print('天気:',jsondata['weather'][0]['main'])
print('天気詳細:',jsondata['weather'][0]['description'])
