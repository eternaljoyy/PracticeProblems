def makeGood(s):

	newStr = list(s)
	goodStr = []

	for i in range(len(newStr)-1):
		if(ord(s[i]) - ord(s[i+1]) == 32):
			continue
		else:
			goodStr.append(newStr.pop(i))
	return ''.join(goodStr)

print(makeGood("abBAcC"))
print(makeGood("leEeetcode"))