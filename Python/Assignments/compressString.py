def compressString(s):
	j=0
	A=[]
	B=[]
	while j+1+sum(A)<len(s):
	    res=sum(A)+j
	    c=0
	    i=j+1+sum(A)
	    while i<len(s):
	        if s[i]!=s[res]:
	            break
	        else:
	            c+=1
	        i+=1
	    A.append(c)
	    B.append(s[res])
	    j+=1
	m=''
	for i in range(len(A)):
	    if A[i]>1:
	        m+=str(A[i]+1)+B[i]
	    else:
	        m+=(A[i]+1)*B[i]
	return m
	    