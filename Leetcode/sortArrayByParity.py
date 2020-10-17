def sortArrayByParity(A):
	evenElements = []
	oddElements = [] 

	for i in range(len(A)):
		if(A[i] % 2 == 0): 
			evenElements.append(A[i])
		else:
			oddElements.append(A[i])
	return evenElements + oddElements

print(sortArrayByParity([3,1,2,4]))