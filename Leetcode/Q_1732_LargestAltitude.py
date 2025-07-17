def largestAltitude(gain):
    """
    N = number of items in the gain array 

    Runtime Complexity: O(N)

    Spacetime Complexity: O(N+1) -> O(N)
    """

    altitude = [0] 
    prefix_sum = 0

    for index in range(len(gain)):
        prefix_sum += gain[index]
        altitude.append(prefix_sum)
    return max(altitude)


# Testcases 
# testcase 1
gain_one = [-5,1,5,0,-7] 
print(largestAltitude(gain_one)) 

# testcase 2 
gain_two = [-4,-3,-2,-1,4,3,2]
print(largestAltitude([-4,-3,-2,-1,4,3,2]))
