def stringTansformation(array):
    def vow_to_dollar(array):
	    for element in array[0]:
		    if element in 'aeiouAEIOU':
			    array[0]=array[0].replace(element,'$')
	    return array[0]

    def cons_to_hash(array):
	    for element in array[1]:
		    if element not in 'aeiouAEIOU':
		    	array[1]=array[1].replace(element,'#')
	    return array[1]

    def upper_case(array):
	    return array[2].upper()

    return vow_to_dollar(array)+cons_to_hash(array)+upper_case(array)
