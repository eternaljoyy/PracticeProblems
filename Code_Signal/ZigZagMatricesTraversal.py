library = [
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [9, 11, 13, 15]
]

# Starting from the bottom right corner of the bookshelf
row = len(library) - 1   # 2 
col = len(library[0]) - 1  # 3
goingUp = True

while col >= 0: 
    print(library[row][col], end=" ") # 15 8 7 5 6 13 11 4 3 1 2 9 
    if goingUp:
        if row == 0:
            goingUp = False
            col -= 1 # col = 0
        else:
            row -= 1  
    else:
        if row == len(library) - 1:
            goingUp = True
            col -= 1 # col = -1 
        else:
            row += 1 # row = 2