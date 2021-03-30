class Progression:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance( )
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))

class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current

    def find_value(self, n):
        for j in range(n):
            val = next(self)
        print(val)

FibonacciProgression(2, 2).find_value(8)

# 0  1  1  2  3  5  8  13
# 1  2  3  5  8  13 21 34
# 1  3  4  7  11 18 29 47
# 2  2  4  6  10 16 26 42