class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        Approach: 

        - Go through the array, keeping track of the maximum average 
        along the way. After youre done going through the array, 
        return the maximum average value.  

        ----------------------------------------------------------- 
        Runtime Complexity: 
        - Going through every item in whole array in 1 pass, resulting 
        in a runtime of O(N). 

        **Spacetime Complexity: 
        - O(k), where we sum the first k elements 
        """   

        ''' 
        [1,12,-5,-6,50,3], k = 4 
        '''


        # window sum of the k elements 
        window_sum = sum(nums[:k])
        max_average = window_sum/k

        for item in range(1, len(nums)-(k-1)): # item = 1
            window_sum += nums[(k - 1) + item] - nums[item-1] # win_sum = 
            max_sum = max(max_average, window_sum/k)

        return max_average



# testcases 
first_maxAvg = Solution() 
print(first_maxAvg.findMaxAverage([1,12,-5,-6,50,3], 4))

second_maxAvg = Solution()
print(second_maxAvg.findMaxAverage([5], 1))