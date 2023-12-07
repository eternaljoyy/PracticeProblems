def can_attend_meetings(intervals): 
    ''' 
    - sort intervals based on starting time and check if end-start times 
    conflict 
        -> end/start times conflict if end-time >= start-time 
        -> check the previous meetings' end-time with the next meetings start time 

    =========================================================================

    Runtime Complexity: O(NlogN) -> due to the sorting of the array 
    Space Complexity: O(1) -> not using any extra data structure 
    '''  

    sortedIntervals = sorted(intervals)

    for i in range(len(sortedIntervals)-1):
        if sortedIntervals[i][1] >= sortedIntervals[i+1][0]:
            return False 
    return True 


print(can_attend_meetings([[0,30],[5,10],[15,20]])) 
print(can_attend_meetings([[7,10],[2,4]]))