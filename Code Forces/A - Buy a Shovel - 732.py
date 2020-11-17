k, r = (int (x) for x in input().split())
d = 10
# if k % d == 0:
#     n = k/d
#     print(int(n))
# if k == r:
#     n = k/r
#     print(int(n))

# else:
n = 1
while n*k % d != 0:
    n += 1

for m in range(1, n+1):
    if (((m * k)-r) % d == 0) and (((m * k)-r) / d >= 0):
        break
    
if n < m:
    print(n)
else:
    print(m)
