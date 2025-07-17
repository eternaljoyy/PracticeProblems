class Solution(object):
    def climbStairs(self, n): # n = 3
        """ 
        Runtime Complexity: O(N) 

        Spacetime Complexity: O(N)
         - making an array with n elements, and this scales linearly 
         as the input grows 
        """

        arr = [0 for i in range(n+1)]
        arr[0] = 1
        arr[1] = 1 


        for i in range(2, n+1):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[n]



first_climb = Solution()
print(first_climb.climbStairs(5))