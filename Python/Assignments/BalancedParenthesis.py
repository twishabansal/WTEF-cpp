def SplitParenthesis(txt):
    A=[]
    i=0
    while i<len(txt):
        if txt[i]==')' and txt[:i].count('(')-txt[:i].count(')')==1:
            A.append(txt[:i+1])
            txt=txt[i+1:]
            i=0
        i+=1
    return A
                