import math

def generate(numRows):
	nums = [[]] * numRows
	print(nums)

	for i in range(numRows):
		nums[i].append(math.pow(2, i))
	return nums

print(generate(5))