s = input()
t = input()
s_l = list(s)

n = 0
c = 0
for i in s_l[:len(s) - 1]:
    for c in range(c, len(t)):
        if t[c] == i:
            n += 1
            break
    c += 1
    if c == len(t):
        break

print(n+1)