def canPlaceFlowers(flowerbed, n):
	''' flowerbed: array 
		n = number of flowers to be added
		
		Cannot be placed when: 
		- First element == 0 and second element == 1 -> (i + 1) == 1
		- Last element == 0 and second-last element == 1 -> (i-1) == 1
		- middle element == 0 and (i -1) == 1 and (i+1) == 1
	
		Can be placed when:
		flowerbed can be placed if i - 1 ==0 and if i + 1 == 0
		OR also if its the first element and its == 0 (Need to check if i + 1 == 0)
		OR also if its the last element and its == 0 (need to check if i - 1 == 0)
	'''  
	for i in range(len(flowerbed)): 
		#Base case A) one element (can be either 0 or 1)
		if(len(flowerbed) == 1):


		#check when it cannot be placed 
		if(flowerbed[i] == 1):
			if(i == 0 and flowerbed[i + 1] == 1 and flowerbed[i] == 0):
				continue 
			elif (i == len(flowerbed)-1 and flowerbed[i -1] == 1 and flowerbed[i] == 0):
				continue
			else:
				if(flowerbed[i] == 0 and flowerbed[i+1] == 1 and flowerbed[i-1] ==1):
					continue
		elif (flowerbed.index(flowerbed[i]) != 0 and flowerbed.index(flowerbed[i]) != len(flowerbed)-1 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
			flowerbed[i] = 1
		elif (flowerbed[i] == 0 and flowerbed.index(flowerbed[i]) == 0 and flowerbed[i + 1] == 0):
			flowerbed[i] = 1
		elif (flowerbed[i] == 0 and flowerbed.index(flowerbed[i]) == len(flowerbed)-1 and flowerbed[i -1] ==0):
			flowerbed[i] = 1
