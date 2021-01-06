n = int(input())
s = [int(x) for x in input().split()]


# indices dictionary - O(n)
order = {}
for i in range(len(s)):
    order[s[i]] = i

if order[n] != 0:
    print('\n' * (order[n] - 1))

last = n
for i in range(n-1):
    if order[n-i-1] > order[last]:
        print(n-i, '', end='\n'*(order[n-i-1]-order[last]))
        last = n-i-1
    else:
        print(n-i, end=' ')
        
print('1')

# # indices dictionary improved (not)
# order = {}
# for i in range(len(s)):
#     order[s[i]] = i

# if order[n] != 0:
#     print('\n' * (order[n] - 1))
# last = n
# for i in range(n-1):
#     if order[n-i] == n:
#         for x in range(i, n-1):
#             print (n-i, end=' ')
#         break
#     elif order[n-i-1] > order[last]:
#         print(n-i, '', end='\n'*(order[n-i-1]-order[last]))
#         last = n-i-1
#     else:
#         print(n-i, end=' ')
    
# print('1')


# # heap w/ O(nlogn)
# import heapq
# hold = []
# for i in s:
#     heapq.heappush(hold, -i)
#     if -1*(hold[0]) == n:
#         while len(hold) != 0 and -1*hold[0] == n:
#             print(n, end=' ')
#             n -= 1
#             heapq.heappop(hold)
#         print()
#     else:
#         print()
