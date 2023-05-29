def twoSum(nums, target):

    '''
    Note: x + y = Target 
              y = Target - x 
              x = Target - y 

    - create a dictionary in order to store and lookup some values
    - go through nums array 
       - if the complement of the current number is in the dictionary, then return 
       the index of that number & the current number 
       - otherwise, add current number to dictionary 
    '''

    pairs_dict = {} 

    for item in range(len(nums)):
        complement = target - nums[item]

        if complement in pairs_dict:
            return item, pairs_dict.get(complement)
        else:
            pairs_dict[nums[item]] = item



#Test cases 
print(twoSum([1,2,3], 4))