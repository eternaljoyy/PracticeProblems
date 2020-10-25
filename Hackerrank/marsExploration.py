def marsExploration(s):  

	#Base case A) Empty string 
	if(s == ''):
		return 0

	count = 0 
	
	for item in s:
		if(item != 'S'):
			if(item != 'O'):
				count += 1
	return count  

print(marsExploration('SOSSOSSOS'))