def groupAnagrams(words):
	arr2=[x.lower() for x in words]
	B=[]
	i=0
	while i<len(arr2):
		C=[arr2[i]]
		j=i+1
		while j<len(arr2):
			if sorted(arr2[i])==sorted(arr2[j]):
				C.append(arr2[j])
				del arr2[j]
				j-=1
			j+=1
		B.append(C)
		i+=1
	return B

