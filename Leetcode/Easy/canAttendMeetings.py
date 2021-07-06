def canAttendMeetings(intervals): 
    '''    
    Assumption: 
        - length of array > 1

    ======================================================
    - have a boolean which can represent the 
    - Sort the intervals array 
    - Go through the array 
     -> check the meeting times, if they overlap then you cannot attend all the 
    meetings, then return False  

    ==================================================== 

    Examples: 

    Example 1:
            Input:
            [[0,30],[5,10],[15,20]]
            
            Output:
            false 

    Example 2:
            Input:
            [[7,10],[2,4]]

            Output:
            true 

    =====================================================
    
    Time complexity: O(N) 

    '''

    sortedIntervals = sorted(intervals) 
    
    #boolean representing whether meeting times overlap + if someone can attend meeting or not 
    canAttend = False


    for item in range(len(sortedIntervals)-1):
        diff = sortedIntervals[item][1] - sortedIntervals[item+1][0]
        print(diff)

        if(diff < 0):
            canAttend = True
        else:
            return False
    return canAttend


print(canAttendMeetings([[0,30],[5,10],[15,20]]))
print(canAttendMeetings([[7,10],[2,4]]))