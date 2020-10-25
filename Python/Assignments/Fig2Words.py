d={0:'zero', 1:'one', 2:'two', 3:'three',4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
def fig2words(n: int) -> str:
    k=str(n)
    s=''
    if n==100:
        return "hundred"
    elif len(k)==3:
        r=int(k[1:])
        s+=d[int(k[0])]
        s+=" hundred"
        if n%100!=0:
            s+=' and'
        if 0<r<=15:
            s+=' '+d[r]
        elif r in range(16,20):
            s+=' '+d[int(k[1:])]+"teen"
        elif r>=20 and r%10!=0:
            s+=' '+d[int(k[1])*10]+' '+d[int(k[2])]
        elif r>=20 and r%10==0:
            s+=' ' +d[int(k[1])*10]
    elif len(k)==2:
        if n<=15:
            s+=d[n]
        elif n in range(16,20):
            s+=d[int(k[1:])]+"teen"
        elif n>=20 and n%10!=0:
            s+=d[int(k[0])*10]+' '+d[int(k[1])]
        elif n>=20 and n%10==0:
            s+=d[int(k[0])*10]
    else:
        s+=d[n]
    return s

