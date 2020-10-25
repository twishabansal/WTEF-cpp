def qsqsq() -> [int]:
    def perfsq(n):
        return True if float(int(n**0.5))==n**0.5 else False
    A=[]
    for i in range(1,32):
        for j in range(2,10):
            k=i**2+j**3
            if k<1000 and perfsq(k)==True:
                A.append(k)
    B=list(set(A))
    B.sort()
    return B
print (qsqsq())