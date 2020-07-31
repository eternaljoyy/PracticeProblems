def count_vowels(txt):
    count = 0 
    letters = 'aeiou'
    
    for item in txt:
        if item in ['a','e','i','o','u']:
            count+=1
    return count