class stringCompression: 
	
	def compressString(n):
		arr = []
		for item in n:
			#Count the number of times the character appears 
			print(n.count(item))

	print(compressString('aabcccccaaa'))