def isSumEqual(firstWord, secondWord, targetWord): 
    '''  


    ==================================================
    Complexity Analysis: 
        Time complexity: O(?) 
        Space Complexity: O(?)  
    '''

    def Helper(word):
        res = ""
    
        for char in word:
            ordVal = ord(char) - ord('a')
            res += str(ordVal)
        return res 

    return int(Helper(firstWord)) + int(Helper(secondWord)) == int(Helper(targetWord))




print(isSumEqual("acb","cba", "cdb"))       
print(isSumEqual("aaa", "a", "aab"))
print(isSumEqual( "aaa", "a", "aaaa"))