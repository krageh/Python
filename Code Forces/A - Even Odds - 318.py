n, k = (int(x) for x in input().split())
# reorder = []
# even = []
# for num in range(1, n+1):
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         reorder.append(num)
# reorder.extend(even)
# print(reorder[k-1])
# reorder = list(range(1, n+1))

if n % 2 == 0:
    if k > n//2:
        print((k - n//2) * 2)
    else:
        print(k * 2 - 1)

else:
    if k > (n//2) + 1:
        print((k - n//2 - 1) * 2)
    else:
        print(k * 2 - 1)
