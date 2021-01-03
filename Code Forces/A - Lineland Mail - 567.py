n = input()
x = [int(x) for x in input().split()]

# for location in x:
#     if location == x[0]:
#         cost_min = abs(location - x[1])
#         cost_max = abs(location - x[-1])
#     elif location == x[-1]:
#         cost_min = abs(location - x[-2])
#         cost_max = abs(location - x[0])
#     else:
#         cost_min = min(abs(location - x[x.index(location)-1]), abs(location - x[x.index(location)+1]))
#         cost_max = max(abs(location - x[0]), abs(location - x[-1]))
#     print(cost_min, cost_max)

for i in range(len(x)):
    if i == 0:
        cost_min = abs(x[i] - x[1])
        cost_max = abs(x[i] - x[-1])
    elif i == len(x)-1:
        cost_min = abs(x[i] - x[-2])
        cost_max = abs(x[i] - x[0])
    else:
        cost_min = min(abs(x[i] - x[i-1]), abs(x[i] - x[i+1]))
        cost_max = max(abs(x[i] - x[0]), abs(x[i] - x[-1]))
    print(cost_min, cost_max)