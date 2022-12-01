def bubble_sort(a):
    n = len(a)
    for i in range(n):
        flag = False
        for j in range(0, n - i - 1):
            if a[j] > a[j+1]:
                a[j + 1], a[j] = a[j], a[j + 1]
                flag = True
        if not flag:
            break

    return a


arr = [1, 3, 2, 5, 60, 12, 100, 1]
bubble_sort(arr)
