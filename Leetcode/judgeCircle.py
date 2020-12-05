def judgeCircle(moves): 
	x = 0 
	y = 0 

	if(moves == ""):
		return True

	for i in moves:
		if(i == 'L'):
			x += 1
		elif (i == 'R'):
			x -= 1
		elif (i == 'D'):
			y -= 1
		else:
			y += 1 
	return x == 0 and y == 0

print(judgeCircle("LDRRLRUULR"))