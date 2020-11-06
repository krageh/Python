# n = int(input("Enter number of games played: "))
 
# s = input("What is the outcome of each game; who won? (insert upper case initial only): ")

# if len(s) != n:
#     print ("That is not the correct number of games.")
# else:
#     for i in s:
#         if i != 'A' and i != 'D':
#             print ('Player not found. Please try again.')
#             break
#         else:
#             if s.count('A') > s.count('D'):
#                 print ('Anton')
#                 break
#             elif s.count('A') < s.count('D'): 
#                 print ('Danik')
#                 break
#             elif s.count('A') == s.count('D'):
#                 print ('Friendship')
#                 break

# Code Forces Submission:
n = int (input ())
s = input ()
if s.count('A') > s.count('D'):
    print ('Anton')
elif s.count('A') < s.count('D'): 
    print ('Danik')
elif s.count('A') == s.count('D'):
    print ('Friendship')
