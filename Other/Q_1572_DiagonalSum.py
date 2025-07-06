def matrixDiagonalSum(arr):
	''' 
	Problem: given an N * N matrix, find the sum of the diagonal. 
	Diagonal starts at the top-left side. 
        - Contains only integers 
    
    ---------------------------------------------------------------
	N = # of items in the matrix 

    Runtime Complexity: O(N) 
	 - Liinearly traversing/probing through each and every row of the 
	 matrix 

    Spacetime Complexity: O(1) 
     - not creating any additional data structures
	'''

	primary_diagonal = 0

	col = len(arr)-1

	secondary_diagonal = 0


	for item in range(0, len(arr)): 
		primary_diagonal += arr[item][item]


		if item != col:
			secondary_diagonal += arr[item][col]

		col -= 1
	return primary_diagonal + secondary_diagonal
 



print(matrixDiagonalSum([[1,1,1,1],
              			[1,1,1,1],
              			[1,1,1,1],
              			[1,1,1,1]]))

print(matrixDiagonalSum([[5]]))

