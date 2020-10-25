def digital_root(n):
    c=0
    k=str(n)
    for i in range(len(k)):
        c+=int(k[i])
    if c<10:
        return c
    else:
        return digital_root(c)
