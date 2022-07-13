import requests
import json
from datetime import datetime,timedelta,timezone
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

url = ('https://api.openweathermap.org/data/2.5/forecast'
'?q={city}&appid={key}&lang=ja&units=metric')
url=url.format(city='Tokyo,JP',key='2764aaf0fb10ddc4bd0cae3f14f05a12')
jsondata=requests.get(url).json()

df=pd.DataFrame(columns=['気温'])

tz=timezone(timedelta(hours = +9),'JST')
for dat in jsondata['list']:
    #jst=str(datetime.fromtimestamp(dat['dt'],tz))
    jst=str(datetime.fromtimestamp(dat['dt'],tz))[5:-9]
    temp=dat['main']['temp']
    df.loc[jst]=temp

#pprint(df)
df.plot(figsize=(15,8))
plt.ylim(-10,40)
plt.grid()
plt.show()

