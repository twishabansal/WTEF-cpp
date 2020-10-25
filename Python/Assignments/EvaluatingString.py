def Evaluating_String(string):
	str1=string[::2]
	str2=string[1::2]
	def str_check(string):
		if len(string)%2==0:
			return -1
		elif ('A' in str1) or ('B' in str1) or ('C' in str1):
			return -1
		elif ('0' in str2) or ('1' in str2):
			return -1
		else:
			return find_value(string)
	
	def str_rep(string1,val,k):
		return string1.replace(string1[k],str(val))


	def find_value(string):
		val=0
		str1=string[::2]
		str2=string[1::2]
		for i in range(len(string)//2):
			if str2[i]=='A':
				if int(str1[i])+int(str1[i+1])==2:
					val=1
			elif str2[i]=='B':
				if int(str1[i])+int(str1[i+1])==1:
					val=1
			else:
				if int(str1[i])+int(str1[i+1])==0:
					val=1
			str_rep(str1,val,i+1)
		return val
	return str_check(string)
