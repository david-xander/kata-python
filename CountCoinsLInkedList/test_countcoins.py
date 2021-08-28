from changelib import ChangeUS
import unittest


class TestChangeUS(unittest.TestCase):

    def test_change_of_one_cent(self):
        p = ChangeUS(1)
        self.assertEqual('1P', p.Change())
    
    def test_change_of_two_cent(self):
        p = ChangeUS(2)
        self.assertEqual('2P', p.Change())
    
    def test_change_of_three_cents(self):
        p = ChangeUS(3)
        self.assertEqual('3P', p.Change())

    def test_change_of_five_cents(self):
        p = ChangeUS(5)
        self.assertEqual('1N', p.Change())    

    def test_change_of_seven_cents(self):
        p = ChangeUS(7)
        self.assertEqual('1N, 2P', p.Change())    

    def test_change_of_twelve_cents(self):
        p = ChangeUS(12)
        self.assertEqual('1D, 2P', p.Change())  

    def test_change_of_39_cents(self):
        p = ChangeUS(39)
        self.assertEqual('1Q, 1D, 4P', p.Change())

    def test_change_of_86_cents(self):
        p = ChangeUS(86)
        self.assertEqual('3Q, 1D, 1P', p.Change())  

    def test_change_of_98_cents(self):
        p = ChangeUS(98)
        self.assertEqual('3Q, 2D, 3P', p.Change())  

    def test_change_of_100_cents(self):
        p = ChangeUS(100)
        self.assertEqual('4Q', p.Change()) 

    def test_change_of_30_cents(self):
        p = ChangeUS(30)
        self.assertEqual('Q, 1N', p.Change()) 

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
