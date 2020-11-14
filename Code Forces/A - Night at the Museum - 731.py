name = input()
import string
alph = string.ascii_lowercase

x = 0
if alph.index(name[0]) > 13:
    x = 26 - alph.index(name[0])
else:
    x = alph.index(name[0])

for i in range(1, len(name), 1):
    if abs(alph.index(name[i]) - alph.index(name[i-1])) > 13 and alph.index(name[i-1]) <= 13:
        x += 26 - alph.index(name[i]) + alph.index(name[i-1])
    elif abs(alph.index(name[i]) - alph.index(name[i-1])) > 13 and alph.index(name[i-1]) > 13:
        x += alph.index(name[i]) + 26 - alph.index(name[i-1])
    elif abs(alph.index(name[i]) - alph.index(name[i-1])) <= 13:
        x += abs(alph.index(name[i]) - alph.index(name[i-1]))

print (x)
    
