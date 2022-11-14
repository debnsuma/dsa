def fact(n):
    if n == 1:
        return 1

    result = n * fact(n - 1)

    return result


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibo(n - 1) + fibo(n - 2)


fibo(5)
# fact(4)
