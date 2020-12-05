
def decompressRLElist(nums): 
	#Base case A) Empty list 
	if (nums == []):
		return nums  

	compressedList = []

	for i in range(len(nums)):
		try:
			if(nums[2*i] and nums[2*i + 1] in nums):
				freq = nums[2*i]
				val = nums[2*i + 1]
				#compress the list 
				compressedList += [val]* freq 
		except IndexError: 
			#exit the loop 
			break
	return compressedList 

print(decompressRLElist([1,2,3,4]))