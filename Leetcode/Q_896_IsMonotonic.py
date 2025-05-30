def isMonotonic(nums):
    """ 
    Runtime Complexity: O(N)

    Spacetime Complexity: O(1) 
      - no additional data structures 
    ----------------------------------------------------

    - Have pointers to check if the stack 
    is increasing or decreasing 
    - Remember: (cannot be both increasing 
    and decreasing) 
    """

    is_increase = True
    is_decrease = True 

    for index in range(len(nums) - 1):

        if nums[index] < nums[index + 1]:
            is_decrease = False 
        else:
            if nums[index] > nums[index + 1]:
                is_increase = False 
    return is_increase or is_decrease



# tests 
print(isMonotonic([1,2,2,3])) # true
print(isMonotonic([1]))   # true

print(isMonotonic([6,5,4,4]))  # true 

print(isMonotonic([1,3,2]))  # false
print(isMonotonic([0, 3, 2, 1])) # false 