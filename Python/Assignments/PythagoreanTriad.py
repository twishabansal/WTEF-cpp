def peri() -> int:
    def trip():
        A=[]
        for b in range(500):
            for a in range(1,b):
                c=(a*a+b*b)**0.5
                if c%1==0 and a+b+c<1000:
                    A.append([a,b,int(c)])
        return A
    A=trip()
    B=[]
    for i in range(len(A)):
        B.append(sum(A[i]))
    C=[]
    ls=list(set(B))
    for j in ls:
        C.append(B.count(j))
    return ls[C.index(max(C))]

        


