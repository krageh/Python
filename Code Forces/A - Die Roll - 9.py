y, w = (int(x) for x in input().split())
d = max(y, w)
if d == 1:
    print('1/1')
else:
    from fractions import Fraction
    print(Fraction(7-d , 6))