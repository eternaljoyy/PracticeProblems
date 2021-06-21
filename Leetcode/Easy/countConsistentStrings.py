def countConsistentStrings(allowed, words): 
    '''  
    - make a variable count to keep track of the number of consistent strings 
    - go through the words array, checking each word in the array is consistent 
       - check if each word appears in the allowed string
       - If so, increment the variable count
    '''   
    #keeps track of whether or not a word is consistent 
    consistent = False  

    #keeps track of the number of consistent words in the words array 
    count = 0 
    
    for word in range(len(words)):
        for char in range(len(words[word])):
            if(words[word][char] in allowed):
                consistent = True
            else: 
                consistent = False 
                break 
        
        if(consistent == True):
            count += 1
    return count 
    

print(countConsistentStrings("ab",["ad","bd","aaab","baa","badab"]))        
print(countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]))
print(countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]))