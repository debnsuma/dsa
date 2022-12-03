def merge_two_arr(a, b):

    i = len(a) + len(b)
    res = []
    a_pointer = 0
    b_pointer = 0
    for i in range(i):
        print(a_pointer, b_pointer)
        if a_pointer < len(a) and a[a_pointer] < b[b_pointer]:
            res.append(a[a_pointer])
            a_pointer += 1
        else:
            res.append(b[b_pointer])
            b_pointer += 1

    return res

a = [10, 15, 20]
b = [5, 6, 6, 30]
merge_two_arr(a,b)