s = input()
s_l = list(s)
for x in s:
    if x == '+':
        s_l.remove(x)
s_l.sort()
# i = 1
# while len(s_l) < len(s):
#     s_l.insert(i, '+')
#     i += 2
# print(*s_l, sep='+')

print('+'.join(s_l))