def rotateString(s, goal): 
    ''' 
        Keep shifting the string one by one to check if that new string is equal to 
        the target string goal. Stop shifting and return True when s == goal, otherwise 
        keep shifting to the right by 1; when youve shifted such that it returns back to 
        original string then return False.   
    '''   

    shuffleStr = s[-1:] + s[:-1] 

    if shuffleStr == goal:
        return True 
    elif shuffleStr == s: 
        return False 
    else: 
        return rotateString(shuffleStr, goal)


# print(rotateString('abcde', 'cdeab'))
print(rotateString('abcde', 'abced'))