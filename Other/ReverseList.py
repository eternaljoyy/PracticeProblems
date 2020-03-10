class reverse: 
	#Write a program which can reverse a list..  
	''' 
	Assumption: contains no duplicates. 
	'''
	def reverseList(nums):
		#make another list 
		newArr = [] 
		#Loop backwards 
		for num in reversed(nums):
			print(num)

	reverseList([1,2,3])