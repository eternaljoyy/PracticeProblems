def maximumWealth(accounts): 
    ''' 
     - go through the accounts matrix 
     - find the wealth of each customer (each customer has a seperate array in the matrix)
     - return the maximum sum    
    '''   

    maximum = 0

    for customer in range(len(accounts)):
        if(sum(accounts[customer]) > maximum):
            maximum = sum(accounts[customer])
    return maximum 

print(maximumWealth([[1,2,3],[3,2,1]]))
print(maximumWealth([[1,5],[7,3],[3,5]]))
print(maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))