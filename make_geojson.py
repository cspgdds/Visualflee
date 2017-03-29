from datetime import timedelta, date
import json

def make_gj_points(latlon, name, timeseries):
    lonlat = latlon[1], latlon[0]
    return  [{
        'type': 'Feature',
        'properties': {
            'start': day.strftime('%Y-%m-%d'),
            'end': (day + timedelta(days=1)).strftime('%Y-%m-%d'),
            'name': name,
            'population': int(population)
        },
        'geometry': {'type': 'Point', 'coordinates': lonlat}
    } for (day, population) in timeseries.iteritems()
    ]
    
def write_geojson(filename, latlon, name, timeseries):
    features = make_gj_points(latlon, name, timeseries)
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
    write_geojson('test.json', (52.0, 0.0), 'Examplecamp', ser)
