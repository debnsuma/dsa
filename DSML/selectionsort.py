def selection_sort(arr):

    for i in range(len(arr)-1):
        current = i + 1
        for j in range(current, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]

        print(arr)

    return arr

# arr = [1,2,40,12,5,100,0,23]
arr = [1,1,1,1, -1, -1, -1]
selection_sort(arr)