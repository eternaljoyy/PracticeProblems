def runningSum(nums):
    """
    N = # of items in the nums array 
            
    Runtime Complexity: 
      -> O(N): going through the nums array in a single pass 

    Spacetime Complexity: 
      -> O(N): making a new array with the same number of items 
      as the nums array 
    """
    
    if len(nums) == 0: 
        return 

    prefix_sum = []  
    sum = 0

    for index in range(len(nums)): # index = 5 
        sum += nums[index]   # sum = 6 + 15  
        prefix_sum.append(sum) # append() runs in O(1) time complexity
    return prefix_sum

    
    
# Testcases 

# Testcase 1
example_one = [1, 2, 3, 4, 5, 6] 
print(runningSum(example_one)) 

# testcase 2 
example_two = [1,1,1,1,1] 
print(runningSum(example_two))

# testcase 3 
example_three = [3,1,2,10,1]
print(runningSum([3,1,2,10,1]))