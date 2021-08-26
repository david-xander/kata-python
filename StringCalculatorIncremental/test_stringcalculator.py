from stringtools import StringCalculator
import unittest


class TestStringCalculator(unittest.TestCase):

    def test_should_fail_not_string(self):
        with self.assertRaises(TypeError):
            sc = StringCalculator().Add(12)

    def test_should_fail_not_string_in_string(self):
        with self.assertRaises(ValueError):
            sc = StringCalculator().Add('doce')

    def test_should_return_zero_empty_string(self):
        self.assertEqual(0, StringCalculator().Add(''))

    def test_sum_should_return_same_number_when_single(self):
        self.assertEqual(1, StringCalculator().Add('1'))
    
    def test_sum_two_numbers(self):
        self.assertEqual(3, StringCalculator().Add('1,2'))

    def test_sum_with_blank_numbers_should_fail(self):
        with self.assertRaises(ValueError):
            sc = StringCalculator().Add('1,,3')

    def test_support_adding_support_for_new_line_separator(self):
        self.assertEqual(6, StringCalculator().Add('1\n2,3'))

    def test_support_new_optional_string_definition_current_avaliable_delimiters(self):
        self.assertEqual(3, StringCalculator().Add('//,\n1,2'))

    def test_support_new_optional_string_definition_any_delimiter(self):
        self.assertEqual(3, StringCalculator().Add('//;\n1;2'))

    def test_should_throw_exception_with_negative_ints(self):
        with self.assertRaisesRegex(Exception, "negatives not allowed: -1, -3, -5$"):
            sc = StringCalculator().Add('-1,2,-3,4,-5')
       

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
