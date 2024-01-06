def findDifference(nums1, nums2): 
	''' 
	- Return list of 2 arrays containing distinct integers 

	==========================================================

	- go through nums1, check if those integers are present in nums2
	(and vice versa)  

	==========================================================

	- Runtime complexity: O(N)
	''' 

	answer = [[], []]

	for i in range(len(nums1)):
		if nums1[i] not in nums2 and nums1[i] not in answer[0]:
			answer[0].append(nums1[i])


	for j in range(len(nums2)):
		if nums2[j] not in nums1 and nums2[j] not in answer[1]:
			answer[1].append(nums2[j])


	return answer 


#Tests 
print(findDifference([1,2,3], [2,4,6]))
print(findDifference([1,2,3,3], [1,1,2,2]))