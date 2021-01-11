dir = input()
sequence = input()
keys = ['qwertyuiop', 'asdfghjkl;', 'zxcvbnm,./']
for x in range(len(keys)):
    keys[x] = list(keys[x])
    
x = -1 if dir == 'R' else 1
for char in sequence:
    for row in range(len(keys)):
        if char in keys[row]:
            break
    print(keys[row][keys[row].index(char)+x], end='')
