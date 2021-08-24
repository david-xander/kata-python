import math

class ClosestToZero:

    ints = []

    def __init__(self, input, *args, **kwargs):
        super(ClosestToZero, self).__init__(*args, **kwargs)
        
        self.validate(input)
        self.ints = self.merge_sort(input)

    def get_closest(self):
        res = math.inf
        for item in self.ints:
            if abs(item) <= abs(res):
                res = item
        
        return res

    def merge_sort(self, input):
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
        while i<n:
            if L[j] <= R[k]:
                res.append(L[j])
                if j < len(L)-1:
                    j += 1
                else:
                    # como hemos avanzado todo L
                    # solo debemos añadir de R en el orden
                    # en que está, que será correcto, porque
                    # L y R ya vienen ordenados
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
        if not isinstance(input, list): raise TypeError
        for item in input:
            if not isinstance(item, int): raise TypeError


if __name__ == '__main__':
    c = ClosestToZero([-2,4,1,2,-1,3])
    print(c.ints)
    
