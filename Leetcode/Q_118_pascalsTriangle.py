def generate(numRows):
    """
        :type numRows: int
        :rtype: List[List[int]]
    """
        
    matrix = []

    for i in range(numRows):
        matrix.append([0] * (i + 1))


    # loop through the matrix
    for n in range(numRows): 
        for i in range(n+1): 
            # **TODO: remove this since for n = 0, n = 1, its always just 1s.  
            if i == 0 or i == n: 
                matrix[n][i] = 1 
            else:
                matrix_val = matrix[n-1][i-1] + matrix[n-1][i]
                matrix[n][i] = matrix_val
    return matrix


print(generate(5))    