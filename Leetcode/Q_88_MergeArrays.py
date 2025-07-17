def merge(nums1, m, nums2, n):
    """
    Example A): 
     nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3;  

     new_nums1 -> [1, 2, 2, 3, 5, 6] 

    --------------------------------------------------------
    Approach: 
     - Make use of pointers to go through the arrays, comparing 
     each element one by one, checking which one is greater and
     then adding that to the back of the nums1 array. 

    --------------------------------------------------------
    Runtime Complexity:  
    N = # elements in nums2, M = # elements in nums1 
    - going through both nums1 and nums2, resulting in a runtime
    complexity of O(N + M). 

    Spacetime Complexity: 
     - Because we arent creating any additional data structure, 
     the time complexity is O(1) (since we are modifying nums1 in-place).
    """ 

    # Insert position in nums1
    index_nums1 = m + n - 1  


    while n > 0 and m > 0:
        if nums2[n-1] > nums1[m-1]:
            nums1[index_nums1] = nums2[n-1]
            n -= 1
        else:
            nums1[index_nums1] = nums1[m-1]
            m -= 1
        index_nums1 -= 1
    

    # If nums2 still has remaining elements to check 
    while n > 0:
        nums1[index_nums1] = nums2[n-1]
        n -= 1
        index_nums1 -= 1
    return nums1    


print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(merge([1], 1, [], 0)) 
print(merge([0], 0, [1], 1))