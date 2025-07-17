def isPalindrome(x):

    ''' 
    Method A): 
        Reverse the integer and check if the reveresed integer
        matches up with x 
        - Drawback: uses extra space..

        ex: x = "121", reversed = "121"; x == reversed 

    Method B): 
        Use a left and right pointer to check whether the 
        numbers are equal. If they are, keep using the pointers to
        go through the number to check the rest of the integer. 
        
    ''' 

    string_valx = str(x) 
    reversed = ''


    for item in range(len(string_valx)-1, -1, -1):
        reversed += string_valx[item]
    return reversed == string_valx


# Test cases 
print(isPalindrome(123))
print(isPalindrome(121))
print(isPalindrome(11))
print(isPalindrome(1))