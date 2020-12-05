def removeCharacters(string):
	''' Returns a string without the special characters
		- check if each character is a letter, if so then add it string
	''' 
	newStr = ''

	for char in string:
		if(char.isalnum()):
			newStr += char
	reverseStr(newStr)


def reverseStr(string):
	''' Purpose: returns true if str is the same backwards and reversed, 
		otherwise return false. 

		NOTE: 
		- Does not take special characters into 
		consideration.  
		- Treat uppercase & lowercase characters the same way 
		(ex: 'A' is the same as 'a')

		Input: string of characters; will include special characters (ex: 
		commas, ?, spaces, etc).  
	'''    

	print(string.lower() == ''.join(reversed(string.lower())))

removeCharacters('Hello World')
removeCharacters('Red rum, sir, is murder')
removeCharacters('Programcreek is awesome')
