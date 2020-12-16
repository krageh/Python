n, x = (int(a) for a in input().split())
dis = 0
for i in range(n):
    s, d = input().split()
    d = int(d)
    if s == '+':
        x += d
    elif s == '-' and d <= x:
        x -= d
    elif s == '-' and d > x:
        dis += 1
print(x, dis)
