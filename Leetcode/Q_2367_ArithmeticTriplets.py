def arithmeticTriplets(nums, diff):
    """
        :type nums: List[int]
        :type diff: int
        :rtype: int
    """ 
    # Brute Force
    unique_triplets = 0
    
    for i in range(len(nums)-2):
        for j in range(i + 1, len(nums)-1):
            for k in range(j + 1, len(nums)):
                if (nums[j] - nums[i] == diff) and (nums[k] - nums[j] == diff):
                    unique_triplets += 1
    return unique_triplets


# Testcases  
# case A
print(arithmeticTriplets([0,1,4,6,7,10], 3))

# Case B 
print(arithmeticTriplets([4,5,6,7,8,9], 2))