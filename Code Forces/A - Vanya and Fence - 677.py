# # Test
# n, h = (int(x) for x in input("Enter number of friends and fence height separated by a space: ").split ())
 
# a = [int(x) for x in input("Enter their heights separated by spaces: ").split()]
 
# for i in range(n):
#     if a[i] > h:
#         a[i] = 2
#     else:
#         a[i] = 1
 
# print (sum(a))

# Code Forces
n, h = (int (x) for x in input ().split ())
 
a = [int (x) for x in input ().split ()]
 
for i in range (n):
    if a[i] > h:
        a[i] = 2
    else:
        a[i] = 1
 
print (sum(a))