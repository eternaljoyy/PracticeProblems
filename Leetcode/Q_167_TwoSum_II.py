def twoSum(numbers, target):
    """
    Runtime Complexity: 

    Spacetime Complexity: O(1) 
     - No additional data structures were being used 
    """

    low = 0 
    high = len(numbers) - 1

    while low < high: 
        if numbers[low] + numbers[high] == target:
            return [low + 1, high + 1]
        elif numbers[low] + numbers[high] < target:
            low += 1
        else:
            high -= 1


# testcases 
print(twoSum([2,7,11,15], 9))

print(twoSum([2, 3, 4], 6))

print(twoSum([-1, 0], -1))