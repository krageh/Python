s = input().split()
l = s[:]
n = 0
for x in s:
    if l.count(x) > 1:
        l.remove(x)
        n += 1
print(n)
