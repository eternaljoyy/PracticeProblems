def diagonalDifference(arr):
	#sums the elements of both diagonals 
    mainDiagonalSum = 0
    secondaryDiagonalSum = 0
    # Write your code here
    for row in range(0, len(arr)):
    	mainDiagonalSum += arr[row][row]
    	secondaryDiagonalSum += arr[row][len(arr) - row - 1]
    print(abs(mainDiagonalSum - secondaryDiagonalSum))

diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]])