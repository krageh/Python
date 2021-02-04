# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums = [1, 1, 2]

l = len(nums)
i = 0
while i < l:
    if nums.count(nums[i]) > 1:
        nums.pop(i)
        l -= 1
    else:
        i += 1
print(l)