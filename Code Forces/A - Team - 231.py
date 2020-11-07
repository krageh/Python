n = int(input())
# sol = [([int(x) for x in input().split()],) * n]
y = 0
for i in range(n):
    Row = (int(x) for x in input().split())
    if sum(Row) >=2:
        y += 1

print (y)
