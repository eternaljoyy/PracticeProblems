def camelcase(s): 

	#Base case A) s is empty string or None 
	if (s == ' ' or s == None):
		return 0 

    #keeps track of the total number of words
	count = 1

	for item in s:
		if(item.isupper()): 
			count += 1
	return count


print(camelcase('oneTwoThree'))