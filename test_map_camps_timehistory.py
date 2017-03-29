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
            'lognitude': [29.3644,29.391], 
            'latitude' :[-3.3822,-3.0804], 
            'location_type': ["conflict","city"], 
            'time': [20,50]}
        self.df = pd.DataFrame(data=self.d)
        i = 0

    def test_name(self):
        startdate = '2015-5-1'
        for i in range(2):
            latlon, name, loctype, timeseries = mct.extract_data(self.df, self.ts, startdate, i)
            self.assertEqual(name, self.d['name'][i])

    def test_latlon(self):
        startdate = '2015-5-1'
        for i in range(2):
            latlon, name, loctype, timeseries = mct.extract_data(self.df, self.ts, startdate, i)
            self.assertEqual(latlon[0], self.d['latitude'][i])
            self.assertEqual(latlon[1], self.d['lognitude'][i])

if __name__ == '__main__':
    unittest.main()
