n, t, k, d = (int(x) for x in input().split())
# import math
# x = math.ceil(n/k)
# if n % k == 0:
#     x=n/k
# else:
#     x = n // k + 1
# t1 = 0
# t2 = d
# i = 0
# while i < x:
#     if t1 <= t2:
#         t1 += t
#     elif t1 > t2:
#         t2 += t
#     i += 1

# t_1 = x * t
# t_2 = max(t1, t2)
# if t_2 < t_1:
#     print('YES')
# else:
#     print('NO')

import math
if k >= n:
    print('NO')
else:
    t_1 = t*(math.ceil(n/k))
# t_2 = d + t*(n-d*k/t)/k/2
    if d % t == 0:
        # t_2 = d + t*(n-k)/k/2
        x = d/t
        m = x*k
        t_2 = x*t
        while m < n:
            t_2 += t
            m += 2*k
    elif d < t:
        m = k
        t_2 = t
        while m < n:
            t_2 += d
            m += k
            if m <n:
                t_2 += t-d
                m += k
    elif d > t:
        # x = math.ceil(d/t)
        x = d//t
        # t_2 = x*t
        t_2 = (x+1)*t
        # m = x*k
        m = (x+1)*k
        while m < n:
            # t_2 += d-(x-1)*t
            t_2 += d-x*t
            m += k
            if m < n:
                # t_2 += x*t-d
                t_2 += (x+1)*t-d
                m += k
    print(t_1)
    print(t_2)
    if t_1 > t_2:
        print('YES')
    else:
        print('NO')

# t/k * d*k/t
# cakes in time d = d*k/t
# cakes with 2 ovens = t*n/k/2
# t_2 = d + t*(n-d*k/t)/k/2
 

# elif d > t:
#     t_2 = 2*t + t-(2*t-d) + t-(t-(2*t-d)) + t-(2*t-d)...
#         = 2*t + d-t + t-(d-t) + d-t...
#         = 2*t + d-t + 2*t-d + d-t...
#     t_2 = 3*t + t-(3*t-d) + t-(t-(3*t-d)) + t-(3*t-d)...
#         = 3*t + d-2*t + t-(d-2*t) + d-2*t...
#         = 3*t + d-2*t + 3*t-d + d-2*t...
#     t_2 = 4*t + t-(4*t-d) + t-(t-(4*t-d)) + t-(4*t-d)...
#         = 4*t + d-3*t + t-(d-3*t) + d-3*t...
#         = 4*t + d-3*t + 4*t-d + d-3*t...
# elif d < t:
#     t_2 = t + t-(t-d) + t-(t-(t-d)) + t-(t-d)...
#         = t + d + t-d + d...
    
