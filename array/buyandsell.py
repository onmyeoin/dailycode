prices = [7,1,5,3,9,4]
 

def maxProfit(prices):
    min_price = 99999
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        daily_profit = prices[i] - min_price
        if daily_profit > max_profit:
            max_profit = daily_profit
        
    return max_profit
    
maxProfit(prices)
