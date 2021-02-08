nums = [4, 3, 2, 7, 8, 2, 3, 1]
# 1 2 2 3 3 4 7 8
# nums = [1, 1, 2, 4]
# nums = [1, 1]
# [ 1, 1, 3, 4]
# nums.sort()
# missing = []
# if len(nums) > 0:
#     if nums[0] != 1:
#         for k in range(1, nums[0]):
#             missing.append(k)
    
#     for i in range(1, len(nums)):
#         if nums[i] - nums[i-1] > 1:
#             for j in range(1, nums[i]-nums[i-1]):
#                 missing.append(nums[i-1]+j)

#     if len(nums) > nums[-1]:
#         for j in range(1, len(nums) - nums[-1] + 1):
#             missing.append(nums[-1]+j)
    
# print(missing)

print(list(set(range(1, len(nums)+1))-set(nums)))