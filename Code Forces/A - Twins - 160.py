n = int(input())
a = [int(x) for x in input().split()]

a.sort(reverse=True)
a_sum = 0
for i in range(n):
    a_sum += a[i]
    if a_sum > sum(a[i+1:len(a)]):
        break
print(i+1)