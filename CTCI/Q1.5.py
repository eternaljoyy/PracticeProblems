class strCompression: 
	
	def compressString(n):
		'''
		Try looping through the letters in n, count the number of times word 
		occurs and place that in a dictionary (as key value pairs). 
		'''
		setLetters = set(n)
		'''convert set to dictionary 
		fromkeys() creates a new dictionary from values provided by user. 

		''' 
		print(setLetters)
		dictionary = dict.fromkeys(setLetters,0)
		for item in dictionary:
			for item in setLetters:
				#replace value with the count of the letter
				dictionary[item] = n.count(item)
		return dictionary


	print(compressString('aabcccccaaa'))