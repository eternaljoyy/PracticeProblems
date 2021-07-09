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