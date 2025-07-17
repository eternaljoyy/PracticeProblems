def distributeCandies(candyType):
    """
        :type candyType: List[int]
        :rtype: int
    """ 

    '''  
    N = # of items in the candyType array 

    Approach: 
    Go through the candy types, getting the different types of candies 
    and their amount. From there, she can only eat N/2 candies in total. 
    From that available pool of candies to eat, find the maximum number
    of different/unique types of candies she can eat. 

    M = # of items in the set

    Spacetime Complexity:  
    - creating a new hashmap containing all elments from candyType, 
    resulting in O(N) spacetime complexity. 

    Runtime Complexity: 
    - going through the candyType array one by one, resulting in 
    runtime comp. of O(N)  
    '''
    
    # set stores different types of candies
    candies = set() 


    for item in range(len(candyType)):
        candies.add(candyType[item])
    return min(len(candyType)//2, len(candies))




print(distributeCandies([1,1,2,2,3,3]))
print(distributeCandies([6, 6, 6, 6]))
print(distributeCandies([1,1,2, 3]))