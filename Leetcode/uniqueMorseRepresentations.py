def uniqueMorseRepresentations(words):
	#dicitonary with morse code mappings 
	wordMappings = {'a': ".-", 'b':"-...", 'c':"-.-.", "d":"-..", 'e': ".", 'f':"..-.",
					'g': "--.", 'h': "....", 'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..", 
					'm': "--", 'n':"-.",'o': "---", 'p': ".--.", 'q': "--.-", 'r': ".-.", 's': "...", 
					't': "-", 'u': "..-", 'v': "...-",
					'w': ".--", 'x': "-..-", 'y': "-.--", 'z': "--.."} 

	#list which will hold the unique transformations 
	transformations = set()

	for item in words: 
		for char in item:
			if(char in wordMappings):
				item = item.replace(char, wordMappings[char])
		transformations.add(item)
	return len(transformations)



print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
