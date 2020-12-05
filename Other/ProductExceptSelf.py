def productExceptSelf(arr):
	result = [1] * len(arr)
	#base case A) one element 
	if(len(arr) == 1):
		return 

	'''calculate the right products of all numbers 
	EXCEPT for the LAST number'''

	rightProduct = 1
	for i in range(len(arr)-2, -1, -1):
		rightProduct *=  arr[i+1]
		result[i] = rightProduct
	print(result)

	
	'''calculate the left product  
	EXCEPT fot the FIRST number -> 0th index
	''' 
	leftProduct = 1
	for j in range(1, len(arr)):
		leftProduct *= arr[j-1]
		result[j] = result[j] * leftProduct
	print(result)
