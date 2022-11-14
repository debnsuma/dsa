def fun(m):
    if m <= 0:
        return
    print(m)
    fun(m - 1)


def fun_reverse(m):
    if m <= 0:
        return
    fun_reverse(m - 1)
    print(m)


fun_reverse(3)
