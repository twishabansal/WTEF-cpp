d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
romans = list(d.keys())


def large_first(s, i):
    return True if romans.index(s[i]) >= romans.index(s[i + 1]) else False


def numerical(s):
    num = d[s[-1]]
    for i in range(len(s) - 1):
        if large_first(s, i):
            num += d[s[i]]
        else:
            num -= d[s[i]]
    return num


print(numerical('XIV'))
