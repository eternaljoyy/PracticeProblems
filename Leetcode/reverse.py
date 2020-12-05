def reverse(x): 
	xList = list(str(x))

	#Base case A) Single digit 
	if (len(xList) == 1): 
		return x 

	string = ''
	for digit in xList: 
		if (digit == '-'):
			continue
		else: 
			string = digit + string
	return int(string)

print(reverse(123))