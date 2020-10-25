def aliquotSum(n):
    c=1
    if n==1:
        return 0
    elif n==2 or n==3:
        return 1
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                c+=i
    return c
    

def classify(n):
    if aliquotSum(n)<n:
        return "Alpha"
    elif aliquotSum(n)==n:
        return "Gamma"
    else:
        return "Beta"
