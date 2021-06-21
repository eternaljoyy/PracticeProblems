def checkIfPangram(sentence):      
    ''' 
    - check if the sentence is a panagram 
    - if the length of the sentence >26 letters, we can return false 

    - as we go through the sentence, we can add the letters to a set 
    - we can return the length of the set after we are done going through the array 
    '''  

    if(len(sentence) < 26):
        return False  

    alphabet = set() 

    for char in range(len(sentence)):
        alphabet.add(sentence[char])
    #print(alphabet)
    return len(alphabet) == 26

print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog")) 
print(checkIfPangram("leetcode")) 
print(checkIfPangram(""))