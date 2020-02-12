class stringCompression: 
	
	def compressString(n):
		string = ''
		arr = []
		count = 0 
		for item in n:
			if(n.index(item) == 0):
				count+=1
				string = item + str(count)
				arr.append(string)
		return arr


	print(compressString('aabcccccaaa'))