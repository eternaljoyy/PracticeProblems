def toLowerCase(str):
	newStr = ''

	for item in range(len(str)):
		if(str[item].isupper()):
		#get ASCII Code of uppercase character
			ASCIICode = ord(str[item]) + 32 
        	lowerCaseChar = chr(ASCIICode)
        	newStr = newStr + lowerCaseChar
        else:
        	newStr = newStr + str[item] 
	print(newStr)