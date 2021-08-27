import re

class StringCalculator:
    
    def Add(self, input):
        if input == '':
            return 0

        if input.find('//') == 0 or len(re.split(',|\\n', input)) >= 2:
            numbers=[]
            if input.find('//') == 0:
                delimiter = input[2]
                numbers = input[4:].split(delimiter)
            else:
                numbers=re.split(',|\\n', input)

            res = 0
            for number in self.validate(numbers):
                num = int(number)
                if num > 1000:
                    num=0
                res += num
            return res
        else:
            return int(input)
    
    def validate(self, nums):
        error = []
        for num in nums:
            if num.find('-') == 0:
                error.append(num)
        if len(error) > 0:
            raise ValueError('negatives not allowed '+', '.join(error))

        return nums


if __name__ == '__main__':
    pass
    
