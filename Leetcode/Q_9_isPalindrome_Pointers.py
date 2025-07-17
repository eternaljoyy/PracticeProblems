def isPalindrome(x):

    '''
    Note: int isnt iterable, so we'd have to make this into a string. 

    Method B): 

        Create a boolean to keep track of whether the number (so far),
        is a palindrome.  

        Use a left and right pointer to check whether the 
        numbers are equal. If they are, keep using the pointers to
        go through the number to check the rest of the integer. 

    ------------------------------------------------------------------
    N = # of items in str_xval 

    Runtime Complexity: 
        - Going through the entire string, one by one (given that its a
        palindrome). This is O(N). 

    Spacetime Complexity:  
        - O(N) 

     --------------------
     ** watch out for integer overflow
    ''' 

    is_palindrome = False 

    str_xval = str(x) # "1 2 1"
    left = 0
    right = len(str_xval)-1


    while left <= right: # left = 2, right = 0

        if str_xval[left] == str_xval[right]:  # 2 == 2
            is_palindrome = True # is_pal.. = True 
            left += 1  # left = 2
            right -= 1  # right = 0
        else:
            return False 
    return is_palindrome


# Test cases 
print(isPalindrome(123))
print(isPalindrome(121))
print(isPalindrome(11))
print(isPalindrome(1))