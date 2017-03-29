from datetime import timedelta, date
import json

def make_gj_points(latlon, name, timeseries):
    return  [{
        'type': 'Feature',
        'properties': {
            'start': day.isoformat(),
            'end': (day + timedelta(days=1)).isoformat(),
            'name': name,
            'population': int(population)
        },
        'geometry': {'type': 'Point', 'coordinates': latlon}
    } for (day, population) in timeseries.iteritems()
    ]
    
def write_geojson(filename, latlon, name, timeseries):
    features = make_gj_points(latlon, name, timeseries)
    with open(filename, 'w') as f:
        json.dump({
            'type': 'FeatureCollection',
            'features': features,
        }, f)

def make_dates(number, start_day=date(2015, 3, 1)):
    [start_day + timedelta(days=n) for n in range(number)]

if __name__ == '__main__':
    import pandas
    index = pandas.date_range('2015-3-1', periods=100)
    popn = [n * 500 for n in range(100)]
    ser = pandas.Series(popn, index=index)
    write_geojson('test.json', (52.0, 0.0), 'Examplecamp', ser)
