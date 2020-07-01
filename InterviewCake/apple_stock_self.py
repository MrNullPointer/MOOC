def get_max_profit(stock_prices):
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for idx in range(1,len(stock_prices)):
        curr_price = stock_prices[idx]
        potential_profit = curr_price - min_price

        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, curr_price)
    
    return max_profit


print(get_max_profit([9, 7, 4, 1]))