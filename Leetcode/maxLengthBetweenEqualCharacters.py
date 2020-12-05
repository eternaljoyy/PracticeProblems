def maxLengthBetweenEqualCharacters(s): 
	lastIndex = len(s) - 1
	maxVal = -1

	#loop through the string, using 2 pointers
	for i in range(len(s)):
		while(i < lastIndex):
			if(s[i] != s[lastIndex]):
				lastIndex -= 1
			else:
				maxVal = max(maxVal, lastIndex - i - 1)
		lastIndex = len(s) - 1
	return maxVal



'''print(maxLengthBetweenEqualCharacters("cbzxy"))
print(maxLengthBetweenEqualCharacters("cabbac"))
print(maxLengthBetweenEqualCharacters("abca"))
print(maxLengthBetweenEqualCharacters("aa"))'''
print(maxLengthBetweenEqualCharacters("ojdncpvyneq"))