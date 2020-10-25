def pick10(s: str, n: int):
    c = s[n]
    r = n
    i = 1
    while i < 10:
        r += i
        c += s[r % len(s)]
        i += 1
    return c
