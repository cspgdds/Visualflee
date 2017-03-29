from datetime import timedelta
import json

def make_gj_points(latlon, name, timeseries):
    return  [{
        'type': 'Feature',
        'properties': {
            'start': day.isoformat(),
            'end': (day + timedelta(days=1)).isoformat(),
            'name': name,
            'population': population
        },
        'geometry': {'type': 'Point', 'coordinates': latlon}
    } for (day, population) in timeseries
    ]
    
def write_geojson(filename, latlon, name, timeseries)
    features = make_gj_points(latlon, name, timeseries)
    with open(filename, 'w') as f:
        json.dump({
            'type': 'FeatureCollection',
            'features': features,
        }, f)
