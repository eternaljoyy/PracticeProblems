def vertical_traverse(matrix):
    """ 
    Traverse the matrix from bottom-up 
    """
    
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return []
    
    rows = len(matrix) 
    cols = len(matrix[0])

    # We start at the bottom right for the vertical traversal.
    row = rows - 1 # row = 2 
    col =  cols - 1 # col = 3 

    result = []

    while col >= 0:
        result.append(matrix[row][col]) 

        if row > 0:
            row -= 1
        # reset the row back to the last one once reaching the top of matrix 
        else: 
            col -= 1 
            row = rows - 1 
    return result

# Example matrix representing library bookshelves
bookshelves = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Output should be the vertical traverse of the bookshelves
print(vertical_traverse(bookshelves))  # [12, 8, 4, 11, 7, 3, 10, 6, 2, 9, 5, 1]