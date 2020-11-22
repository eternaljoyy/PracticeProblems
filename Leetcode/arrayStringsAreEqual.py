def arrayStringsAreEqual(word1, word2):
	strA = ''
	strB = ''

	for i in range(len(word1)):
		strA += word1[i]

	for j in range(len(word2)):
		strB += word2[j]

	return strA == strB

print(arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))
print(arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))
        