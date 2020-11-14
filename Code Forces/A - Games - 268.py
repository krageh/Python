n = int(input())
h_a_l = []

for i in range(n):
    h, a = input().split()
    h_a_l.append((h, a))

x = 0
for i in range(n):
    for j in range(n):
        if h_a_l[i][0] == h_a_l[j][1]:
         x += 1

print(x)



