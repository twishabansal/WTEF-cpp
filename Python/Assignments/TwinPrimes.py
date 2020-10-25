def isPrime(num):
    if num<=1:
        return False
    elif num in {2,3,5,7}:
        return True
    elif num%3==0 or num%2==0:
        return False
    else:
        r=5
        while r*r<=num:
            if num%r==0:
                return False
            r+=2
            if num%r==0:
                return False
            r+=4
        return True

def twinPrimes(start, limit):
    if start<=0 or limit<=0:
        return -1
    if start>=limit:
        return -2
    else:
        A=[]
        for i in range(start,limit-1):
            if isPrime(i) and isPrime(i+2):
                A.append((i,i+2))
        if len(A)==0:
            return -3
        else:
            return A

        