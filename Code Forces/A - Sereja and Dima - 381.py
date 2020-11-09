n = int(input())
c = [int(x) for x in input().split()]
s = []
d = []
for i in range(n):
    s.append(max(c[0],c[-1]))
    c.remove(s[i])
    if len(c) < 1:
        break
    d.append(max(c[0],c[-1]))
    c.remove(d[i])
    if len(c) < 1:
        break

score = [sum(s), sum(d)]
print(*score, sep=' ')