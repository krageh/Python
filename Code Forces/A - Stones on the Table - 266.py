n = int(input())
c = input()
l = list(c)
l_copy = l[:]

for i in range (n-1, 0, -1):
    if l[i] == l[i-1]:
        l_copy.remove(l[i])
    
print(len(l) - len(l_copy))
            

