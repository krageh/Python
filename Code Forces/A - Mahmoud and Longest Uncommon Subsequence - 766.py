s1 = list(input())
s2 = list(input())

if s1 == s2:
    print('-1')

elif len(s1) == len(s2):
    print(len(s1))

else:
    print(max(len(s1), len(s2)))
