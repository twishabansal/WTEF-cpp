def matches(s1, s2):
    c=0
    k=min(len(s1),len(s2))
    if k==0:
        return 0
    else:
        for i in range(k):
            if s1[i]==s2[i]:
                c+=1
    return c

