def arithmeticTriplets(nums, diff):
    """ 
    N = # of items in the nums array 

    Runtime Complexity: 
    -> O(N) 
      - going through all the values 
      in the nums array 


    Spacetime Complexity: 
    -> O(1) 
      - no new additonal data structures 
      were created 
    """

    unique_triplets = 0 


    for index in range(len(nums)):
        i = abs(diff - nums[index])
        k = diff + nums[index]

        if i < nums[index] < k and nums[index] - i == diff and k - nums[index] == diff:
            # check if they exist in the array 
            if i in nums and k in nums:
                unique_triplets += 1
    return unique_triplets


# Testcases 
# testcase A
print(arithmeticTriplets([0, 1, 4, 6, 7, 10], 3))

# # testcase B
print(arithmeticTriplets([4, 5, 6, 7, 8, 9], 2))

# # testvase C 
print(arithmeticTriplets([0, 1, 2], 1))

# testcase D 
print(arithmeticTriplets([1,2,3,7,8], 4))