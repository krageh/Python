class Vector():
    def __init__(self, d):
        self._coords = [0]*d

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
            newVector[j] = self[j]*-1
        return newVector

a = Vector(5)
for i in range(5):
    a[i] = i
print(-a)
