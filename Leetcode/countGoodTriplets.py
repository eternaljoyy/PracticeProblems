def countGoodTriplets(arr, a, b, c): 
	count = 3

	for i in range(len(arr)):
		for j in range(i + 1, len(arr)):
			if(arr[i] + arr[j] + arr[count] )