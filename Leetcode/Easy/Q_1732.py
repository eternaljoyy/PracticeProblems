def largestAltitude(gain): 
	''' 
	- Find & return the highest altitude of a point  

	===================================================

	Approach: 
	 - make new array - altitude 
     - go through the gains array, calculating the altitude by 
     finding the prefix sum 
       - add prefix sum into new array 
     - find and return the maximum sum from altitude array  

     ===================================================
	
	N = Length of gain array 

	Time Complexities: 
	  - Runtime complexity: O(N)
	  - Spacetime complexity: O(N)
	''' 

	altitude = [] 
	altitude.append(0)
	altitude.append(gain[0])

	altitudeIndex = 0 
	prefixSum = 0 


	for item in range(1, len(gain)): 
		prefixSum = gain[item] + altitude[item]

		altitude.append(prefixSum)
	return max(altitude) 


print(largestAltitude([-5,1,5,0,-7]))
print(largestAltitude([-4,-3,-2,-1,4,3,2]))


