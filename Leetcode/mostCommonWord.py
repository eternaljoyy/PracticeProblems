def mostCommonWord(paragraph, banned):
	
	#Dont account for the punctuation 
	for item in '''!()-[]{};:'"\,<>./?@#$%^&*_~''':
		paragraph = paragraph.lower().replace(item, " ")
	#split the sentence
	splitSentence = paragraph.split()

	words = {}

	#Add all of the words (that arent in banned dictionary) into it
	for item in splitSentence: 
		if(item not in banned): 
			if(item not in words): 
				words[item] = 1
			else:
				words[item] += 1

	#find the maximum occurence of the word
	count = max(words.values())
	for key,val in words.items():
		if(val == count):
			return key

print(mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', ['hit']))
print(mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))