class Solution:
    def search(self, nums, target):

        start = 0 
        end = len(nums)-1

        while start <= end: 
            midpoint = (start + end) // 2

            if (nums[midpoint] == target):
                return midpoint 
            elif nums[midpoint] > target:
                end -= 1
            else:
                start += 1 
        return -1 




bs_one = Solution() 
print(bs_one.search([-1,0,3,5,9,12], 9))

bs_two = Solution()
print(bs_two.search([-1,0,3,5,9,12], 2))

bs_three = Solution()
print(bs_three.search([5], 5))