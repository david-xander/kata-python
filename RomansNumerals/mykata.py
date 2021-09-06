from datetime import time


class Number:
    romanLetters = ['M','D','C','L','X','V','I']
    romanLettersValues = [1000,500,100,50,10,5,1]

    def __init__(self, value) -> None:
        self.value = value
        self.onethoudendths = ''
        self.fivehundreths = ''
        self.hundreths = ''
        self.fiftieths = ''
        self.tenths = ''
        self.fifths = ''
        self.ones= ''
    def convertToRoman(self):
        value = self.calcOneThousendths(self.value)
        value = self.calcFiveHundreths(value)
        value = self.calcHundreths(value)
        value = self.calcFiftieths(value)
        value = self.calcTenths(value)
        value = self.calcFifths(value)
        value = self.calcOnes(value)
        return self.onethoudendths+self.fivehundreths+self.hundreths+ \
            self.fiftieths+self.tenths+self.fifths+self.ones

    def calcOnes(self, value):
        if value > 0:
            self.ones = 'I'*value
        return value

    def calcFifths(self, value):
        if value >= 4:
            value = value - 5
            if value == -1:
                self.fifths = 'IV'
            elif value > -1:
                self.fifths = 'V'
        return value

    def calcTenths(self, value):
        times = value // 10
        reminder = value % 10
        value = value - (10*times)
        self.tenths = 'X'*times
        if reminder == 9:
            self.tenths = self.tenths + 'IX'
            value -= 9
        return value

    def calcFiftieths(self, value):
        times = value // 50
        reminder = value % 50
        value = value - (50*times)
        self.fiftieths = 'L'*times
        if reminder == 49:
            self.fiftieths = self.fiftieths + 'IL'
            value -= 49
        return value

    def calcHundreths(self, value):
        times = value // 100
        reminder = value % 100
        value = value - (100*times)
        self.hundreths = 'C'*times
        if reminder == 99:
            self.hundreths = self.hundreths + 'IC'
            value -= 99
        return value

    def calcFiveHundreths(self, value):
        times = value // 500
        reminder = value % 500
        value = value - (500*times)
        self.fivehundreths = 'D'*times
        if reminder == 499:
            self.fivehundreths = self.fivehundreths + 'ID'
            value -= 499
        return value

    def calcOneThousendths(self, value):
        times = value // 1000
        reminder = value % 1000
        value = value - (1000*times)
        self.onethoudendths = 'M'*times
        if reminder == 999:
            self.onethoudendths = self.onethoudendths + 'IM'
            value -= 999
        return value
    
    def getNumber(self, value=None, index = 0):
        res = []
        if value == None:
            value = self.value
        
        roman_number_value = self.romanLettersValues[index]
        roman_number_letter = self.romanLetters[index]
        times = value // roman_number_value
        reminder = value % roman_number_value
        value = value - (roman_number_value*times)
        res.append(roman_number_letter*times)
        if reminder > 0:
            for number in self.romanLettersValues:
                times = value//number
                if number <= roman_number_value and \
                    reminder == roman_number_value-number:
                        res.append(self.romanLettersValues[i]+\
                            roman_number_letter)
                        value -= number
        if value > 0:
            index += 1
            res.append(self.getNumber(value, index))
        
        return ''.join(res)

if __name__ == '__main__':
    print(Number(1912).getNumber())
    
