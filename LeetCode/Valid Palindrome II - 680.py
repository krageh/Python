import timeit
start = timeit.timeit()
# s = input()
# s = list(s)
# # r = s[len(s)::-1]
# r = s[::-1]
# i = 0
# if r == s:
#     print(r == s)
# else:
#     for x in range(len(s)):
#         s_m = s[:x]+s[x+1:]
#         # s_m.remove(x)
#         r = s_m[::-1]
#         if r == s_m:
#             i += 1
#     if i == 0:
#         print(False)
#     else:
#         print(True)
# def pal(s):
#     # s = input()
#     s = list(s)
#     # r = s[:]
#     # r.reverse()
#     # i = 0
#     if s == s[-1:0:-1]:
#         return(True)
#     else:
#         for x in range(len(s)):
#             # s_m = s[:x] + s[x+1:]
#             # r_m = s_m[:]
#             # r_m.reverse()
#             # if s_m == sorted(s_m, reverse=True):
#                 # i += 1
#                 # return(True)
            
#             if x == len(s) and s[:x] == s[x-1:0:-1] + s[0:1]:
#                 return True
#             elif x == len(s)-1 and s[:x] + s[x+1:x] == s[x+1:x] + s[x-1:0:-1] + s[0:1]:
#                 return True
#             elif x > 1 and s[:x] + s[x+1:] == s[-1:x:-1] + s[x-1:0:-1] + s[0:1]:
#                 return True
#             elif x == 0 and s[x+1:] == s[-1:x:-1]:
#                 return True
#             elif x == 1 and s[:x] + s[x+1:] == s[-1:x:-1] + s[0:1]:
#                 return True
        
#         return(False)

# s = input()
# print(pal(s))
# end = timeit.timeit()
# print(end)

s = list(input())
# def isPalindrome(s):
#     x = 0
#     if s == s[::-1]:
#         return True
#     else:
#         flag = True
#         for i in range(len(s)):
#             l = s[::-1]
#             del(l[i])
#             if l == l[::-1]:
#                 x +=1
#         if x == 0:
#             flag = False
#         return flag
# print(isPalindrome(s))

def isPalindrome(s):
    if s == s[::-1] or len(s) <= 1:
        return True
    else:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1  
            else:   
                if s[i+1] != s[j] and s[i] != s[j-1]:
                    return False
                if s[i+1] == s[j]:
                    if branch_i(i+1, j):
                        break
                if s[i] != s[j-1]:
                    return False
                if s[i] == s[j-1]:
                    if not branch_j(i, j-1):
                        return False
                    else:
                        break
            return True

def branch_i(i, j):
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True
            

def branch_j(i, j):
    # c2 = 1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            # c1 += 1
            # c2 -= 1
            return False
    return True
            



# def isPalindrome(s):
#     if s == s[::-1] or len(s) <= 1:
#         return True
#     else:
#         i = 0
#         j = len(s) - 1
#         while i <= j:
#             if s[i] == s[j]:
#                 i += 1
#                 j -= 1
#             else:
#                 break
            
#         if s[i+1] != s[j] and s[i] != s[j-1]:
#                 return False

#         if s[i+1] == s[j]:
#                 if branch_i(i+1, j):
#                     return True

#         if s[i] != s[j-1]:
#             return False

#         if s[i] == s[j-1]:
#                 if not branch_j(i, j-1):
#                     return False
    
#         return True

# def branch_i(i, j):
#     while i < j:
#         if s[i] == s[j]:
#             i += 1
#             j -= 1
#         else:
#             return False
#     return True
            

# def branch_j(i, j):

#     while i < j:
#         if s[i] == s[j]:
#             i += 1
#             j -= 1
#         else:
#             return False
#     return True

print(isPalindrome(s))
end = timeit.timeit()
print(end)