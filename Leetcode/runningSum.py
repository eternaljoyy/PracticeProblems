def runningSum(nums):
	#base case A) Empty list or list has 1 element 
	if(len(nums) == 1 or nums == []):
		return nums 

	count = 0
	for i in range(len(nums)):
	# sum the current value of nums w/ previous value of count 
		count = count + nums[i]
		nums[i] = count 
	return nums 

print(runningSum([1,2,3,4]))
print(runningSum([1,1,1,1,1]))
print(runningSum([3,1,2,10,1]))