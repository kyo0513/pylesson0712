import pandas as pd
import folium
from folium.features import CustomIcon

df=pd.read_csv('174.csv',encoding='shift_jis')
img = 'smile.png'
icon = CustomIcon(
    icon_image = img,
    icon_size = (50, 50),
    icon_anchor = (30, 30),
    #shadow_image = shadow_img, # 影効果（今回は使用せず コメントアウト
    #shadow_size = (30, 30),
    #shadow_anchor = (-4, -40),
    popup_anchor = (3, 3)
)
icon_latlng = [35.942957, 136.198863]

#print(len(df))
#print(df.columns.values)

store=df[['展示場所の緯度','展示場所の経度','名称']].values
#print(len(store))
#print(store)

m=folium.Map(location=[35.942957,136.198863],zoom_start=16)

for data in store:
    folium.Marker([data[0],data[1]],tooltip=data[2],icon_image = img).add_to(m)

folium.Marker(
    location = icon_latlng,
    popup = 'はかせ',
    tooltip = 'はかせ',
    icon = icon
).add_to(m)

m.save('store.html')

