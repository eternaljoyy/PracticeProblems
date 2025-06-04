def column_traverse(matrix):
    rows = len(matrix)   
    cols = len(matrix[0]) 
    row = rows - 1 # rows = 2 
    col = cols - 1 # cols = 3 
    direction = -1  # Start going upwards
    output = []

    for _ in range(rows * cols): # 0 
        output.append(matrix[row][col]) # output: 12 
        # TODO: Implement logic to change direction and move left when hitting the top or bottom of the shelf

        if direction == -1: 
            if row == 0:
                # change direction to going down 
                direction = 1
                col -= 1 # col = 0 
            else: 
                row -= 1 # row = 0 
        else:
            if row == len(matrix) - 1:
                # change the direction to go back up 
                direction = -1 
                col -= 1 
            else:
                row += 1 # row 
    return output

# Example matrix resembling a bookshelf (3 shelves, 4 books each)
bookshelf = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(column_traverse(bookshelf))