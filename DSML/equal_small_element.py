

def solve(A, B):
    global count
    print(count, A)
    if not A:
        return count
    else:
        lower = 0
        upper = len(A)
        mid = (upper + lower) // 2

        if B >= A[mid]:
            count += mid + 1
            return solve(A[mid+1:], B)
        else:
            return solve(A[0:mid], B)


count = 0
print(solve([1,2,5,5], 3))
