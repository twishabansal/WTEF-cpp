def isCircularPrime(num):
    def prime(n):
        if n==2:
            return True
        elif n==1:
            return False
        else:
            for i in range(2,n):
                if n%i==0:
                    return False
        return True
    k=str(num)
    if num<=0:
        return False
    elif prime(num)==False:
        return False
    elif len(k)==1 and prime(num)==True:
        return True
    else:
        for i in range(len(k)-1):
            k=k[1:]+k[0]
            if prime(int(k))==False:
                return False
        return True
