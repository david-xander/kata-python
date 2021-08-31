from calculator import *
import unittest


class TestCalculator(unittest.TestCase):
    
    def test_empty_return_zero(self):
        self.assertEqual(0, Calculator().Add(''))
    
    def test_calc_one_return_one(self):
        self.assertEqual(1, Calculator().Add('1'))
    
    def test_calc_two_numbers(self):
        self.assertEqual(3, Calculator().Add('1,2'))

    def test_calc_more_then_two_numbers(self):
        self.assertEqual(6, Calculator().Add('1,2,3'))

    def test_line_break_support(self):
        self.assertEqual(6, Calculator().Add('1\n2,3'))

    def test_should_fail_line_break_without_num(self):
        with self.assertRaises(ValueError):
            r = Calculator().Add('1,\n')

    def test_support_special_string_def(self):
        self.assertEqual(5, Calculator().Add('//,\n2,3'))
        self.assertEqual(5, Calculator().Add('//;\n2;3'))

    def test_should_fail_negatives_values(self):
        with self.assertRaisesRegex(ValueError, 'negatives not allowed: -1,-5$'):
            r = Calculator().Add('-1,2,-5')        

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
