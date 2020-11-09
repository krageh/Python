name = input()
l_name = list(name)
s_name = l_name[:]

# for x in s_name:
#     if l_name.count(x) > 1:
#         l_name.remove(x)

# if len(l_name) %2 == 0:
#     print("CHAT WITH HER!")
# else:
#     print("IGNORE HIM!")
    
for x in name:
    if l_name.count(x) > 1:
        l_name.remove(x)

if len(l_name) %2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")