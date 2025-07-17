class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        
        # find and merge intervals 
        # after merging, count the total 
        # number of points remaining from the start to the end 