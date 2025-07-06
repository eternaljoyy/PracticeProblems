def printTriangle(row_num):
	'''
	given a number row_num, representing the 
	number of rows. Print the numbers up to the
	nth row: 

	Example 1: 

	row_num = 3 

	1 
	2 3
	4 5 6 


	Example 2: 

	row_num = 4 

	1 
	2 3
	4 5 6
	7 8 9 10  

	---------------------------------------------------

	Spacetime Complexity: O(1)
	  - Not making any new additional data structures 

	Runtime Complexity: O(N^2)
	'''

	#keep track of the number you need to print. (Starting at 1)
	sum = 1

	for item in range(row_num):
		for j in range(item + 1):  
			print(sum, end= " ")
			sum += 1
		print()


print(printTriangle(5))