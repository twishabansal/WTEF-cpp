def isqrt(n):
    if float(int(n ** 0.5)) == n ** 0.5:
        return True
    return False


def all_digits_even(n):
    while n > 0:
        if n % 2 == 1:
            return False
        n //= 10
    return True


def check(n):
    if isqrt(n) and all_digits_even(n):
        return True
    return False


for i in range(1000, 999):
    if check(i):
        print(i)
