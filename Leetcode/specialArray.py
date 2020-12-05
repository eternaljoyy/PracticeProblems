def func(number, count):
	if(number == count):
		return count 

def specialArray(nums):
	#sort the array
	sortedNums = sorted(nums)
	#keeps track of number of times something occurs 
	count = 0
	
	for i in range(1, len(nums)-1):
		for item in range(0 , len(sortedNums)):
			number = i
			if(nums[item] > number):
				count += 1 
				number += 1
			else:
				number += 1
    func(number, count)

specialArray([3,5])