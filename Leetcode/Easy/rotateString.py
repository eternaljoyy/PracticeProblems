def rotateString(s, goal): 
    ''' 
        Keep shifting the string one by one to check if that new string is equal to 
        the target string goal. Stop shifting and return True when s == goal, otherwise 
        keep shifting to the right by 1; when youve shifted such that it returns back to 
        original string then return False.    

    ======================================================================================= 

    Runtime Complexity: O(N) (loop) * O(?) (w/ slicing)

    Spacetime Complexity: O(?) -> No additional data structure was made  
    

    -> TODO: Figure out time and space complexity of slicing a list 
    '''   
    
    numChars = len(s)

    while numChars != 0: 

        s = s[-1:] + s[:-1] 
        
        if s == goal:
            return True 

        numChars -= 1
    return False 


#Testcases 
print(rotateString('abcde', 'cdeab'))
print(rotateString('abcde', 'abced'))
