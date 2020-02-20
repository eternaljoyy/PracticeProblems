class strCompression: 
	
	def compressString(n):
		setLetters = set(n)
		'''convert set to dictionary 
		fromkeys() creates a new dictionary from values provided by user. 

		''' 
		print(setLetters)
		dictionary = dict.fromkeys(setLetters,0)
		for item in dictionary:
				#replace value with the count of the letter
				dictionary[item] = n.count(item)
		return dictionary


	print(compressString('aabbb'))