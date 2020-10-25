def odd(n):
    return n % 2 == 1


def Multi_matrix(n1, n2):
    B = []
    while n1 >= 1:
        B.append([str(n1), str(n2), '+']) if odd(n1) else B.append([str(n1), str(n2)])
        n1 //= 2
        n2 *= 2
    return B


def product(B):
    c = 0
    for i in range(len(B)):
        if odd(int(B[i][0])):
            c += int(B[i][1])
    k = str(c)
    return k


def each_row(i, B):
    return B[i][0].ljust(len(B[0][0]), " ") + " " + B[i][1] + " " + "+" if odd(int(B[i][0])) else B[i][0].ljust(
        len(B[0][0]), " ") + " " + B[i][1]


def len_line(B):
    return len(B[0][0]) + len(B[-1][1]) + 3


def product_print(k, line):
    return k.rjust(line, " ")


def equal_print(line):
    return '=' * line


if __name__ == '__main__':
    n1 = 18
    n2 = 85
    B = Multi_matrix(n1, n2)
    line = len_line(B)
    k = product(B)
    for i in range(len(B)):
        print(each_row(i, B))
    print(equal_print(line))
    print(product_print(k, line))
    print(equal_print(line))
