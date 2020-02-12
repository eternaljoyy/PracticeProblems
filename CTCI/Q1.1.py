class UniqueSolution: 
	#Determine if input str is unique 
	'''
	A character is unique only if it occurs once 
	ex: str LETTER is not unique since 'T' & 'E' occur more than once 
	'''
	def uniqueStr(userInput):
		#loop through the alphabet (uppercase)
		for uppercaseLetter in userInput:
			if(userInput.count(uppercaseLetter) != 1):
				return False 
			else:
				return True 


	ret = uniqueStr('LETTER')
	print(ret)