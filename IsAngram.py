def makeDictionaries(s, t):
	'''
	purpose: go through each string, then add that word into 
	a dictionary. 
	'''   
	firstDict = {}
	secondDict = {}
	
	for itemS in s:
		firstDict[itemS] = s.count(itemS)
	print(firstDict) 

	for itemJ in t:
		secondDict[itemJ] = t.count(itemJ) 
	print(secondDict)

	isAnagram(firstDict, secondDict)


def isAnagram(s, t):
	'''  
	Assumption: str1 and str2 will only contain lowercase alphabets

	purpose: return true if str1 & str2 are angrams of each other 
	Note: str1, str2 are both words, or a phrase
	'''   

	print(s == t)


makeDictionaries('anagram', 'nagaram')
makeDictionaries('cinema', 'iceman')
makeDictionaries('ice&man', 'cine&ma')
