def findDuplicates(nums):
        newArr = [] 
        
        #Base case (only has one element)
        if(len(nums) == 1):
            return nums 

        #print all items appearing twice in list 
        for item in nums: 
            if (nums.count(item) == 2):
                if(item not in newArr):
                    newArr.append(item)
        return newArr

print(findDuplicates([4,3,2,7,8,2,3,1]))
