
# a = input()
# b = input()
# # a = a.lower()
# # b = b.lower()
# a = a.upper()
# b = b.upper()
# if a < b:
#     print ('-1')
# elif a > b:
#     print('1')
# else:
#     print(0)


a = input()
b = input()
a = a.casefold()
b = b.casefold()
if a < b:
    print ('-1')
elif a > b:
    print('1')
else:
    print(0)

# help(str.isalpha)
# help(str.lower)