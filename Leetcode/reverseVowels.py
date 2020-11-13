def reverseVowels(s):

	#base case A) empty string or has blank space
	if(s == '' or s == ' '):
		return s

	newList = list(s)
	ptr1 = 0
	ptr2 = len(newList)-1
	lowerVowels = 'aeiou'
	upperVowels = 'AEIOU' 

	while(ptr1 < ptr2):
		if((newList[ptr1] in lowerVowels) or (newList[ptr1] in upperVowels)): 
			if(((newList[ptr2] in lowerVowels) or ((newList[ptr2] in upperVowels)))):
				newList[ptr1], newList[ptr2] = newList[ptr2], newList[ptr1]
				ptr1 += 1
				ptr2 -= 1 
			else:
				#move pointer 2 (since it is not a vowel)
				ptr2 -= 1 
		elif((newList[ptr2] in lowerVowels) or (newList[ptr2] in upperVowels)):
			ptr1 += 1 
		else:
			ptr1 += 1
			ptr2 -= 1 
	return ''.join(newList)

print(reverseVowels('Hello'))
print(reverseVowels('leetcode'))
