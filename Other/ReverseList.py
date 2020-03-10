class reverse: 
	#Write a program which can reverse a list.. (while preserving the order) 
	#todo: figure out a way to reverse the array in-place 
	def reverseList(nums):
		#make another list 
		newArr = [] 
		#Loop backwards 
		for num in reversed(nums):
			newArr.append(num)
		return newArr

	print(reverseList([1,2,3,4,3]))