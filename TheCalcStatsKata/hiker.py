class Hiker:
    input = []
    PRECISSION = 6

    def __init__(self, entrada, *args, **kwargs):
        super(Hiker, self).__init__(*args, **kwargs)
        self.validate(entrada)
        self.input = entrada
        
    def validate(self, entrada):
        if not len(entrada) >= 1: raise ValueError
        if not isinstance(entrada, list): raise TypeError
        for num in entrada:
            if not isinstance(num, int): raise TypeError
    
    def minimum(self):
        res = self.input[0]
        for num in self.input:
            if num<res: res = num
        
        return res

    def maximum(self):
        res = self.input[0]
        for num in self.input:
            if num>res: res = num
        
        return res

    def number_of_elements(self):
        return len(self.input)
    
    def average(self):
        res = 0
        for num in self.input:
            res += num
        
        return round(res/self.number_of_elements(), self.PRECISSION)