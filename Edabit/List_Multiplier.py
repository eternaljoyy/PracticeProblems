def multiply(l):
	newArr = []
	#base case (empty list) 
	if( l == []):
		return [] 

	for item in l: 
		if(isinstance(item, int)):
			newArr.append(([item]*item))
		else: 
			if(isinstance(item, str)):
				newArr.append([item]*len(l))
	return newArr

print(multiply(["*", "%", "$"]))