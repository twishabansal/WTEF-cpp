def is_palindrome_possible(txt):
    c=0
    for i in set(txt):
        if txt.count(i)%2!=0:
            c+=1
    if len(txt)%2==0 and c==0:
        return True
    elif len(txt)%2!=0 and c==1:
        return True
    return False
