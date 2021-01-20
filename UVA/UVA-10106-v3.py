while True:
    try:
        x = int(input())
        y = int(input())
        print(x*y)
    except:
        break

# while True:
#     x = int(input())
#     y = int(input())
#     if type(x) == int and type(y) == int:
#         print(x*y)
#     else:
#         break

# def add(add1, add2):
#     e_m_reset = ''
#     c_add = 0
#     counter = 0
#     for i_add in range(min(len(add2), len(add1))):
#         counter += 1
#         m_add = str(int(add2[i_add]) + int(add1[i_add]) + c_add)
#         if len(m_add) == 2:
#             c_add = int(m_add[0])
#             m2_add = m_add[1]
#             e_m_reset += m2_add
#         else:
#             e_m_reset += m_add
#             c_add = 0
#     if len(add2) != counter:
#         for i_rem in range(len(add2) - counter):
#             m3_add = str(int(add2[counter+i_rem]) + c_add)
#             if len(m3_add) == 2:
#                 c_add = int(m3_add[0])
#                 m4_add = m3_add[1]
#                 e_m_reset += m4_add
#             else:
#                 e_m_reset += m3_add
#                 c_add = 0
#     if len(add1) != counter:
#         for i_rem in range(len(add1) - counter):
#             m3_add = str(int(add1[counter+i_rem]) + c_add)
#             if len(m3_add) == 2:
#                 c_add = int(m3_add[0])
#                 m4_add = m3_add[1]
#                 e_m_reset += m4_add
#             else:
#                 e_m_reset += m3_add
#                 c_add = 0
#     if c_add != 0:
#         e_m_reset += str(c_add)
                
#     return e_m_reset

# while True:
#     n1_inp = input()
#     n2_inp = input()

#     det = 0
#     dig = '0123456789'
#     if not n1_inp or not n2_inp:
#         break

#     for num in n1_inp:
#         if num not in dig:
#             det += 1
#             break
#     if det > 0:
#         break
#     for num in n2_inp:
#         if num not in dig:
#             det += 1
#             break
#     if det > 0:
#         break


#     if n1_inp == '0' or n2_inp == '0':
#         print('0')

#     else:
#         for l in range(len(n1_inp)):
#             if n1_inp[l] != '0':
#                 if l == 0:
#                     n1 = n1_inp
#                 break
#             else:
#                 n1 = n1_inp[l+1:]
#         for l in range(len(n2_inp)):
#             if n2_inp[l] != '0':
#                 if l == 0:
#                     n2 = n2_inp
#                 break
#             else:
#                 n2 = n2_inp[l+1:]



#         if n1 == '1':
#             print(n2)

#         elif n2 == '1':
#             print(n1)
#         # e_m_s = ''

#         else:
#             e_m_add = ''
#             for j in range(len(n2), 0, -1):
#                 c = 0
#                 e_m = '0'*(len(n2)-j)
#                 for i in range(len(n1), 0, -1):
#                     m = str(int(n1[i-1]) * int(n2[j-1]) + c)
#                     if len(m) == 2:
#                         c = int(m[0])
#                         m2 = m[1]
#                         e_m = m2 + e_m
#                     else:
#                         e_m = m + e_m
#                         c = 0
#                 if c != 0:
#                     e_m = str(c) + e_m
#                 if len(e_m_add) != 0:
#                     e_m_s = add(''.join(reversed(e_m)), e_m_add)
#                     e_m_add = e_m_s
#                 else:
#                     e_m_add = ''.join(reversed(e_m))
#             print(''.join(reversed(e_m_add)))