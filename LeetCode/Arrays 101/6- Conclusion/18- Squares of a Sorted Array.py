nums = [-4,-1,0,3,10]
for i in range(len(nums)):
    nums[i] = pow(nums[i], 2)
nums.sort()
print(nums)

# compare operations

def square(n):
    return n*n

result = list(map(square, nums))
result.sort()
print(result)