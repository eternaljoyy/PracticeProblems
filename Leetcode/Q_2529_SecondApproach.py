class Solution:
    def maximumCount(self, nums):
        ''' 
        Going through the array one by one and checking whether
        the number is negative or positive.  

        [-3,-2,-1,0,0,1,2] 

        -> # neg = first index of positive number ( <0 )
        -> # pos = len(array) - index of first positive number ( >0)
        ------------------------------------------------------- 
        N = # of items in the nums array 

        Runtime Complexity: 
        Spacetime Complexity: O(1)
        '''

        neg = 0

        left = 0 
        right = len(nums) - 1 

    





# testcase 
first_case = Solution()
print(first_case.maximumCount([-2,-1,-1,1,2,3]))


secnd_case = Solution()
print(secnd_case.maximumCount([5,20,66,1314]))