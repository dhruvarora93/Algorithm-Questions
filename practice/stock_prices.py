def get_max_profit(stock_prices):

    min_price = stock_prices[0]
    max_profit = float('-inf')
    for stock in stock_prices[1:]:
        max_profit = max(max_profit,stock - min_price)
        min_price = min(min_price,stock)
    print(max_profit)


get_max_profit([10, 7, 5, 8, 6, 9])