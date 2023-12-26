def canPlaceFlowers(flowerbed, n): 
	''' 
	 - go through array 
	  - before placing flowerbed, check if the adjacent indices have a 1; 
	  if not then place flower (decrement n by 1)
	  - otherwise, keep going through array 
	 - return whether all flowers have been placed or not (check value
	 of n) 

	 =========================================================

	 Runtime Complexity: O(N)
	 Space Complexity: O(1)
	'''  

	#base case 1 -- no flower to be added 
	if n == 0:
		return True 

	#base case 2 -- single empty plot of land 
	if len(flowerbed) == 1:
		if flowerbed[0] == 0:
			return True
		else:
			return False 

	canPlaceFlower = False   

	
	for flower in range(len(flowerbed)):

		if flowerbed[flower] == 0:
		   	if flower == 0 and flowerbed[flower+1] != 1:
		   		flowerbed[flower] = 1
		   		n -= 1 
		   	elif flower == len(flowerbed)-1 and flowerbed[flower-1] != 1:
		   		flowerbed[flower] = 1
		   		n -= 1 
		   	else:
		   		if flowerbed[flower-1] != 1 and flowerbed[flower+1] != 1: 
			   		flowerbed[flower] = 1
			   		n -= 1

		if n == 0:
			return True  

	if n == 0:
		return True 
	return False 


print(canPlaceFlowers([0,0,0,0,0], 4))
print(canPlaceFlowers([1,0,0,0,1], 1))
print(canPlaceFlowers([1,0,0,0,1], 2))
print(canPlaceFlowers([1,0,1,0,1,0,1], 0))
print(canPlaceFlowers([1,0,0,0,1,0,0], 2))