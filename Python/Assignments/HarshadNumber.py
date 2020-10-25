def moranNumbers(n):
    def is_prime(n):
        if n<=1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    s=str(n)
    digit_sum=0
    for i in range(len(s)):
        digit_sum+=int(s[i])
    if n/digit_sum%1==0 and is_prime(n/digit_sum):
        return "M"
    elif n%digit_sum==0:
        return "H"
    return "Neither"
    

        
            