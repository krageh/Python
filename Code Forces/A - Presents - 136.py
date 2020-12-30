n = int(input())
i = [int(x) for x in input().split()]

p = [0]*n
for e in i:
    p[e-1] = i.index(e)+1

# print(*p, sep=' ')