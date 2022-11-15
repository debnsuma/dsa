def sumOfDigits(n):
    '''
    :param n: given number
    :return: sum of digits of n.
    '''
    # code here

    if n < 10:
        return n

    return n % 10 + sumOfDigits(n // 10)

sumOfDigits(999999999)
#%%
