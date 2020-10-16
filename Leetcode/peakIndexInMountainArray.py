def peakIndexInMountainArray(arr): 
	#base case A) emty array 
	if(arr == None):
		return 

	#Loop through array 
	for item in range(0, len(arr)):
		if(arr[item - 1] < arr[item] and arr[item] > arr[item + 1]):
			return arr.index(arr[item])

print(peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19]))