from mykata import *
import unittest


class TestMyKata(unittest.TestCase):

    def test_one_is_one(self):
        assert '1' == Number('1').value

    def test_regular_conversion_of_one(self):
        assert 'I' == Number(1).convertToRoman()
    
    def test_regular_conversion_of_two(self):
        assert 'II' == Number(2).convertToRoman()

    def test_regular_conversion_of_three(self):
        assert 'III' == Number(3).convertToRoman()

    def test_regular_conversion_of_four(self):
        assert 'IV' == Number(4).convertToRoman()

    def test_regular_conversion_of_five(self):
        self.assertEqual('V', Number(5).convertToRoman())

    def test_regular_conversion_of_six(self):
        self.assertEqual('VI', Number(6).convertToRoman())

    def test_regular_conversion_of_seven(self):
        self.assertEqual('VII', Number(7).convertToRoman())

    def test_regular_conversion_of_nine(self):
        self.assertEqual('IX', Number(9).convertToRoman())

    def test_regular_conversion_of_ten(self):
        self.assertEqual('X', Number(10).convertToRoman())

    def test_regular_conversion_of_eleven(self):
        self.assertEqual('XI', Number(11).convertToRoman())

    def test_regular_conversion_of_13(self):
        self.assertEqual('XIII', Number(13).convertToRoman())

    def test_regular_conversion_of_14(self):
        self.assertEqual('XIV', Number(14).convertToRoman())

    def test_regular_conversion_of_15(self):
        self.assertEqual('XV', Number(15).convertToRoman())

    def test_regular_conversion_of_18(self):
        self.assertEqual('XVIII', Number(18).convertToRoman())

    def test_regular_conversion_of_19(self):
        self.assertEqual('XIX', Number(19).convertToRoman())

    def test_regular_conversion_of_20(self):
        self.assertEqual('XX', Number(20).convertToRoman())

    def test_regular_conversion_of_21(self):
        self.assertEqual('XXI', Number(21).convertToRoman())

    def test_regular_conversion_of_24(self):
        self.assertEqual('XXIV', Number(24).convertToRoman())

    def test_regular_conversion_of_25(self):
        self.assertEqual('XXV', Number(25).convertToRoman())

    def test_regular_conversion_of_27(self):
        self.assertEqual('XXVII', Number(27).convertToRoman())        

    def test_regular_conversion_of_48(self):
        self.assertEqual('XXXXVIII', Number(48).convertToRoman())  

    def test_regular_conversion_of_49(self):
        self.assertEqual('IL', Number(49).convertToRoman())  

    def test_regular_conversion_of_50(self):
        self.assertEqual('L', Number(50).convertToRoman())  

    def test_regular_conversion_of_51(self):
        self.assertEqual('L', Number(50).convertToRoman()) 

    def test_regular_conversion_of_65(self):
        self.assertEqual('LXV', Number(65).convertToRoman()) 

    def test_regular_conversion_of_79(self):
        self.assertEqual('LXXIX', Number(79).convertToRoman()) 

    def test_regular_conversion_of_99(self):
        self.assertEqual('IC', Number(99).convertToRoman()) 

    def test_regular_conversion_of_100(self):
        self.assertEqual('C', Number(100).convertToRoman()) 

    def test_regular_conversion_of_179(self):
        self.assertEqual('CLXXIX', Number(179).convertToRoman()) 

    def test_regular_conversion_of_200(self):
        self.assertEqual('CC', Number(200).convertToRoman()) 

    def test_regular_conversion_of_500(self):
        self.assertEqual('D', Number(500).convertToRoman()) 

    def test_regular_conversion_of_499(self):
        self.assertEqual('ID', Number(499).convertToRoman()) 

    def test_regular_conversion_of_868(self):
        self.assertEqual('DCCCLXIX', Number(869).convertToRoman()) 

    def test_regular_conversion_of_999(self):
        self.assertEqual('IM', Number(999).convertToRoman()) 

    def test_regular_conversion_of_1000(self):
        self.assertEqual('M', Number(1000).convertToRoman()) 

    def test_regular_conversion_of_2021(self):
        self.assertEqual('MMXXI', Number(2021).getNumber())

    def test_regular_conversion_of_1912(self):
        self.assertEqual('MCMXII', Number(1912).convertToRoman())

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
