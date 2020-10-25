def trailing_zeros(n):
    c=0
    i=5
    while n//i>=1:
        c+=n//i
        i*=5
    return c