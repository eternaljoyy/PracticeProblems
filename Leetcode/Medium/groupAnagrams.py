from collections import defaultdict 

def groupAnagrams(strs): 
    """  

    **TODO 
    -Given an array of strings, group the anagrams together
    (return answer in any order). 

    - keep track of the anagrams using a dictionary 
        -> sort the word in the strs array
       -> have the key as the sorted words and the anagrams of that key can be the values
       -> ex: 

       aet: {'eat', 'tea', 'ate'} 
    
    - then, we can go through the dictionary, adding the values to the list 

    -> NOTE: string obj has no atrribute (remeber to add the values correpsonding to the keys as a list
    , NOT just a string -- we add that string into a list) 

    -> Runtime: O(N)? 
    """  
    
    anagramDict = defaultdict(list) 

    for word in strs:  
        #sorted() returns a sorted list of the itersble object 
        sortedWord = ''.join(sorted(word))

        if(sortedWord not in anagramDict):
            anagramDict[sortedWord] = [word]
        else:
            anagramDict[sortedWord].append(word)
    return anagramDict.values()


#testing 
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"])) 
print(groupAnagrams([""]))
print(groupAnagrams( ["a"]))