s = input()
s_l = list(s)
# for x in range(len(s)):
#     s_l[x] = s[x].strip()
s_l_c = s_l[:]
for x in s_l_c:
    if s_l.count(x) > 1 or x == ',' or x == ' ':
        s_l.remove(x)
print(len(s_l)-2)

