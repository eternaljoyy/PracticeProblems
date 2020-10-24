from string import ascii_lowercase

def pangrams(s):
	if(s == None or s == ''):
		return   

	alphabet = set(ascii_lowercase)
	strNoSpaces = s.replace(" ", "")
	newStr = set(strNoSpaces.lower())
	
	if(len(alphabet) == len(newStr)):
		return 'pangram'
	else:
		return 'not pangram'

print(pangrams('We promptly judged antique ivory buckles for the prize'))