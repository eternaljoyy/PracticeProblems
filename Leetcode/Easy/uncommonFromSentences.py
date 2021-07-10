def uncommonFromSentences(s1, s2):
	''' 
	- go through both the strings 
	- try to find words that only appear in one string but not the other (and
	it must appear in that string only once)
	''' 

	#split the strings into a list 
	splitStr1 = s1.split()
	splitStr2 = s2.split()
	
	#list to store words that are uncommon
	uncommonWords = [] 

	for char in splitStr1:
		if (splitStr1.count(char) == 1 and char not in splitStr2):
			print(char)
			uncommonWords.append(char)
	
	for otherChar in splitStr2: 
		if (splitStr2.count(otherChar) == 1 and otherChar not in splitStr1):
			uncommonWords.append(otherChar) 
	
	return uncommonWords


print(uncommonFromSentences("this apple is sweet", "this apple is sour"))
print(uncommonFromSentences("apple apple", "banana"))
