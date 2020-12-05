def birthdayCakeCandles(candles):
	maxVal = max(candles)
	count = 0

	for item in candles:
		if(item >= maxVal):
			count += 1 
	return count

print(birthdayCakeCandles([3, 2, 1, 3]))