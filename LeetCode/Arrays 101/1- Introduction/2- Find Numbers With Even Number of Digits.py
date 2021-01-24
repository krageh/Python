nums = [12, 345, 2, 6, 7896]
c = 0
for d in nums:
    if len(str(d))%2 == 0:
        c += 1
print(c)