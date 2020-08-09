def sort_by_length(lst):
    '''
    Create a function that takes a list of strings and return a list, 
    sorted from shortest to longest.

    use a dictionary
    (key, value) -> (word, length of word)
    '''
    dict = {} 
    for item in range(0, len(lst)):
        dict[lst[item]] = len(lst[item])
    sorted_dict(dict)

#sort the dictionary 
def sorted_dict(dict):
    sort_items = sorted(dict.items(), lambda x:)
    
    
    
    
sort_by_length(["Jung", "Turing", "Einstein"])