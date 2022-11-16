def palindrome(s):
    if len(s) == 1:
        print("Yes")
        return True
    elif len(s) == 2:
        if s[0] == s[1]:
            print("Yes")
            return True
        else:
            print("No")
            return False

    elif s[0] == s[-1]:
        palindrome(s[1:len(s) - 1:])

    else:
        print("No")
        return False


def palindrome2(s):
    if len(s) == 0 or len(s) == 1:
        print("Yes")
        return

    else:
        if s[0] == s[-1]:
            palindrome2(s[1:len(s) - 1:])
        else:
            print("No")
            return


# palindrome2("aabaaaba")


def numReverse(n):

    global reverse_num, base
    if n == 0:
        return reverse_num

    reverse_num = reverse_num * 10
    reverse_num += n % 10

    return numReverse(n // 10)


reverse_num = 0

numReverse(123456)