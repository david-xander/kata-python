import re

class StringCalculator:

    ints = None
    delimiter = None
    
    def Add(self, input):
        self.ints = []
        if input == '':
            input = '0'
        elif isinstance(input, str) and input.find('//') == 0:
            self.delimiter = input[2:3]
            input = input[4:]

        self.validate(input)
        for number in self.list_string(input):
            self.ints.append(int(number))
        
        return self.sum()

    def sum(self):
        res = 0
        for number in self.ints:
            res += number
        return res

    def validate(self, input):
        negatives_found = []
        if not isinstance(input, str): raise TypeError
        for number in self.list_string(input):     
            if isinstance(int(number), int):
                if int(number) < 0:
                    negatives_found.append(number)
            else: raise ValueError
        
        if len(negatives_found) > 0:
            cases = ", ".join(negatives_found)
            raise Exception('negatives not allowed: '+cases)

    def list_string(self, input):
        if self.delimiter == None:
            res = re.split(',|\\n', input)
        else:
            res = re.split(',|'+self.delimiter, input)
        return res

if __name__ == '__main__':
    print(StringCalculator().Add('-1,2,-3,4,-5'))
    
