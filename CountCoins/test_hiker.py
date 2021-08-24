from typing import Type
from hiker import Hiker
import unittest


class TestHiker(unittest.TestCase):

    def test_input_is_int(self):
        with self.assertRaises(TypeError):
             h = Hiker('val')

    def test_input_is_valid_dollar_bill(self):
        with self.assertRaises(ValueError):
            # valid bills are [1,2,5,10,20,50,100]
            h = Hiker(9, True)

    def test_one_dollar_change_in_quarters(self):
        h = Hiker(1, True)
        self.assertEqual(['4Q'], h.ways_change(h.QUARTERS))

    def test_50cents_change_in_quarters(self):
        h = Hiker(50)
        self.assertEqual(['2Q'], h.ways_change(h.QUARTERS))

    def test_one_dollar_change_in_dimes(self):
        h = Hiker(1, True)
        self.assertEqual(['10D'], h.ways_change(h.DIMES))

    def test_70cents_change_in_dimes(self):
        h = Hiker(70)
        self.assertEqual(['7D'], h.ways_change(h.DIMES))

    def test_one_dollar_change_in_nickles(self):
        h = Hiker(1, True)
        self.assertEqual(['20N'], h.ways_change(h.NICKLES))

    def test_one_dollar_change_in_nickles(self):
        h = Hiker(1, True)
        self.assertEqual(['100P'], h.ways_change(h.PENNIES))

    def test_15cents_change(self):
        h = Hiker(15)
        self.assertEqual('15P', h.ways_change()[0])

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
