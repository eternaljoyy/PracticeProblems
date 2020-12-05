class MatrixOperations: 
	def max_from_ops(self, newMatrix, operations): 
		rowOp = operations[0]
		colOp = operations[1]
		#TODO: FIgure out how to loop through multiple operations 
				
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

	
	#Calls the max_from_ops function (doing each operation one by one)
	def operationsList(self, newMatrix, operations):

		for item in operations:
			self.max_from_ops(newMatrix, item)

	def create_matrix(self, m, n):
		newMatrix = []	

		for row in range(m):
			rows = []
			for col in range(n):
				rows.append(0) 
			newMatrix.append(rows)
		self.operationsList(newMatrix, [[1,1], [2,2]])

firstMatrix = MatrixOperations()
firstMatrix.create_matrix(4,4)