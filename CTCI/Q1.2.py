class Reverse: 
	'''Reverse the string 
	TODO: Account for whitespace
	'''
	def reverseStr(n):
		arr = []
		#Loop through the empty array 
		for item in range(len(n)-1, -1, -1):
			#Append item to list 
			arr.append(n[item])
		#join method concatonates strings together
		return ''.join(arr)

	print(reverseStr('hello'))