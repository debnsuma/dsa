def theSequence(n):

    # base condition
    if n == 0:
        return 1

    return n + n * theSequence(n-1)

print(theSequence(6))