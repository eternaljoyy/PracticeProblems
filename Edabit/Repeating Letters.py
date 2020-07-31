def double_char(txt):
	newStr = '' 
	for item in txt:
		if(txt.count(item)!= 0):
			newStr += item*2 
	return newStr