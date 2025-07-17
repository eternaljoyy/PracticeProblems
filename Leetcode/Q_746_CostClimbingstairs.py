class Solution(object):
    def minCostClimbingStairs(self, cost):  
        ''' 
        ex A): 
         cost = [10, 15, 20, top]
                 0    1   2 

        min_cost = cost[0]

        step 0: 
            cost to reach step 0 = 0 (since we can start from this spot)


        step 1: 
            cost to reach step 1 = 0 (0 since we can start from this spot!)
                             

        top: 
        min_cost =  min(cost at step 2+ min_cost to step 2, cost at step 1 + min_cost to step 1)


        min_cost[i] = min(cost[i-1]+ min_cost[i-1], cost[i-2]+ min_cost[i-2]) 



        step 2: 

        min_cost[2] = min(cost[1] + min_cost[1], cost[0]+ min_cost[0])
                    = min(15 + 0, 10+0)
        min_cost[2] = 10 


        top: 

        min_cost[len(cost)+1] = min(cost[2] + min_cost[2], cost[1] + min_cost[1])
                 = min(20+10, 15+0)
                 = min(30, 15)
                 = 15 
        '''  


        min_cost = [0 for i in range(len(cost)+1)]

        min_cost[0] = 0 
        min_cost[1] = 0


        for i in range(2, len(cost)+1):
            min_cost[i] = min(cost[i-1] + min_cost[i-1], cost[i-2] + min_cost[i-2])
        return min_cost[len(cost)]
        


        
              
stairs_firstset = Solution()
print(stairs_firstset.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))

