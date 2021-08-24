from hiker import Hiker
import unittest


class TestHiker(unittest.TestCase):

    def test_if_input_is_not_list(self):
        with self.assertRaises(TypeError):
            h = Hiker('[1,2,3]')        
    
    def test_if_list_not_empty(self):
        with self.assertRaises(ValueError):
            h = Hiker([])

    def test_if_not_all_numbers(self):
        with self.assertRaises(TypeError):
            h = Hiker([1,'dos',3])        
        
        # it can't rise any exception with valid list
        h = Hiker([1,2,3])

    def test_minimum_call(self):
        h = Hiker([6, 9, 15, -2, 92, 11])  
        self.assertEqual(-2, h.minimum())  

    def test_maximum(self):
        h = Hiker([6, 9, 15, -2, 92, 11])  
        self.assertEqual(92, h.maximum())  

    def test_number_of_elements(self):
        h = Hiker([6, 9, 15, -2, 92, 11])  
        self.assertEqual(6, h.number_of_elements())  

    def test_average_calculation(self):
        h = Hiker([6, 9, 15, -2, 92, 11])  
        self.assertEqual(21.833333, h.average())


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
