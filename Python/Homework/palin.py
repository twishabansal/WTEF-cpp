def palin(s):
    c = 0
    for i in set(s):
        if s.count(i) % 2 != 0:
            c += 1
    if len(s) % 2 == 0 and c == 0:
        return True
    elif len(s) % 2 != 0 and c == 1:
        return True
    return False
