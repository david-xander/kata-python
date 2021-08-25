import math

class Hiker:
    
    ints = []
    
    def __init__(self, input, *args, **kwargs):
        super(Hiker, self).__init__(*args, **kwargs)
        self.validate(input)
        self.ints = self.merge_sort(input)

    def closest(self):
        res = math.inf
        for item in self.ints:
            if abs(item) <= abs(res):
                res = item
        return res

    def merge_sort(self, input):
        # divide and conquer part
        n = len(input)
        half = n//2

        L = input[:half]
        R = input[half:]

        if len(L) > 1:
            L = self.merge_sort(L)
        if len(R) > 1:
            R = self.merge_sort(R)

        return self.merge(L, R)

    def merge(self, L, R):
        res = []
        n = len(L) + len(R)
        i = 0
        j = 0
        k = 0
        while i < n:
            if L[j] <= R[k]:
                res.append(L[j])
                if j < len(L)-1:
                    j += 1
                else:
                    L[j] = math.inf
            else:
                res.append(R[k])                
                if k < len(R)-1:
                    k += 1
                else:
                    R[k] = math.inf
            i += 1

        return res


    def validate(self, input):
        if not isinstance(input, list): raise Exception
        for item in input:
            if not isinstance(item, int): raise Exception
        
    

if __name__ == '__main__':
    pass
