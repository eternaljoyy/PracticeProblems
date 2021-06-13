def transpose(transposeMatrix, matrix): 
    ''' 
    - flip the matrix so that rows become the columns (and vice versa)
    - make a new matrix; place the transpose matrix in there  
    ''' 

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            transposeMatrix[col][row] = matrix[row][col]
    return transposeMatrix


def makeMatrix(matrix, newMatrix):
    '''
    - make a new matrix with the same number of rows as the input matrix 
    '''

    #make the new matrix 
    newMatrix = [] 

    for col in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)):
            newRow.append(0)
        newMatrix.append(newRow) 
    return transpose(newMatrix, matrix) 


print(makeMatrix([[1,2,3],[4,5,6],[7,8,9]], []))
print(makeMatrix([[1,2,3],[4,5,6]], []))