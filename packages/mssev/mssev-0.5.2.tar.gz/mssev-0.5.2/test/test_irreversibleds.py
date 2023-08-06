import unittest
import numpy as np
import pandas as pd

from mssev import irreversible_ds

import matplotlib.pyplot as plt


class TestGlobalMSSS(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = pd.read_csv('test/samples/assessments.csv',
                               parse_dates=['date'])

    def test_values(self):
        iedss = irreversible_ds(self.data)
        self.assertTrue(np.allclose(iedss, self.data.iedss, equal_nan=True))
