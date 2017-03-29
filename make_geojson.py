from datetime import timedelta, date
import json

def make_gj_points(latlon, name, loctype, timeseries):
    return  [{
        'type': 'Feature',
        'properties': {
            'start': day.isoformat(),
            'end': (day + timedelta(days=1)).isoformat(),
            'name': name,
            'loctype': loctype,
            'population': int(population)
        },
        'geometry': {'type': 'Point', 'coordinates': latlon}
    } for (day, population) in timeseries.iteritems()
    ]

def write_geojson_from_features(features):
    with open(filename, 'w') as f:
        json.dump({
            'type': 'FeatureCollection',
            'features': features,
        }, f, indent=2)
    
def write_geojson(filename, latlon, name, loctype, timeseries):
    features = make_gj_points(latlon, name, loctype, timeseries)
    with open(filename, 'w') as f:
        json.dump({
            'type': 'FeatureCollection',
            'features': features,
        }, f, indent=2)

if __name__ == '__main__':
    import pandas
    index = pandas.date_range('2015-3-1', periods=100)
    popn = [n * 500 for n in range(100)]
    ser = pandas.Series(popn, index=index)
    write_geojson('test.json', (52.0, 0.0), 'Examplecamp', 'camp', ser)
