from hiker import Hiker
import unittest


class TestHiker(unittest.TestCase):
    
    def test_input_is_list(self):
        with self.assertRaises(Exception):
            h = Hiker('not list')
    
    def test_input_all_items_are_ints(self):
        with self.assertRaises(Exception):
            h = Hiker([1, 2, 'not int'])

    def test_all_items_are_there(self):
        input = [1, 2, 3, 4, 5]
        h = Hiker(input)
        self.assertEqual(input, h.ints)

    def test_all_items_are_ordered(self):
        input = [5, 2, 1, -1, 3, -2]
        h = Hiker(input)
        self.assertEqual([-2,-1,1,2,3,5], h.ints)

    def test_all_closest_method(self):
        input = [5, 2, 1, -1, 3, -2]
        h = Hiker(input)
        self.assertEqual(1, h.closest())

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
