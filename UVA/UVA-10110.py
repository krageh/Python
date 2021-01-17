while True:
    n = int(input())
    if n == 0:
        break
    else:
        print('yes' if n % int(n**.5) == 0 and n > 0 else 'no')
