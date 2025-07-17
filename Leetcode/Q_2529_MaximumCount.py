class Solution:
    def maximumCount(self, nums):
        ''' 
        Going through the array one by one and checking whether
        the number is negative or positive. 
        ------------------------------------------------------- 
        N = # of items in the nums array 

        Runtime Complexity: O(N)
         - We are linearly probing through the array, resulting in a
         runtime complexity of O(N). 

        Spacetime Complexity: O(1)
         - no additional data structure is being used. 
        '''

        pos = neg = 0 

        for index in range(len(nums)):

            if nums[index] > 0:
                pos += 1
            elif nums[index] < 0:
                neg += 1
            continue
        return max(pos, neg) 
        


# testcase 
first_case = Solution()
print(first_case.maximumCount([-2,-1,-1,1,2,3]))


secnd_case = Solution()
print(secnd_case.maximumCount([5,20,66,1314]))