"""Unittests for getdata.py

Copyright 2017 Jeffrey Elkner
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import unittest
import pandas as pd

import getdata


class Test(unittest.TestCase):

    def testGetCSV(self):
        url = ("https://apps.elections.virginia.gov/SBE_CSV/ELECTIONS/"
               "ELECTIONTURNOUT/Turnout-2010%20November%20General.csv"
               )
        print(url)
        df = getdata.ReadCSV(url)
        self.assertTrue(isinstance(df, pd.core.frame.DataFrame))


if __name__ == "__main__":
    unittest.main()
