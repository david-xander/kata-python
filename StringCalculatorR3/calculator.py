import re

class Calculator:
    def Add(self, input: str) -> int:
        if input == '':
            return 0
        
        res = 0
        spliting_str = ',|\\n' 
        operands = input  
        if len(input) > 2 and input[:2] == "//":
            spliting_str = input[2:3]
            operands = input[3:]

        numbers = re.split(spliting_str, operands)
        negatives = []
        for number in numbers:
            if not number[:1] == '-':
                res += int(number)
            else:
                negatives.append(number)

        if len(negatives):
            negatives_str = ','.join(negatives)
            raise ValueError('negatives not allowed: ' + negatives_str)


        return res


if __name__ == '__main__':
    r = Calculator().Add('-1,2,-5') 
    print(r)
    
