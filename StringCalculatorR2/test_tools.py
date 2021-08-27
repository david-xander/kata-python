from logging import addLevelName
from tools import StringCalculator
import unittest


class TestStringCalculator(unittest.TestCase):
    
    def test_empty_string_return_zero(self):
        self.assertEqual(0, StringCalculator().Add(''))
    
    def test_one_return_one(self):
        self.assertEqual(1, StringCalculator().Add('1'))

    def test_two_numbers_return_sum(self):
        self.assertEqual(3, StringCalculator().Add('1,2'))

    def test_using_more_than_two_numbers(self):
        self.assertEqual(6, StringCalculator().Add('1,2,3'))

    def test_handling_new_lines(self):
        self.assertEqual(6, StringCalculator().Add('1\n2,3'))

    def test_single_input_two_separators(self):
        with self.assertRaises(ValueError):
            c = StringCalculator().Add('1,\n')

    def test_support_for_delimite_definition(self):
        self.assertEqual(3, StringCalculator().Add('//;\n1;2'))

    def test_single_input_two_separators(self):
        with self.assertRaisesRegex(ValueError, 'negatives not allowed -1, -3'):
            c = StringCalculator().Add('-1,2,-3')

    def test_numbers_greater_than_1000(self):
        self.assertEqual(2, StringCalculator().Add('1001,2'))

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
