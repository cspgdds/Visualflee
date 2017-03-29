from datetime import timedelta, date
import json

def make_gj_points(latlon, name, loctype, timeseries):
    lonlat = latlon[1], latlon[0]
    return  [{
        'type': 'Feature',
        'properties': {
            'start': day.strftime('%Y-%m-%d'),
            'end': (day + timedelta(days=1)).strftime('%Y-%m-%d'),
            'name': name,
            'loctype': lt,
            'population': int(population)
        },
        'geometry': {'type': 'Point', 'coordinates': lonlat}
    } for ((day, population), lt) in zip(timeseries.iteritems(), loctype)
    ]

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
