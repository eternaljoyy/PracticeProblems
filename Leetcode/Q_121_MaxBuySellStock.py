def maxProfit(prices):
    """
    Go through array, and find a day in which to buy a
    stock, and then find a day in which to sell the stock. 

    Max Profit = Sell Price - Buy Price  

    ---------------------------------------------------------
    N = # of items in the prices array 

    Runtime Complexity: O(N)
     - Going through the prices array in one pass, going through 
     each element 1 by 1 

    Spacetime Complexity: O(1) 
     - no additional use of any extra data structures 
    """  

    max_profit = 0 
    buy_price = prices[0]


    for index in range(len(prices)):
        buy_price = min(buy_price, prices[index])
        max_profit = max(max_profit, prices[index] - buy_price)
    return max_profit



print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
print(maxProfit([1]))
