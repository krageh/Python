nums = [3, 2, 1]
nums.sort()

i = 0
l = len(nums)
while i < l:
    if nums.count(nums[i]) > 1:
        nums.pop(i)
        l -= 1
    else:
        i += 1
if len(nums) >= 3:
    print(nums[-3])
else:
    print(nums[-1])