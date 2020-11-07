# # using loops w/ list (too imperative)
# n = int(input())
# a = [int(x) for x in input().split()]

# while True: 
#     for i in range(n-1, 0, -1):
#         if a[i] < a[i-1]:
#             x = (a[i-1] - a[i])
#             a[i] = a[i] + x
#             a[i-1] = a[i-1] - x
#     y = 0
#     for i in range(n-1, 0, -1):
#         if a[i] >= a[i-1]:
#             y += 1
#     if y == n-1:
#         break

# print (*a, sep=" ")


# # using .sort() w/ list (most efficient)
# n = int(input())
# a = [int(x) for x in input().split()]
# a.sort()
# print (*a, sep=" ")


# # converting to string
# n = int(input())
# a = [int(x) for x in input().split()]
# a.sort()
# for x in range(len(a)):
#     a[x] = str(a[x])
# print(' '.join(a))


# # constructing string
# n = int(input())
# a_str = ""
# a = [int(x) for x in input().split()]
# a.sort()
# for x in range(len(a)):
#     a_str = a_str + str(a[x])
# print(*a, sep=" ")


# # constructing tuple
# n = int(input())
# a = ()
# b = [int(x) for x in input().split()]
# b.sort()
# for i in range(len(b)):
#     a = a + (b[i],)

# print (*a, sep=" ")

# # using function w/ tuple

