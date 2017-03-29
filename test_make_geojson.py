import pandas
import make_geojson

def test_make_gj_points():
    index = pandas.date_range('2015-3-1', periods=100)
    popn = [n * 500 for n in range(100)]
    ser = pandas.Series(popn, index=index)
    loctype = (['city'] * 50) + (['conflict'] * 50)
    res = make_geojson.make_gj_points((52.0, 0.0), 'Examplecamp', loctype, ser)
    
    assert len(res) == 100
    assert res[0]['type'] == 'Feature'
    assert res[0]['properties']['start'] == '2015-03-01'
    assert res[0]['properties']['end'] == '2015-03-02'
    assert res[0]['properties']['loctype'] == 'city'
    assert res[0]['geometry']['coordinates'] == (0.0, 52.0)

    assert res[50]['properties']['loctype'] == 'conflict'
    assert res[50]['properties']['start'] == '2015-04-20'
