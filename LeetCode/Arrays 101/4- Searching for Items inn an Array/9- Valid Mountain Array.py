arr = [0, 2, 3, 4, 5, 2, 1, 0]
# arr = [0, 2, 3, 3, 5, 2, 1, 0]
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr = [0, 3, 2, 1]


# i = 1
# flag = False
# if len(arr) > 2:
#     while i in range(1, len(arr)) and arr[i] > arr[i-1]:
#         i += 1
#     while i in range(i, len(arr)) and arr[i] < arr[i-1]:
#         i += 1
#     if i == len(arr) and arr[0] < arr[1] and arr[i-1] < arr[i-2]:
#         flag = True

# print(flag)


# i = 1
# if len(arr) > 2:
#     while i in range(1, len(arr)) and arr[i] > arr[i-1]:
#         i += 1
#     if i == 1 or i == len(arr):
#         return (False)
#     while i in range(i, len(arr)) and arr[i] < arr[i-1]:
#         i += 1

#     return i == len(arr)

x = arr.index(max(arr))
flag = True
if len(arr) < 3 or x == 0 or x == len(arr) -1:
    flag = False
for i in range(1, x+1):
    if arr[i] <= arr[i-1]:
        flag = False
for i in range(x+1, len(arr)):
    if arr[i] >= arr[i-1]:
        flag = False

# x = arr.index(max(arr))
# flag = True
# if len(arr) < 3 or x == 0 or x == len(arr) -1:
#     flag = False
# for i in range(1, len(arr)):
#     if arr[i] <= arr[i-1]:
#         break
# for j in range(len(arr) - 1, 0, -1):
#     if arr[j] >= arr[j-1]:
#         break
# print(i==j+1)