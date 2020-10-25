def expand(num):
    s=str(num)
    A=[]
    for i in range(len(s)):
        if int(s[i])!=0:
            A.append(s[i]+('0'*(len(s)-1-i)))
    return " + ".join(A)