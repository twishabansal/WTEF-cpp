def each_row(i, n):
    return ("*" * (2 * i + 1)).rjust(n + i, " ")


def pattern(n):
    A = []
    for i in range(n):
        A.append(each_row(i, n))
    return A


'''
n=4
for ele in pattern(n):
	print (ele)
'''
# or don't use pattern(n)
'''
n=4
for i in range(n):
	print (each_row(i,n))
'''
