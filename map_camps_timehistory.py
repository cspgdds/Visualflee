import numpy as np
import pandas as pd
import make_geojson as mgj

def save_map(df):
    import folium
    minlong = df['lognitude'].min()
    maxlong = df['lognitude'].max()
    minlat = df['latitude'].min()
    maxlat = df['latitude'].max()

    m = folium.Map([minlat, minlong], zoom_start=6)

    colours = ['']

    for i in range(df.shape[0]):
        folium.CircleMarker(location=[df['latitude'][i], 
                                      df['lognitude'][i]], 
                               radius=df['population'][i],
                                popup=df['name'][i], color='r',
                        fill_color='r').add_to(m)
    m.save("out.html")




#Load csv data into pandas dataframes
df = pd.read_csv('./blocations.csv')
ts = pd.read_csv('./burundioutput.csv')

#Get meta data for city
startdate = '2015-3-1'
features = []
for i in range(df.shape[0]):
    name = df['name'][i]
    latlon = [df['latitude'][i], df['lognitude'][i]]
    loctype = df['location_type'][i]

    #print(name, latlon,loctype)

    try:
        #Starting from the 1st May 2015, increments of one day
        index = pd.date_range(startdate, periods=ts.shape[0])
        timeseries = pd.Series(ts[name].values, index=index)

        feature = mgj.make_gj_points(latlon, name, loctype, timeseries)
        features.extend(feature)
    except KeyError:
        print("warning ", name, "missing from burundioutput" )

#Write to file
mgj.write_geojson_from_features('all_camps.json', features)





