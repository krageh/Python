n = int(input())
a = [int(x) for x in input().split()]
m = int(input())

xy = []
for w in range(m):
    xy.append([int(t) for t in input().split()])

for i in range(m):
    if xy[i][0] == 1 and xy[i][0] != n:
        a[xy[i][0]] = a[xy[i][0]] + a[xy[i][0]-1] - xy[i][1]
        a[xy[i][0]-1] = 0
    elif xy[i][0] == n:
        a[xy[i][0]-2] = a[xy[i][0]-2] + xy[i][1] - 1
        a[xy[i][0]-1] = 0
    else:
        a[xy[i][0]-2] = a[xy[i][0]-2] + xy[i][1] - 1
        a[xy[i][0]] = a[xy[i][0]] + a[xy[i][0]-1] - xy[i][1]
        a[xy[i][0]-1] = 0
        

for i in range(n):
    print(a[i])

# Beautiful Matrix input

