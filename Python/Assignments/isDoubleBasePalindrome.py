def isDoubleBasePalindrome(n):
    k=bin(n)[2::]
    def palin(n):
        if str(n)==str(n)[::-1]:
            return True
        return False
    if palin(n) and palin(k):
        return True
    return False