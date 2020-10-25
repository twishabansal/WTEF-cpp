def encrypt(input_word):
    s=input_word[::-1]
    A=['a','e','o','u']
    for i in range(len(s)):
        if s[i] in A:
            s=s.replace(s[i],str(A.index(s[i])))
    return s+'aca'
            
