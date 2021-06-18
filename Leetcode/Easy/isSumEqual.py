def mapToInt(word, wordMap): 
    '''  
    - Map the input word to the integer equivalent 
    ''' 
    
    num = ""

    for char in range(len(word)): 
        num += str(wordMap[word[char]])
    return int(num)


def isSumEqual(firstWord, secondWord, targetWord): 
    '''  
    Leetcode 1880

    The letter value of a letter is its position in the alphabet starting from 0 
    (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).

    The numerical value of some string of lowercase English letters s is the concatenation of the letter values of 
    each letter in s, which is then converted into an integer.

    For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After converting it, 
    we get 21. You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase 
    English letters 'a' through 'j' inclusive.

    Return true if the summation of the numerical values of firstWord and secondWord equals the numerical value of 
    targetWord, or false otherwise. 

    Example 1:

    Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
    Output: true
    Explanation:
    The numerical value of firstWord is "acb" -> "021" -> 21.
    The numerical value of secondWord is "cba" -> "210" -> 210.
    The numerical value of targetWord is "cdb" -> "231" -> 231.
    We return true because 21 + 210 == 231.  

    ======================================================================

    -create a map in order to map the letters to their numerical counterparts 
    -Convert first and second words into integers and add them 
    '''   

    wordMap = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9} 

    numFirstWord = mapToInt(firstWord, wordMap) 

    numSecondWord = mapToInt(secondWord, wordMap) 

    numTargetWord = mapToInt(targetWord, wordMap) 

    return numFirstWord + numSecondWord == numTargetWord

    
             
print(isSumEqual("acb", "cba", "cdb"))   
print(isSumEqual("aaa", "a", "aab"))  
print(isSumEqual("aaa", "a", "aaaa"))