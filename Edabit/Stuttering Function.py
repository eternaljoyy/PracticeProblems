
def stutter(word):
	'''Note: [n:m] returns the n'th 
	to the m'th part of string (up to but not including the last)'''
	return word[:2] + "... " + word[:2] + "... " + word + "?"