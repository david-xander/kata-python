import math

class Hiker:
    ints = []

    def __init__(self, input, *args, **kwargs):
        super(Hiker, self).__init__(*args, **kwargs)
        self.validate(input)
        self.ints = self.merge_sort_input(input)
    
    def validate(self, input):
        if not isinstance(input, list): raise TypeError
        for item in input:
            if not isinstance(item, int): raise ValueError

    def merge_sort_input(self, input):
        items_in_input = len(input)
        half = items_in_input//2
        L = input[0:half]
        R = input[half:]

        if len(L) > 1:
            L = self.merge_sort_input(L)

        if len(R) > 1:
            R = self.merge_sort_input(R)
        
        res = self.merge_input(L,R)
        return res

    def merge_input(self, L, R):
        j = 0
        k = 0
        i = 0
        n = len(L) + len(R)

        res = []
        while i<n:
            if L[j] <= R[k]:
                res.append(L[j])
                if len(L) > j + 1:
                    j += 1
                else:
                    L[j] = math.inf
            else:
                res.append(R[k])
                if len(R) > k + 1:
                    k += 1
                else:
                    R[k] = math.inf              
            i += 1

        return res

    def find_closest_to_zero(self):
        res = math.inf
        for num in self.ints:
            if abs(num) <= abs(res):
                res = num

        return res

if __name__ == '__main__':
    h = Hiker([3,-1,2,1])
    print(h.ints)
    
