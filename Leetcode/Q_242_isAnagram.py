def isAnagram(s, t):
    """
    Method A: 

      - Notice that s == t if/when 
      you sort both these strings (either in ascending order 
      or in descending order), they can be equal to one another. 

      Ex: s = 'ate', t = 'eat'; s = 'aet', t = 'aet' s == t 

      - sorting the strings
      - then check to see if they're equal to each other 


    Method B: 
      - create a hashmap to store the number of occurences of each 
      letter in string, and then compare the 2 hashmaps, checking if 
      theyre equal to one another  

    -----------------------------------------------------------------
    Runtime Complexity: 

    N = # of items in string s, M = # of items in string t 
    
    Runtime Complexity:
    - O(N+M)

    Spacetime Complexity: 
    - O(N+M)
    """ 

    map_strS = {} 
    map_strT = {}


    for item in range(len(s)):
        if s[item] not in map_strS:
            map_strS[s[item]] = 1
        else:
            map_strS[s[item]] += 1


    for item in range(len(t)):
        if t[item] not in map_strT:
            map_strT[t[item]] = 1
        else:
            map_strT[t[item]] += 1 


    return map_strT == map_strS



print(isAnagram("anagram", "nagaram")) 
print(isAnagram("", " "))  
print(isAnagram("eat", "ate"))
print(isAnagram("rat", "car"))
