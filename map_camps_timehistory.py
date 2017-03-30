import numpy as np
import pandas as pd
import make_geojson as mgj

def save_map(df):
    """Not currently used - this was an experiment in a making the map a
    different way, using the 'folium' Python library (which wraps leafletjs)
    """
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


def get_loctype(location, date_index):
    """Returns a pandas Series of the location type for each day.
    
    Locations with a changetime have type *city* before that day, and *conflict*
    after it.
    """
    n_days = len(date_index)
    changetime = location.time
    if pd.isnull(changetime):
        loctype = location.location_type
    else:
        #0:changetime, loctype = "city"
        loctype = ['city'] * int(changetime)
        #changetime:-1, loctype = "conflict"
        loctype +=['conflict'] * int(n_days - changetime)
    return pd.Series(loctype, index=date_index)


def get_population(timeseries_data, name, defaultpop=1000):
    """Get the population time series for the named location.
    
    If the name is not in the data provided, construct a time series with a
    constant default population, so that the marker shows up on the map.
    """
    try:
        return timeseries_data[name]
    except KeyError:
        print("Warning:", name, "missing from time series data")
        return pd.Series(defaultpop, index=timeseries_data.index)


def make_features(locations_file='blocations.csv',
                  timeseries_file='burundioutput.csv',
                  startdate='2015-05-01'):
    locations = pd.read_csv(locations_file)
    timeseries = pd.read_csv(timeseries_file)
    n_days = timeseries.shape[0]
    # Construct an index with real dates rather than day numbers
    timeseries.index = pd.date_range(startdate, periods=n_days)

    features = []
    for location in locations.itertuples(name='Location'):
        latlon = (location.latitude, location.longitude)
        loctype_by_day = get_loctype(location, timeseries.index)
        population_by_day = get_population(timeseries, location.name)
        
        data_for_location = pd.DataFrame({'loctype': loctype_by_day,
                                          'population': population_by_day})
        feature = mgj.make_gj_points(latlon, location.name, data_for_location)
        features.extend(feature)
    return features

if __name__ == '__main__':
    features = make_features()
    #Write to file
    mgj.write_geojson_from_features('all_camps.json', features)
