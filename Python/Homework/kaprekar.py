def array_n(n):  # no to array
    return list(map(int, str(n).strip()))


def arrint(arr):  # array into integer
    st = ''
    for ele in arr:
        st += str(ele)
    return int(st)


def max_no(n):
    arr = array_n(n)
    arr.sort(reverse=True)
    return arrint(arr)


def min_no(n):
    arr = array_n(n)
    arr.sort()
    return arrint(arr)


def diff(n):
    return max_no(n) - min_no(n)


def kaprekar(n):
    if diff(n) == n:
        return [n, max_no(n), min_no(n), diff(n)]
    return [n, max_no(n), min_no(n), diff(n)] + kaprekar(diff(n))


print(kaprekar(1267))
