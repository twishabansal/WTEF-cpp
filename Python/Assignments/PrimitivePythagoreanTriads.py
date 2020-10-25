def primitive_pyth() -> [(int, int, int)]:
    def gcd(x,y):
        while y:
            x,y=y,x%y
        return x
    A=[]
    for b in range(1,100):
        for a in range(1,b):
            c=(a*a+b*b)**0.5
            if c%1==0 and c<100:
                if gcd(a,b)==1 or gcd(b,c)==1 or gcd(a,c)==1:
                    A.append((a,b,int(c)))
    return A
print (primitive_pyth())