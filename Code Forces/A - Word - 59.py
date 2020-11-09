s = input()
i = 0
for x in s:
    if (x.islower()):
        i += 1
if i < len(s)-i:
    s = s.upper()
else:
    s = s.lower()
print(s)