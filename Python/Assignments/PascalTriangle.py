def pascals_triangle(row):
    def fact(n):
        if n==0:
            return 1
        else:
            return n*fact(n-1)
    string=''
    for i in range(row):
        string+=str(int(fact(row)/(fact(row-i)*fact(i))))
        string+=' '
    string+=str(1)
    return string
        
        