def expand_no(n):
    s = str(n)
    A = []
    for i in range(len(s)):
        if int(s[i]) != 0:
            r = s[i] + ('0' * (len(s) - 1 - i))
            A.append(r)
    print(A)
    return " + ".join(A)


print(expand_no(5320))
