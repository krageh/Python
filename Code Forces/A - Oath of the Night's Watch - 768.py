n = int(input())
s = [int(x) for x in input().split()]

# count = 0
# for strength in s:
#     if strength != min(s) and strength != max(s):
#         count += 1

# print(count)

count = n - s.count(min(s)) - s.count(max(s))
if count < 0:
    print('0')
else:
    print(count)