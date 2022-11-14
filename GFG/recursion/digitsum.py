def dig_sum(n):
    if n < 10:
        return n

    digit = n % 10

    return digit + dig_sum(n // 10)


dig_sum(253)
