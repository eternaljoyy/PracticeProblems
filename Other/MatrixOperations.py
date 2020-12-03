def max_from_ops(newMatrix, operations): 
	#TODO: FIgure out how to loop through multiple operations 
	rowOp = operations[0] 
	colOp = operations[1]

	for row in range(len(newMatrix)):
		if(row < rowOp):
			for col in range(len(newMatrix[row])):
				if(col < colOp):
					newMatrix[row][col] += 1
				else:
					break  
		else:
			break
	return newMatrix
			

def create_matrix(m, n):
	newMatrix = []	

	for row in range(m):
		rows = []
		for col in range(n):
			rows.append(0) 
		newMatrix.append(rows)
	print(max_from_ops(newMatrix, [1,1]))

print(create_matrix(4,4))