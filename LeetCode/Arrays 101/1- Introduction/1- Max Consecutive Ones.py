nums = [1, 1, 0, 1, 1, 1]
# c1 = 0
# c2 = 0
# if nums[0] == 1:
#     c1 += 1
# for i in range(1, len(nums)):
#     if nums[i] == 1:
#         c1 += 1
#     elif nums[i] == 0:
#         if c1 > c2:
#             c2 = c1
#         c1 = 0
# if c1 > c2:
#     c2 = c1
# print(c2)

c1 = 0
c2 = 0

for i in range(len(nums)):
    if nums[i] == 1:
        c1 += 1
    elif nums[i] == 0:
        c2 = max(c1, c2)
        c1 = 0
print(max(c1, c2))