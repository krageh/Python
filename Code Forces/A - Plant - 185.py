n = int(input())

u1 = pow(2, n-1, 1000000007)
u2 = pow(2, 2*n-1, 1000000007)
print(int((u1+u2)%1000000007))

