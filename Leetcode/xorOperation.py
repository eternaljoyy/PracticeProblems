def returnBinary(arr):
	count = arr[0]

	for num in range(1, len(arr)): 
		count = count ^ arr[num]
	print(count) 

def xorOperation(n, start):
	newArr = []

	#make the array 
	for item in range(n):
		newArr.append(start + 2*item)
	returnBinary(newArr)  	

xorOperation(5, 0)