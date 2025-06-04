def bookshelfTraversal(bookshelves):

    # TODO: Determine the number of rows and columns in 'bookshelves'
    rows = len(bookshelves) - 1 # rows = 1
    cols = len(bookshelves[0]) - 1  # cols = 3

    direction = 'up'
    traversal_path = []

    while cols >= 0:
        traversal_path.append(bookshelves[rows][cols]) # path = 8 4 3 7 6 2 1 5 

        if direction == 'up':
            if rows > 0:
                rows -= 1
            else:
                direction = 'down'
                cols -=1 
        else:
            if rows == len(bookshelves) - 1:
                direction = 'up' 
                cols -= 1 
            else:
                rows += 1
    return traversal_path


# TODO: Create a 2x4 'bookshelves' variable with unique numbers representing books
bookshelves = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

# TODO: Print the traversal path of the books
print(bookshelfTraversal([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]))