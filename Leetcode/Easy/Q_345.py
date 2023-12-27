def reverseVowels(s): 
	''' 
	 - make an array of strings 
	 - have 2 pointers of the string 
	   - one at the beginning 
	   - one at the end 
	 - switch them both if theyre both vowels, 
	 otherwise increment/decrement one that isnt the vowel 
	 - return the resulting string   

	  ======================================================== 
		  - Time Complexity: O(N)
		  - Space Complexity: O(N)**
	'''  

	# check if empty string 
	if s == '' or s == ' ':
		return s


	firstPtr = 0 
	secondPtr = len(s)-1
	splitStr = list(s)

	vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


	while(firstPtr < secondPtr):

		if splitStr[firstPtr] not in vowels:
			firstPtr += 1
		elif splitStr[secondPtr] not in vowels:
			secondPtr -= 1 
		else: 
			splitStr[firstPtr], splitStr[secondPtr] = splitStr[secondPtr], splitStr[firstPtr]
			firstPtr += 1
			secondPtr -= 1
	return ''.join(splitStr)


#Test cases 
print(reverseVowels('hello'))