def getPrimoral(number):
    if number==0:
        return 0
    def prime(n):
        c=0
        for i in range(1,n):
            if n%i==0:
                c+=1
        if c==1:
            return True
        return False
    def arr(n):
        A=[]
        i=2
        while True:
            if len(A)<n:
                if prime(i):
                    A.append(i)
            else:
                break
            i+=1
        return A
    c=1
    A=arr(number)
    for i in range(len(A)):
        c*=A[i]
    return c
    
