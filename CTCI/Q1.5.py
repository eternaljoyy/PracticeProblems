class stringCompression: 
	
	def compressString(n):

		string = ''
		arr = sorted(n)
		count = 0 

		for i in range(0, len(n)-1):
			for j in range(1, len(n)):
				if(n[i] == n[j]):
					count+=1
		return count

	print(compressString('aabcccccaaa'))