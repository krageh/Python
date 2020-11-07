
a, b = (int(x) for x in input().split())

i = 0
while a <= b:
    a = 3 * a
    b = 2 * b
    i += 1

print (i)
