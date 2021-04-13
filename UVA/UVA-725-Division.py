import random
# n = 'start'
# while n != 0:
#     n = int(input())
#     ch = [k for k in range(10)]
#     d_l = [None]*5
#     for i in range(5):
#         d_l[i] = random.choice(ch)
#         ch.remove(d_l[i])


# def get_permutations(sequence):
#     import math
#     l = list(sequence)
#     perm_list = []
    
#     if len(sequence) == 1:
#         return(l)
    
#     else:
#         iter_list = get_permutations(sequence[1:len(sequence)])
#         for list_comb in range(math.factorial(len(l)-1)):
#             for i in range(len(l)):
#                 perm_list.append(mutate_get_permutations(iter_list, list_comb, i, l))
#         return(perm_list)
    
# def mutate_get_permutations(m, comb, i, l):
#     import copy
#     if len(m) == 1:
#         m_m = copy.deepcopy(m)
#         m_m.insert(i, l[0])
#     else:
#         m_m = copy.deepcopy(m[comb])
#         m_m.insert(i, l[0])
#     # if len(m_m) == x:
#     #     m_m = ''.join(m_m)
#     return(m_m)

# def el_to_str(perms):
#     l = perms[:]
#     for i in range(len(l)):
#         l[i] = ''.join(l[i])
#     # for el in l:
#     #     print(''.join(s for s in el), end=' ')
#     print(l)


# def PuzzleSolve(k, S, U):
#     # den = []
#     for e in U:
#         S.append(e)
#         U.remove(e)
#         # c = S
#         if k == 1:
#             den.append(S)
#             return den
#         else:
#             den.append(PuzzleSolve(k - 1, S, U))
#         i = S.pop()
#         U.append(i)
#         U.sort()
#     return den

# den = []
# print(PuzzleSolve(2, [], [0, 1, 2, 3]))


# N = int(input())
# while N != 0:
#     import itertools
#     # den = [k for k in range(10)]
#     den = list(itertools.permutations([k for k in range(10)], 5))
#     den_int = den[:]
#     # print(den)

#     for i in range(len(den)):
#         den_int[i] = (''.join([str(j) for j in den[i]]))

#     nom_prosp = []
#     c1 = 0
#     # Use Bisection method to optimize where to start loop
#     low = 0
#     high = len(den_int) - 1
#     while low < high:
#         target_start = (low + high) // 2
#         a, b = divmod(int(den_int[target_start]), N)
#         if b != 0: low += 1
#         else:
#             if len(str(a)) >= 4:
#                 high = target_start - 1
#             elif len(str(a)) < 4:
#                 low = target_start + 1

#     for i in range(target_start, len(den)):
#         quot, rem = divmod(int(den_int[i]), N)
#         if rem == 0: #and len(str(quot)) in range (4, 6):
#             if len(str(quot)) == 4: x = '0' + str(quot)
#             else: x = str(quot)
#             x_set = set(x)
#             if len(x) == len(x_set):
#                 c2 = 0
# # try set to check for uniqueness
#                 unique_check = set(str(den_int[i]) + x)
#                 if len(unique_check) == 10:
#                     c1 += 1
#                     print(f'{den_int[i]} / {x} = {N}')
#                 else:
#                     continue
# # loop to check for uniqueness
#                 # for ch in str(den_int[i]):
#                 #     if ch in x:
#                 #         break
#                 #     else:
#                 #         c2 += 1
#                 #         if c2 == 5:
#                 #             print(f'{den_int[i]} / {x} = {N}')
#                 #             c1 += 1
#     # if c1 == 0: print('There are no solutions for {N}.'.format(N = N))
#     if c1 == 0: print(f'There are no solutions for {N}.')
#     N = int(input())


