def recur_search(key, values, lower, upper):

    # base case
    # print(lower, upper)
    if lower >= upper:
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





key = 2
values = [1,1,1,1,1]
lower = 0
upper = len(values)
print(recur_search(key, values, lower, upper))

