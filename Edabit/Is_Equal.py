def is_equal(lst): 
    #Split the numbers 
    firstNum = list(map(int, str(lst[0])))
    secondNum = list(map(int, str(lst[1])))

    return sum(firstNum) == sum(secondNum)

print(is_equal([105, 42]))
print(is_equal([14, 21]))