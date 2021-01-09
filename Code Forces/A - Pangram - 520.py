n = int(input())
s = input()

import string
s_lower = s.lower()
l_lower = list(s_lower)
l_iter = l_lower[:]
if n < 26:
    print('NO')

else:
    for i in l_iter:
        if l_lower.count(i) > 1:
            l_lower.remove(i)
    l_lower.sort()
    print('YES' if l_lower == list(string.ascii_lowercase) else 'NO')
