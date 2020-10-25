def sum_of_holes(limit):
    A=[1,0,0,0,1,0,1,0,2,1]
    def hole(n):
        k=str(n)
        c=0
        for i in range(len(k)):
            c+=A[int(k[i])]
        return c
    c=0
    for i in range(1,limit+1):
        c+=hole(i)
    return c

