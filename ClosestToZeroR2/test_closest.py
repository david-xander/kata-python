from closest import ClosestToZero
import unittest

class TestClosest(unittest.TestCase):

    example = [-2,4,1,2,-1,3]
    example_ordered = [-2,-1,1,2,3,4]

    def test_input_is_a_list(self):
        with self.assertRaises(TypeError):
            c = ClosestToZero('nice')

    def test_input_is_all_items_ints(self):
        with self.assertRaises(TypeError):
            c = ClosestToZero([1, 2, 'nice'])
    
    def test_merge_sort_should_return_same_size_input(self):
        c = ClosestToZero(self.example)
        self.assertEqual(len(self.example), len(c.ints))

    def test_merge_sort_should_return_same_items_in_list(self):
        ex = self.example
        c = ClosestToZero(ex)
        for item in c.ints:
            if item in ex:
                ex.pop( ex.index(item) )
            else:
                raise AssertionError

    def test_merge_sort_should_return_all_ordered(self):
        c = ClosestToZero(self.example)
        self.assertEqual(self.example_ordered, c.ints)

    def test_closest_to_zero_val(self):
        c = ClosestToZero([-2,4,1,2,-1,3])
        self.assertEqual(1, c.get_closest())

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
