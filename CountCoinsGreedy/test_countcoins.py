from changelib import ChangeUS
import unittest


class TestChangeUS(unittest.TestCase):

    def test_change_of_one_cent(self):
        p = ChangeUS(1)
        self.assertEqual('1P', p.Change())
    
    def test_change_of_two_cent(self):
        p = ChangeUS(2)
        self.assertEqual('2P', p.Change())
    
    def test_change_of_three_cent(self):
        p = ChangeUS(3)
        self.assertEqual('3P', p.Change())

    def test_change_of_five_cent(self):
        p = ChangeUS(5)
        self.assertEqual('1N', p.Change())    


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
