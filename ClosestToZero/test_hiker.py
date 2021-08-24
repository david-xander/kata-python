from hiker import Hiker
import unittest


class TestHiker(unittest.TestCase):
    
    def test_input_is_array(self):
        with self.assertRaises(TypeError):
            h = Hiker('asdf')

    def test_all_items_are_int(self):
        with self.assertRaises(ValueError):
            h = Hiker([1,'A',3]) 

    def test_items_are_ordered(self):
        h = Hiker([3,-1,2,1])
        self.assertEqual([-1,1,2,3], h.ints)

    def test_closest_to_zero(self):
        h = Hiker([3,-1,2,1])
        self.assertEqual(1, h.find_closest_to_zero())

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
