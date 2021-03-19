def reverseStr(strOfNums):
	strInOrder = "" 

	for item in range(len(strOfNums)-1, -1, -1):
		strInOrder += strOfNums[item]
	return strInOrder


def thousandSeparator(n):
	""" 
	- going through the string backwards, for every 3rd
	digit, place a dot 
	  - count the number of digits as you go along 
		- making sure its equal to 3 
	""" 
	newN = str(n)

	#check if theres 3 characters or less
	if(len(newN) <= 3):
		return str(n) 

	newStr = ""
	#this variable keeps track of the number of digits	
	count = 1 

	#O(N) runtime
	for index in range(len(newN)-1,-1,-1): 
		if(count == 3 and index != 0):
			newStr += newN[index]
			newStr += "."
			index += 2
			count = 1
		#reached the end of the string 
		elif(index == 0):
			newStr += newN[index]
			count += 1
			return reverseStr(newStr)
		else:
			newStr += newN[index]
			count += 1 


print(thousandSeparator(987))
print(thousandSeparator(1234))
print(thousandSeparator(123456789))