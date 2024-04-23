"""
Task
You start with $100. Each turn you will be given the stock prices of current day and previous 4 days.
You must then choose to BUY or SELL the stocks.
Your program will be run with input for 1 day at a time.

Input
The input of each turn will consist of multiple lines.
All money values are doubles to two decimal places, all other numbers are integers.
The first line contains three space separated numbers m k d.
m - the amount of money you could spend that day.
k - the number of different stocks available for buying or selling.
d - the number of remaining days for trading stocks.
k lines follow, each in the following format:
name owned prices
name - the name of the stock (a string).
owned - the number of shares you own of that stock.
prices - 5 space separated numbers representing the stock's price for the last 5 days.
These are ordered from oldest to newest, so the last number is the current stock price.
Your program will be fed the days sequentially so
you can write to a file in order to store a longer history of the prices.

Output
The output for each turn should also contain multiple lines:
Output N for the number of transactions you wish to make. Output 0 if you are not making any transactions that day.
If you are making transactions, output N lines containing the name of the stock (case sensitive),
BUY or SELL, and the number of shares you wish to buy or sell.
NOTE: Money earned from selling stocks will only become available (for buying stocks) on the following day.
"""

money, num_stocks, remaining_days = [float(i) for i in input().strip().split()]

transactions = []
for i in range(int(num_stocks)):
    parts = input().strip().split()
    name, owned = parts[0], int(parts[1])
    prices = [float(price) for price in parts[2:]]

    current_price = prices[-1]
    avg_price = sum(prices[:-1]) / len(prices[:-1])

    if (current_price > avg_price) and (owned > 0):
        transactions.append(f'{name} SELL {owned}')
    elif (current_price <= avg_price) and (money >= current_price):
        shares_to_buy = int(money / current_price)
        money = - current_price * shares_to_buy
        transactions.append(f'{name} BUY {shares_to_buy}')

print(len(transactions))
for transaction in transactions:
    print(transaction)
