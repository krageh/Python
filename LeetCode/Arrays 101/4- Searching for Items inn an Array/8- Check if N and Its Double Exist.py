# arr = [10, 2, 5, 3]
# arr = [7, 1, 14, 11]
# arr = [3, 1, 7, 11]
arr = []
c = 0
for i in range(len(arr) - 1):
    if arr[i]*2 in arr[i+1 : len(arr)] or arr[i]/2 in arr[i+1 : len(arr)]:
        c += 1
print(True if c > 0 else False)
        