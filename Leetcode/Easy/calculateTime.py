def calculateTime(keyboard, word):
    '''There is a special keyboard with all keys in a single row.
    You have given a string keyboard of length 26 indicating the layout of the keyboard 
    (indexed from 0 to 25), initially your finger is at index 0. To type a character, you have to
    move your finger to the index of the desired character. The time taken to move your finger from index i 
    to index j is |i – j|.You want to type a string word. Write a program to calculate how much time it takes 
    to type it with one finger
    =============================================================================

    Example 1: 
    Input :- Keyboard = "abcdefghijklmnopqrstuvwxyz", Word = "cba"
    Output :- 4

    Example 2: 
    Input :- Keyboard = "pqrstuvwxyzabcdefghijklmno", Word = "hello"
    Output :- 31 

    ============================================================================= 
    High level solution/Approach: 
    - map the letter to its index equivalent (in the keyboard)  
    - go through the word string 
     -> find the index of the word in dictionary 
     -> get the difference (on the indices) of the current word and the word after it  
     -> add the difference to the variable count
    - return count 
    '''  

    #make a dictionary mapping the letter to the index equivalent from the keyboard 
    charDict = {}

    for item in range(len(keyboard)): 
        charDict[keyboard[item]] = item
    #print(charDict) 

    
    count = 0

    for char in range(len(word)-1): 
        if(char == 0):
            count += charDict[word[char]]
        count+= abs(charDict[word[char]] - charDict[word[char+1]])
    return count 


print(calculateTime("abcdefghijklmnopqrstuvwxyz", "cba"))
print(calculateTime("pqrstuvwxyzabcdefghijklmno", "hello"))