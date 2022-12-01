def bubble_sort(a):
    n = len(a)
    for i in range(n):
        flag = False
        for j in range(0, n - i - 1):
            if a[j] > a[j+1]:
                a[j + 1], a[j] = a[j], a[j + 1]
                flag = True
        # if not flag:
        #     break
#            print(a, a[::-1][0] + a[::-1][-1])
            print(a, a[0] + a[-1])


    return a[::-1]


#arr = "64 34 25 12 22 11 90".split()
arr = "46 86 55 13 19 40 80 78".split(" ")
#arr = "54 75 58 96 113 54 667".split(" ")
arr = [int(i) for i in arr]
bubble_sort(arr)

