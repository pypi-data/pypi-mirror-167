import unittest
import numpy as np
import pandas as pd

from mssev import MSSS


class TestMSSS(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = pd.read_csv('test/samples/mssev.csv')

    def test_roxburgh(self):
        original_msss = MSSS(self.data, ref='roxburgh')
        self.assertTrue(np.allclose(original_msss,
                                    self.data.oGMSSS,
                                    equal_nan=True))

    @unittest.expectedFailure
    def test_manouchehrinia(self):
        updated_msss = MSSS(self.data, ref='manouchehrinia')
        self.assertTrue(np.allclose(updated_msss,
                                    self.data.uGMSSS,
                                    equal_nan=True))
