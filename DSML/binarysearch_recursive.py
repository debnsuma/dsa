def recur_search(key, values, lower, upper):

    # base case
    # print(lower, upper)
    if lower > upper:
        return False

    mid = (upper + lower)//2

    if values[mid] == key:
        return True
    elif values[mid] > key:
        upper = mid - 1
        return recur_search(key, values, lower, upper)
    else:
        lower = mid + 1
        return recur_search(key, values, lower, upper)


def recur_search2(key, values, lower, upper):

    while lower <= upper:

        mid = (upper + lower)//2
        if values[mid] == key:
            return True
        elif key < values[mid]:
            upper = mid - 1
        else:
            lower = mid + 1

    else:
        return False




key = 1
values = [0,2,2,3]
lower = 0
upper = len(values)
print(recur_search2(key, values, lower, upper-1))

