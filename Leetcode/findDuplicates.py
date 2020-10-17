def findDuplicates(nums): 
	newArr = []
	# O(n) runtime & extra space 

	#base case A) empty list 
	if(nums == []):
		return 

	count = 0 
	for item in range(len(nums)):
		if(nums.count(nums[item]) > 1):
			newArr.append(nums[item])
	print(set(newArr)) 

findDuplicates([4,3,2,7,8,2,3,1])