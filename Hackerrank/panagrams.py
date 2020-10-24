from string import ascii_lowercase

def pangrams(s):
	alphabet = set(ascii_lowercase)
	newS = s.replace(" ", "")
	newStr = set(newS.lower())
	
	if(len(alphabet) == len(newStr)):
		return 'pangram'
	else:
		return 'not a pangram'

print(pangrams('We promptly judged antique ivory buckles for the prize'))