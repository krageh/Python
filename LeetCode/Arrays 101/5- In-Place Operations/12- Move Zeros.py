# nums = [1, 0, 1, 0, 0, 3, 12, 0] # [1, 0, 0, 3, 12] # [1, 3, 0, 0, 12] #[1, 3, 12, 0, 0]
nums = [1, 2, 1]
# i = 0 if nums[0] == 0 else 1
# while i < len(nums)-1:
#     if nums[i] == 0:
#         for j in range(i+1, len(nums)):
#             if nums[j] != 0:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 break
#     i += 1
# print(nums)

# l = len(nums)
# i = 0
# while i < l:
#     if nums[i] == 0:
#         nums.pop(i)
#         nums.append(0)
#         l -= 1
#     else:
#         i += 1
# print(nums)

i = 0
for j in range(len(nums)):
    if nums[j] != 0:
        nums[i] = nums[j]
        i += 1
for k in range(i+1, len(nums)):
    nums[k] = 0
print(nums)