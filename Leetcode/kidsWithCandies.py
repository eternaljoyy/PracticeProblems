def kidsWithCandies(candies, extraCandies):  
	#base case A) empty list 
	if(candies == []):
		return candies

	newArr = []
	flag = False
	# count = 0

	for item in range(len(candies)):
		if(candies[item] + extraCandies >= max(candies)):
			newArr.append(True)
		else:
			newArr.append(False)
			continue 
	return newArr

print(kidsWithCandies([3], 1))
print(kidsWithCandies([12,1,12], 10))
print(kidsWithCandies([4,2,1,1,2], 1))
print(kidsWithCandies([2,3,5,1,3], 3))