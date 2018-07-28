import folium
import pandas as pd

# Read the file and get the values of latitude, longitude, location and elevation
data = pd.read_csv("Volcanoes_USA.txt")
lat = data["LAT"]
lon = data["LON"]
location = data["LOCATION"]
elev = data["ELEV"]


def colour_producer(elevation):
    """
    Returns the colour as per the elevation data.
    :param elevation: elevation of particular location
    """
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 2000:
        return 'yellow'
    else:
        return 'red'


# Map object with Indian Latitude and Longitute location
map = folium.Map(location=[22.790194, 79.522939], zoom_start=5, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanos")

for lt, ln, loc, el in zip(lat, lon, location, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], color="gray", fill=True, fill_color=colour_producer(el),
                                      fill_opacity=0.5,
                                      popup=loc))
    # fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(loc), icon=folium.Icon(color=colour_producer(el))))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding="utf-8-sig").read(),
                             style_function=lambda x: {'fillColor': 'yellow' if x['properties']['POP2005'] < 10000000
                             else 'green' if 10000000 <= x['properties']['POP2005'] < 20000000
                             else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map.html")
