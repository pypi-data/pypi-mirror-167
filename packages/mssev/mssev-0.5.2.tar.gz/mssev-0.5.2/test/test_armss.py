import numpy as np
import pandas as pd
import unittest

from mssev import ARMSS


class TestARMSS(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = pd.read_csv('test/samples/mssev.csv')

    def test_original(self):
        original_armss = ARMSS(self.data)
        self.assertTrue(np.allclose(original_armss,
                                    self.data.gARMSS,
                                    equal_nan=True))
