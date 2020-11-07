#Question 1464 

def maxProduct(nums):
        #base case A) Empty list 
        if(nums == [] or len(nums) == 1):
            return nums
        
        maxProduct = 0
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if((nums[i]-1) * (nums[j]-1) > maxProduct):
                    maxProduct = (nums[i]-1) * (nums[j]-1)
        return maxProduct