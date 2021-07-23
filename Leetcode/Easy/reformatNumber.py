def reformatNumber(number):
    '''  

    - we can try to split the string (by the '-' dashes)
    - then we can try to remove the spaces in the string 
    
    - Afterwards, we can loop through the string, checking which condition 
    the string at the current index adheres to and then slicing it and 
    adding it to the new string accordingly 
    '''
     
    newStr = number.replace(' ', "")
    newStr = newStr.split("-")
    n = ''.join(newStr)

    index = 0 
    reformattedStr = ""
    
    while(len(n[index:]) > 0):
        if(len(n[index:]) == 4):
            #group the strings into 2 seperate groups
            reformattedStr += n[index : index +2] + '-' + n[index+2 :index+4]
            index += 4
        elif(len(n[index:]) == 3):
            #group numbers into groups of 3
            reformattedStr +=  n[index : index+3] 
            index += 3
        elif(len(n[index:]) > 4):
            reformattedStr += n[index : index+3] + '-'
            index += 3
        else:
            reformattedStr += n[index : index+2]
            index += 2
    return reformattedStr


print(reformatNumber("1-23-45 6"))
print(reformatNumber("--17-5 229 35-39475 "))
print(reformatNumber("123 4-5678"))