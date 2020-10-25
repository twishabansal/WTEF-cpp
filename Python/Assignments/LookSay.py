def look_and_say(n):
    s=str(n)
    if len(s)%2!=0:
        return 'invalid'
    k=''
    for i in range(1,len(s)+1,2):
        k+=s[i]*int(s[i-1])
    return int(k)