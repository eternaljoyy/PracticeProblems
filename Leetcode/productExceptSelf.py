def productExceptSelf(nums): 
	'''  
	(for every element except the first and last ones):
	- while on current element, start from the very beginning,
	finding the product of each element (excluding the current)
	
	(first element):
	- go through the array, finding the product of every other 
	element 

	(last element):
	- go through the arrray, finding the product of every other
	element 
	'''   
	prod = 1
	ptr1 = 0 
	newArr = [] 

	newArr = nums[:]

	for current in range(len(nums)):
		print(newArr)

		prod = 1
		ptr1 = 0 

		while(ptr1 < len(nums)):

			if(current != 0 and current != len(nums)- 1):
				if(ptr1 != current):
					prod *= nums[ptr1]
					ptr1 += 1 
				else:
					ptr1 += 1
			
			elif(current == 0):
				if(ptr1 != current):
					prod *= nums[ptr1]
					ptr1 += 1   
				else:
					ptr1 += 1
			else: 
				if(current == len(nums)-1):
					if(ptr1 != current):
						prod *= nums[ptr1]
						ptr1 += 1 
					else:
						break 
		newArr[current] = prod
	return newArr 


productExceptSelf([1,2,3,4])
'''print(productExceptSelf([1, 3, 2]))
print(productExceptSelf([2,6,9,10]))''' 