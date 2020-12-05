def isIsomorphic(s, t):  
	''' 
	- A value can ONLY map to ONE key 
	 
	base cases: 
	  - both have length of 1 (return true)
	  - both are empty strings (return true)
	  - one of them are empty strings (return true)

	''' 
	if(len(s) == 1 and len(t) == 1):
		return True
	elif (s == "" and t == ""):
		return True 
	elif (s == "" and len(t) == 1):
		return True 
	else:
		if(t == "" and len(s) == 1):
			return True


	wordDictS = {}
	wordDictT = {} 
	bool = False 


	#Add the words to the dictionary 
	for keyS, keyT in zip(s, t):
		wordDictS[keyS] = keyT
		wordDictT[keyT] = keyS


	for itemT, itemS in zip(t, s):
		if(wordDictS[itemS] == itemT and wordDictT[itemT] == itemS):
			bool = True
		else:
			return False 
	return bool


print(isIsomorphic("foo", "bar"))
print(isIsomorphic("egg", "add"))
print(isIsomorphic("xyx", "bai"))
print(isIsomorphic("paper", "title"))
print(isIsomorphic("", ""))
print(isIsomorphic("f", "g"))
print(isIsomorphic("", "g"))
print(isIsomorphic("ab", "aa"))