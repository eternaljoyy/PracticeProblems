def twoSum(nums, target):

    #Base Case A) Empty list or single element
    if(len(nums) < 2):
        return nums

    #Solution 1: Naive solution (2 for loops)
    '''for i in range(len(nums)-1):
        for j in range(1, len(nums)):
            if(nums[i] + nums[j] == target):
                return [i, j]'''


print(twoSum([2,7,11,15],9))
#print(twoSum([3,2,4],6)) 
#print(twoSum([3,3]BB, 6))