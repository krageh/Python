nums = [0,1,2,2,3,0,4,2]
# nums = [4, 5]
val = 2

# def ret(nums, val):
#     if not nums:
#         print(nums)

#     elif len(nums) == nums.count(val):
#         if nums[0] == val:
#             nums.clear()
#             print(nums)

#     else:
#         i = 0
#         while i < len(nums):
#             if nums[i] == val:
#                 nums[i], nums[-1] = nums[-1], nums[i]
#                 nums.pop()
#             else:
#                 i += 1

#         print(str(len(nums) - nums.count(val))+',', end=' ')
#         print(nums[:len(nums) - nums.count(val)])
# l = len(nums)
# i = 0
# while i < length:
#     if nums[i] == val:
#         nums.pop(i)
#         length-=1
#         continue
#     i += 1

# print(len(nums))
# print(nums)


# l = len(nums)
# i = 0
# while i < l:
#     if nums[i] == val:
#         nums[i], nums[-1] = nums[-1], nums[i]
#         nums.pop()
#         l -= 1
#     else:
#         i += 1
# print(nums)    

l = len(nums)
i = 0
while i < l:
    if nums[i] == val:
        nums.pop(i)
        l -= 1
    else:
        i += 1
print(nums)



