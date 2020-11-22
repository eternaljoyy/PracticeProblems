def toGoatLatin(S):
	newSentence = S.split(" ")
	vowels = 'aeiou'
	count = 0 
	newArr = []
	
	for item in range(len(newSentence)):
		s = ''
		count += 1

		if((newSentence[item][0] in vowels.lower()) or (newSentence[item][0] in vowels.upper())):
			s += newSentence[item] + 'ma' + ('a' * count)
			newArr.append(s)
		else: 
			s += newSentence[item][1:] + newSentence[item][0] + 'ma' + ('a' * count)
			newArr.append(s)
	return ' '.join(newArr)


print(toGoatLatin("I speak Goat Latin"))
print(toGoatLatin("The quick brown fox jumped over the lazy dog"))