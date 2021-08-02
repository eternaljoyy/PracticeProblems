def areOccurrencesEqual(s):
    '''
    - create a dictionary which stores the letter and the occurence of the letter 
    - have a boolean variable (which keeps track of whether the frequency of each word is the same)
    - go through the string s  
      -> add the current letter (and its frequency) to the dictionary  
    - go through the dictionary, checking if all the words match the 
    frequency of the current word 
    - go through the dictionary, checking if all the values in the dictionary are the same 
    ''' 

    frequencyLetter = {}  

    for char in range(len(s)): 
        frequencyLetter[s[char]] = s.count(s[char])

    
    occurence = set()

    for key in frequencyLetter:
      occurence.add(frequencyLetter[key])

    if(len(occurence) > 1):
      return False 
    else:
      return True

    

print(areOccurrencesEqual("abacbc"))
print(areOccurrencesEqual("aaabb"))