def IsSpecialNumber(n):
    def fact(n):
        if n==0:
            return 1
        else:
            return n*fact(n-1)
    s=str(n)
    c=0
    for i in range(len(s)):
        c+=fact(int(s[i]))
    if c==n:
        return True
    return False

        