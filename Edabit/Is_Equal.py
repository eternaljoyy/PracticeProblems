def is_equal(lst): 
    #Assumption: both of the numbers are not null 
    return sum(map(int, str(lst[0]))) == sum(map(int, str(lst[1])))

print(is_equal([105, 42]))
print(is_equal([14, 21]))