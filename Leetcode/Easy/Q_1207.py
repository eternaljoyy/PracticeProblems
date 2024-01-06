def uniqueOccurrences(arr): 
	'''  
	Approach: 

	- Use a dictionary to keep track of occurence 
	of each element; key (item) & value (# of occurrence) 
	- go through array, counting the occurence of each item & 
	add it to dictionary  
	- iterate through dictionary to check for any repeated
	value	

	==========================================================

	N = size of input array, arr 
	M = size of dictionary 

	Time Complextities: 
	 - Runtime Complexity: O(N + M)
	 - **Spacetime Complexity: ??
	''' 

	numOccurrences = {} 

	for item in range(len(arr)):
		if arr[item] not in numOccurrences:
			numOccurrences[arr[item]] = 1
		else:
			numOccurrences[arr[item]] += 1 

	
	uniqueVals = set() 

	
	for key in numOccurrences:
		if numOccurrences[key] in uniqueVals:
			return False 
		uniqueVals.add(numOccurrences[key])
	return True 


#Tests 
print(uniqueOccurrences([1,2,2,1,1,3]))
print(uniqueOccurrences([1,2]))
print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
