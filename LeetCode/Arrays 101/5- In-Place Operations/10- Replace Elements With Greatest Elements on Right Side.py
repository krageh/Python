# arr = [17, 18, 5, 4, 6, 1]
arr = [400]
for i in range(len(arr)-1):
    arr[i] = max(arr[i+1:len(arr)])
arr[-1] = -1
print(arr)