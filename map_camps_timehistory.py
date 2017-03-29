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

    for i in range(df.shape[0]):
        folium.CircleMarker(location=[df['latitude'][i], 
                                      df['lognitude'][i]], 
                               radius=df['population'][i],
                                popup=df['name'][i], color='r',
                        fill_color='r').add_to(m)
    m.save("out.html")

def read_csv(locoutput, outputfile):

    #Load csv data into pandas dataframes
    df = pd.read_csv(locoutput)
    ts = pd.read_csv(outputfile)

    return df,ts

def extract_data(df, ts, startdate, defaultpop=1000):

    name = df['name'][i]
    latlon = [df['latitude'][i], df['lognitude'][i]]
    changetime = df['time'][i]
    if pd.isnull(changetime):
        loctype = [df['location_type'][i]]*ts.shape[0]
    else:
        #0:changetime, loctype = "city"
        loctype = ['city'] * (int(changetime))
        #changetime:-1, loctype = "conflict"
        loctype +=['conflict'] * int(ts.shape[0] - changetime)
       
    index = pd.date_range(startdate, periods=ts.shape[0])
    try:
        timeseries = pd.Series(ts[name].values, index=index)
    except KeyError:
        print("warning ", name, "missing from burundioutput" )
        timeseries = pd.Series(defaultpop, index=index)

    return latlon, name, loctype, timeseries


#Get meta data for city
startdate = '2015-5-1'
locoutput = './blocations.csv'
outputfile = './burundioutput.csv'
df, ts = read_csv(locoutput, outputfile)

features = []
df = pd.read_csv(locoutput)
for i in range(df.shape[0]):
    latlon, name, loctype, timeseries = extract_data(df, ts, startdate)
    feature = mgj.make_gj_points(latlon, name, 
                                 loctype, timeseries)
    features.extend(feature)

#Write to file
mgj.write_geojson_from_features('all_camps.json', features)





