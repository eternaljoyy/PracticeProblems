def runningSum(self, nums):
    """
        - can use a 2 pointer approach in order to 
        find the sum of the elements 
        - have a variable sum, which keeps track of the sum of the 
        elements in the array 
        - create a new array (which will keep the new elements)
        - go through the array, adding the current item to sum  
        
        ==============================================================
        N -> Number of elements in the array 
        
        
        - Runtime complexity: O(N)
        - Spacetime complexity: O(??)
    """
        
    sum = 0 
        
    runningSumArr = []
        
        
    for item in range(len(nums)): 
        if item < len(nums):
            sum += nums[item]

            runningSumArr.append(sum) 
    return runningSumArr