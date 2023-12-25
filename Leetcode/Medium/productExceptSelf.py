def productExceptSelf(nums): 
	''' 
	  - go through the array, keeping track of current index 
	  - go through array again, trying to find the product 
	  - return the product  

	  ======================================================== 
	  -> Runtime complexity: O(N^2)
	  -> Spacetime complexity: O(N) 

	  **TODO: Do this in O(N^2) time 
	'''

	answer = [] 

	for i in range(len(nums)):
		product = 1 

		for j in range(len(nums)): 
			if i != j:
				product *= nums[j]
		answer.append(product) 
	return answer 


#Tests 
print(productExceptSelf([-1,1,0,-3,3]))
print(productExceptSelf([1,2,3,4]))