
import folium
import pandas
data = pandas.read_csv("file_processs/Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
el  = list(data["ELEV"])

def colour_procucer(er):
    if er < 1000:
        return "green"
    elif er >= 1000 and  er < 1500:
        return "purple"
    else :
        return "red"       

map = folium.Map(location = [53.462592, -2.291076] , zoom_start=6, tiles = "Stamen Terrain")

Fg = folium.FeatureGroup(name = "mymap")

for lt , ln , el in zip(lat, lon , el):

# for coordinates in [[53.462592, -2.291076] , [52.462592, -2.491076] ]:
    Fg.add_child(folium.Marker(location = [lt , ln] , popup = str(el) + "m" , icon = folium.Icon(color = colour_procucer(el))))
# Fg.add_child(folium.CircleMarker(location = [lt , ln] , popup = str(el) + "m" , fill_color = colour_procucer(el) ))
# Fg.add_child(folium.Marker(location=[53.462592, -2.291076], popup = "Hi i am at old trafford" , icon = folium.Icon(color='red')))
# map.add_child(folium.Marker(location=[53.462592, -2.291076], popup = "Hi i am at old trafford" , icon = folium.Icon(color='red')))
# we could have used above line(19) of code but instead we used Fg to keep code more organised and it also helps when we add layer of control features

Fg.add_child(folium.GeoJson(data = open("resources/world.json" , 'r' , encoding='utf-8-sig' ).read() ))

map.add_child(Fg)
map.save("manchester.html")
