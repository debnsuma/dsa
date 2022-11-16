def fact(n):
    if n == 0:
        return 1

    return n * fact(n - 1)


# print(fact(5))

def nCr(n, r):

    if n == r:
        return 1
    if(n < r):
        return 0
    if r == 0:
        return 1
    if(r == 1):
        return n
    if(n == 1):
        return 1

    return (nCr(n-1, r-1) + nCr(n-1, r))

print(nCr(5, 2))