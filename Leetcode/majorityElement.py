import math 

def majorityElement(nums):        
	half = math.floor(len(nums)/2)

	#approach 1 
	for i in range(len(nums)):
		if(nums.count(nums[i]) > half):
			return nums[i]

print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))