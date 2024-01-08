def mergeAlternatively(word1, word2): 
	'''  
	Approach: 

	 - add first letter from word1 into new string
	 - go through word1 and word2 using pointers, alternating 
	 b/w the two 
	 - if youve reached end of word1 or word2, then
	 slice of the other word and add it to new string 
	- return the new string 

	============================================== 
	
	N = length of word1
	M = length of word2 

	**TODO ~ Time Complexities: 
      - Runtime Complexity: 
      - Space Complexity: O(N + M)
	'''


	alternateStr = "" 

	#pointers for word1 and word2, respectively 
	ptr1 = 0 
	ptr2 = 0 

	alternateStr += word1[ptr1]
	ptr1 += 1 

	#flag used to keep track of which word to alternate with  
	#False - go to word1 
	#True - go to word2 
	word1Flag = False 


	while len(alternateStr) != len(word1) + len(word2): 
		
		if ptr1 == len(word1):
			alternateStr += word2[ptr2:] 
		elif ptr2 == len(word2):
			alternateStr += word1[ptr1:] 
		elif word1Flag == False:
			alternateStr += word2[ptr2] 
			ptr2 += 1 
			word1Flag = True 
		else: 
			alternateStr += word1[ptr1]
			ptr1 += 1 
			word1Flag = False 
	return alternateStr 


print(mergeAlternatively("abc", "pqr"))
print(mergeAlternatively("ab", "pqrs"))
print(mergeAlternatively("abcd", "pq"))