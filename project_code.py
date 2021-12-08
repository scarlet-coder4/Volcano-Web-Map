import pandas
df=pandas.read_csv("Volcanoes.txt")
lat=list(df["LAT"])
lon=list(df["LON"])
name=list(df["NAME"])
elev=list(df["ELEV"])
ty=list(df["TYPE"])
import folium
a=folium.Map(location=[39.870256093997405, -99.09758867269652],tiles="Stamen Terrain",zoom_start=4)
fg=folium.FeatureGroup(name="abcc")

def m_color(t):
    if (t == 'Stratovolcano' or t == 'Stratovolcanoes'):
        return "lightblue"
    elif (t == 'Cinder cones' or t == 'Cinder cone'):
        return "red"
    elif (t == 'Caldera' or t == 'Calderas'):
        return "blue"
    elif (t == 'Shield volcano' or t == 'Shield volcanoes'):
        return "green"
    elif (t == 'Volcanic field'):
        return "purple"
    elif (t == 'Fissure vents'):
        return "orange"
    elif (t == 'Maar'):
        return "lightred"
    elif (t == 'Lava domes'):
        return "beige"
    elif (t == 'Complex volcano'):
        return "cadetblue"
    else:
        return "darkgreen"

for lt,ln,n,el,t in zip(lat,lon,name,elev,ty):
    fg.add_child(folium.CircleMarker(location=(lt,ln),radius=5,color=m_color(t),
    fill=True,fill_opacity=1, popup="name:{} \n elevation:{}m \n type:{}".format(n,el,t)))
a.add_child(fg)
a.save("map.html")