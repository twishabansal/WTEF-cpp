def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    return gcd(a, b - a)


def relatively_prime(n1, n2):
    return gcd(n1, n2) == 1


def totient(n):
    count = 1
    for i in range(2, n):
        if relatively_prime(n, i):
            count += 1
    return count
