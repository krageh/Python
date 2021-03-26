import collections.abc
class Vector():
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0]*d
        elif isinstance(d, collections.abc.Iterable):
            self._coords = d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val
    
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must agree.')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

    def __neg__(self):
        newVector = Vector(len(self))
        for j in range(len(self)):
            newVector[j] = self[j] * -1
        return newVector

    def __mul__(self, other):       
        mulVector = Vector(len(self))
        if isinstance(other, (int, float)):
            for j in range(len(self)):
                mulVector[j] = self[j] * other
        elif len(self) != len(other):
            raise ValueError('Dimensions must agree.')
        else:
            for j in range(len(self)):
                mulVector[j] = self[j] * other[j]
        return mulVector

    def __rmul__(self, val):
        return self * val

# a = Vector(5)
a = Vector([1, 2, 3, 4])
print(a)
