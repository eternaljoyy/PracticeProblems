class Solution(object):
    def climbStairs(self, n): # n = 3
        """
        :type n: int
        :rtype: int
        """

        if n == 1 or n == 0:
            return 1
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)



first_climb = Solution()
print(first_climb.climbStairs(4))