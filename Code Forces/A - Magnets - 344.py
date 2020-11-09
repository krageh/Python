n = int(input())
pos_l = []
x = 1
for i in range(n):
    pos = input()
    pos_l.append(pos)
    if i > 0:
        if pos_l[i][0] == pos_l[i-1][1]:
            x += 1
print(x)
    



