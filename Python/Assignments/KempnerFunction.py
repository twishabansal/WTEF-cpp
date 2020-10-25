def kempner(n):
    def fact(n):
        return n*fact(n-1) if n!=0 else 1
    def is_prime(n):
        if n<=1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    if is_prime(n):
        return n
    i=1
    while True:
        if fact(i)%n==0:
            return i
        i+=1