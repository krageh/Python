n = int(input())
e = [int(x) for x in input().split()]
e_c = e[:]

x = 0
for i in range (len(e)):
    if e[i] > 0:
        x += e[i]
        e_c.pop()
    elif e[i] < 0:
        if x >= 1:
            x -=1
            e_c.pop()

print (len(e_c))
