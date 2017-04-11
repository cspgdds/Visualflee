from datetime import timedelta, date
import json

def make_gj_points(latlon, name, timeseries):
    """Make geojson Point features for a single location.
    
    latlon: 2-tuple, e.g. (-3.3822, 29.3644)
    name: string
    timeseries: Data frame, rows representing days, with columns loctype & population
    """
    lonlat = latlon[1], latlon[0] # GeoJSON puts longitude first
    return  [{
        'type': 'Feature',
        'properties': {
            'start': day.strftime('%Y-%m-%d'),
            'end': (day + timedelta(days=1)).strftime('%Y-%m-%d'),
            'name': name,
            'loctype': row['loctype'],
            'population': int(row['population'])
        },
        'geometry': {'type': 'Point', 'coordinates': lonlat}
    } for (day, row) in timeseries.iterrows()
    ]

# This format is called JSONP; it consists of a normal blob of JSON wrapped in
# a Javascript function call (we're calling the function jpcallback for jsonp
# callback, which is a pretty bad name). This is a bit more convenient to load
# from Javascript than normal JSON (without the function call).
def write_geojson_from_features(filename, features):
    with open(filename, 'w') as f:
        f.write('jpcallback(')
        json.dump({
            'type': 'FeatureCollection',
            'features': features,
        }, f, indent=2)
        f.write(')')
    
def write_geojson(filename, latlon, name, loctype, timeseries):
    features = make_gj_points(latlon, name, loctype, timeseries)
    with open(filename, 'w') as f:
        f.write('jpcallback(')
        json.dump({
            'type': 'FeatureCollection',
            'features': features,
        }, f, indent=2)
        f.write(')')

if __name__ == '__main__':
    import pandas
    index = pandas.date_range('2015-3-1', periods=100)
    popn = [n * 500 for n in range(100)]
    ser = pandas.Series(popn, index=index)
    write_geojson('test.json', (52.0, 0.0), 'Examplecamp', 'camp', ser)
