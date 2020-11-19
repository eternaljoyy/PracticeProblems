def diagonalSum(mat): 
	sumPrimary = 0
	sumSecondary = 0 
	primaryDiagonal = [] 

	#base case A) empty matrix or mat of length 1 
	if(mat == ''):
		return mat 
	else:
		if(len(mat) == 1):
			return mat[0][0] 

	for row in range(len(mat)):
		if(mat[row][row] not in primaryDiagonal):
			primaryDiagonal.append((row, row))
			sumPrimary += mat[row][row] 
	
	for row in range(len(mat)):
		'''make sure that elements on secondary diagonal arent part of 
		elements on primary diagonal
		- check if index of element is in the list 
		''' 
		
		if((row, len(mat)-(row+1)) not in primaryDiagonal):
			if(row == 0):
				sumSecondary += mat[row][len(mat)-1]
			else: 
				sumSecondary += mat[row][len(mat)-(row+1)]
		else:
			continue
	return sumPrimary + sumSecondary


print(diagonalSum([[1,2,3], [4,5,6], [7,8,9]]))
print(diagonalSum([[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]))
print(diagonalSum([[5]]))