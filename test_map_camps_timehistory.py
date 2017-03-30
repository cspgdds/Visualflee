import map_camps_timehistory as mct
import pandas as pd
import unittest

class test_mct(unittest.TestCase):
    def setUp(self):
        N = 100
        popn = [n * 500 for n in range(N)]
        self.t = {"Bujumbura":popn, "Bubanza":popn}
        self.ts = pd.DataFrame(data=self.t)

        self.d = {'name': ["Bujumbura","Bubanza"], 
            'longitude': [29.3644,29.391], 
            'latitude' :[-3.3822,-3.0804], 
            'location_type': ["conflict","city"], 
            'time': [20,50]}
        self.df = pd.DataFrame(data=self.d)
        i = 0

    def test_get_loctype(self):
        for location in self.df.itertuples():
            loctype = mct.get_loctype(location, self.ts.index)
            assert len(loctype) == len(self.ts.index)
            
            for t in range(location.time):
                self.assertEqual(loctype[t], 'city')

            for t in range(location.time, len(loctype)):
                self.assertEqual(loctype[t], 'conflict')
    
    def test_get_population(self):
        # get_population(timeseries_data, name, defaultpop=1000)
        pop_buj = mct.get_population(self.ts, 'Bujumbura')
        assert (pop_buj == self.ts['Bujumbura']).all()
        
        # Test handling missing location
        pop_dflt = mct.get_population(self.ts, 'Not a place', defaultpop=919)
        assert (pop_dflt == 919).all(), pop_dflt
    
    def test_make_features(self):
        # Smoke test - check that it doesn't crash doing this
        mct.make_features(locations_file='blocations.csv',
                          timeseries_file='burundioutput.csv',
                          startdate='2015-05-01')

if __name__ == '__main__':
    unittest.main()
