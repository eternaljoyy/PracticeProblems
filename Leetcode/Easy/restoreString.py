def restoreString(s, indices):
    '''
    - make a new string (to hold the new ordered string) 
    - map the indices to each letter in the string, s
    - order the map by the indices (in ascending order)
        -> go through the dictionary, grabbing each corresponding value assosiated
        with the key and add it to the new string 
    - return the new string  

    ============================================================================

    Time complexity: O(N)
    Space Complexity: O()
    ''' 


    orderedStr = ""

    #dictionary to map the indices to the letters in the string s
    strMap = {} 

    #index which will be used to go through the string, s
    index = 0

    #mappings of the index to the corresponding string 
    for item in range(len(indices)):
        strMap[indices[item]] =  s[index]
        index += 1
    #return strMap


    #order the dictionary by the key 
    sortedDict = dict(sorted(strMap.items())) 

    #go through the sorted dict, adding the corresponding value assioiatd with they key to orderedStr 
    for key in sortedDict:
        orderedStr += sortedDict[key]
    return orderedStr


print(restoreString("aiohn", [3,1,4,2,0]))
print(restoreString("aaiougrt", [4,0,2,6,7,3,1,5]))
print(restoreString("art", [1,0,2]))