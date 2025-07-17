class Solution:
    def searchInsert(self, nums, target):

        '''
        nums = [0, 3, 5, 6], target = 1 
                R  L,M          
        -------------------------------
        Approach: 

        use binary search to search through the array trying to
        check whether the target is present. If its not present,
        return where in the array it would've been. 
        '''
    

        left, right = 0, len(nums)-1


        while left <= right: 

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1 
            else:
                left = mid + 1
        return left 
        


#testcases 
first_example = Solution() 
print(first_example.searchInsert([1,3,5,6], 7))