# # minimize cast and iter
# import itertools
# den = list(itertools.permutations([k for k in range(10)], 5))
# N = int(input())
# while N != 0:
#     c1 = 0
#     # use Bisection method to optimize where to start loop
#     low = 0
#     high = len(den) - 1
#     while low < high:
#         target_start = (low + high) // 2
#         a, b = divmod(int(''.join([str(j) for j in den[target_start]])), N)  # cast element to int
#         # if b != 0: low += 1
#         # else:
#         # if len(str(a)) >= 4:
#         if a >= 1000:
#             high = target_start - 1
#         # elif len(str(a)) < 4:
#         elif a < 1000:
#             low = target_start + 1

#     # if target_start > (len(den) - 1) // 2:
#     for i in range(target_start, len(den)):
#         den_str = (''.join([str(k) for k in den[i]]))
#         den_int = int(den_str)
#         quot, rem = divmod(den_int, N)
#         if rem == 0: #and len(str(quot)) in range (4, 6):
#             if len(str(quot)) == 4: x = '0' + str(quot)
#             else: x = str(quot)
#             x_set = set(x)
#             if len(x) == len(x_set):
#                 c2 = 0
# # try set to check for uniqueness
#                 unique_check = set(den_str + x)
#                 if len(unique_check) == 10:
#                     c1 += 1
#                     print(f'{den_int} / {x} = {N}')
#     if c1 != 0: print()
#     else: print(f'There are no solutions for {N}.\n')
#     N = int(input())


# mult with inc of N
N = int(input())
import itertools
den = list(itertools.permutations([k for k in range(10)], 5))
while N != 0:
    c1 = 0
    # low_finish = 0
    # high_finish = len(den) - 1
    # while low_finish < high_finish:
    #     target_finish = (low_finish + high_finish) // 2
    #     check_finish = int(''.join([str(j) for j in den[target_finish]])) *N
    #     if len(str(check_finish)) >= 6:
    #         high_finish = target_finish - 1
    #     elif len(str(check_finish)) < 6:
    #         low_finish = target_finish + 1
        
    # for i in range(0, target_finish + 1):
    for i in range(0, len(den)):
        den_str = (''.join([str(k) for k in den[i]]))
        den_int = int(den_str)
        mult = N * den_int
        if mult > 98765: break
        mult_str = str(mult)
        mult_set = set(mult_str)
        if len(mult_str) in range(4, 6) and len(mult_set) == len(mult_str):
                c2 = 0
                unique_check = set(den_str + mult_str)
                if len(unique_check) == 10:
                    c1 += 1
                    print(f'{mult_str} / {den_str} = {N}')
    if c1 == 0: print(f'There are no solutions for {N}.')
    N = int(input())
    if N > 0: print()

# presentation: separate input and output
# import itertools
# den = list(itertools.permutations([k for k in range(10)], 5))
# N_set = []
# while True:
#     N_input = int(input())
#     if N_input == 0: break
#     N_set.append(N_input)
    
# for N in N_set:
#     c1 = 0
#     if N == 0: break
#     low_finish = 0
#     high_finish = len(den) - 1
#     while low_finish < high_finish:
#         target_finish = (low_finish + high_finish) // 2
#         check_finish = int(''.join([str(j) for j in den[target_finish]])) *N
#         if len(str(check_finish)) >= 6:
#             high_finish = target_finish - 1
#         elif len(str(check_finish)) < 6:
#             low_finish = target_finish + 1
        
#     for i in range(0, target_finish + 1):
#         den_str = (''.join([str(k) for k in den[i]]))
#         den_int = int(den_str)
#         mult = N * den_int
#         mult_str = str(mult)
#         mult_set = set(mult_str)
#         if len(mult_str) in range(4, 6) and len(mult_set) == len(mult_str):
#                 c2 = 0
#                 unique_check = set(den_str + mult_str)
#                 if len(unique_check) == 10:
#                     c1 += 1
#                     print(f'{mult_str} / {den_str} = {N}')
#                 # else:
#                 #     continue
#     if c1 > 0: print()
#     else: print(f'There are no solutions for {N}.\n')