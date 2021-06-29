def maxProductDifference(nums):
    ''' 
    - find the maximum product of the 2 pairs of numbers in the array  
        -> find the maximum number in the array 
        -> find the second maximum number in the array 
    - find the minimum product of the 2 paris of numbers in the array  
        -> find the minimum number in the array 
        -> find the second minimum number in the array  
    - can sort the elements to find the pair of the maximum and minimum operations  
    - compute then return the maximum product of the pair of the numbers 
    ''' 
 
    sortedArr = sorted(nums) 

    minElement = sortedArr[0]
    maxElement = sortedArr[len(sortedArr)-1] 

    secondMinElem = sortedArr[1]
    secondMaxElem = sortedArr[len(sortedArr)-2]

    return (maxElement * secondMaxElem) - (minElement * secondMinElem)


print(maxProductDifference([5,6,2,7,4]))
print(maxProductDifference([4,2,5,9,7,4,8]))