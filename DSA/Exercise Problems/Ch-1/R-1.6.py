def sso(n):
    c = 0
    for i in range(n):
        if i%2 > 0: # == 1
            c += i**2
    return c
