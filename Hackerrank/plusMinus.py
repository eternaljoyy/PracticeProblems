def plusMinus(arr): 
	positiveElem = 0
	negativeElem = 0
	zeroElem = 0 

	for item in arr:
		if(item > 0):
			positiveElem += 1
		elif (item < 0):
			negativeElem += 1 
		else: 
			zeroElem += 1 
	print(round(positiveElem/len(arr), 6))
	print(round(negativeElem/len(arr), 6))
	print(round(zeroElem/len(arr), 6)) 

plusMinus([1, 1, 0, -1, -1])