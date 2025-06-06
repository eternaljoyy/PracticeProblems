def transposeRestaurantSeating(seatingArrangement):

    # col = 1
    # row = 1

    # one-liner transposition to be implemented
    return [[seatingArrangement[row][col] for row in range(len(seatingArrangement[0]))] for col in range(len(seatingArrangement))]

# Example Seating Arrangement
original_seating = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# TODO: Call the function to transpose the seating and print each row of the transposed seating.
print(transposeRestaurantSeating(original_seating))