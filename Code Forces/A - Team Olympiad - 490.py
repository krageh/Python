# lists
n = int(input())
t = input().split()
# t_ = t[:]
# e1 = []
# e2 = []
# e3 = []

# if t.count('1') == 0 or t.count('2') == 0 or t.count('3') == 0:
#     print('0')
# else:
#     print(min(t.count('1'), t.count('2'), t.count('3')))
#     for i in range(len(t)):
#         if t[i] == '1':
#             e1.append(i+1)
#             t[i] = '_'
#         elif t[i] == '2':
#             e2.append(i+1)
#             t[i] = '_'
#         elif t[i] == '3':
#             e3.append(i+1)
#             t[i] = '_'
#     for x in range(min(t_.count('1'), t_.count('2'), t_.count('3'))):
#         print(e1[x], e2[x], e3[x])

# # dictionaries
# t = [int(x) for x in input().split()]
# talents = {1:[], 2:[], 3:[]}

# for i in range(len(t)):
#     talents.get(t[i]).append(i+1)

# num_teams = min(len(talents[1]), len(talents[2]), len(talents[3]))
# print(num_teams)
# if num_teams != 0:
#     for i in range(num_teams):
#         print(talents[1][i], talents[2][i], talents[3][i])

talents = {'1':[], '2':[], '3':[]}

for i in range(len(t)):
    talents.get(t[i]).append(i+1)

num_teams = min(len(talents['1']), len(talents['2']), len(talents['3']))
print(num_teams)
if num_teams != 0:
    for i in range(num_teams):
        print(talents['1'][i], talents['2'][i], talents['3'][i])


