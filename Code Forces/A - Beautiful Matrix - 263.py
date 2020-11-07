# # Code Forces
# # a = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# a = [[int(x) for x in input().split()], [int(x) for x in input().split()], [int(x) for x in input().split()], [int(x) for x in input().split()], [int(x) for x in input().split()]]
a = [input().split(), input().split(), input().split(), input().split(), input().split()]
# # print (len(a[0]))

# r = []
# for i in range(5):
#     r.append(input().split())
#     print(r)
#     if r[j] == '1':
       
    

x = 0
while x in range(len(a)):
    print(len(a[0]))
    for i in range (len(a[0])):
        if a[x][i] == '1':
            break
    if a[x][i] == '1':
        break
    else:
        x += 1

print (abs(x-2) + abs(i-2))


