def if_ascending(n, size):
    k = str(n)
    for i in range(size - 1):
        if int(k[i + 1]) <= int(k[i]):
            return False
    return True


def start(size):
    return int(size * '1')


def end(size):
    return int(size * '9')


def value_array(size):
    A = []
    for i in range(start(size), end(size) + 1):
        if if_ascending(i, size):
            A.append(i)
    return A


def no_displayed(l, size):
    A = value_array(size)
    k = l % len(A)
    return A[k - 1]


def kth_next_reading(n, k, size):
    A = value_array(size)
    ind = A.index(n)
    return A[(ind + k) % len(A)]


def kth_prev_reading(n, k, size):
    A = value_array(size)
    ind = A.index(n)
    return A[(ind - k) % len(A)]


def distance_bw_readings(r1, r2, size):
    A = value_array(size)
    ind1 = A.index(r1)
    ind2 = A.index(r2)
    return abs(ind1 - ind2)
