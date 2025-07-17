def merge(nums1, m, nums2, n):
    """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    
    ''' 
    Go through each array and compare 2 elements at a time (one from 
    nums1 and one from nums2).  

    ---------------------------------------
    Runtime Complexity: 

    Spacetime Complexity: 

    --------------------------------------- 

    nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3 

    merged = [1, 2, 2, 3, 5, 6]
    '''

    nums1_ptr = m - 1
    nums2_ptr = n - 1 
    index_nums1 = m + n - 1


    





#testcases 
print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
