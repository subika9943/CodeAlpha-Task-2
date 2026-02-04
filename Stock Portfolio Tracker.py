stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total_investment = 0

print(" Stock Portfolio Tracker")
print("Available stocks:", list(stock_prices.keys()))

n = int(input("Enter number of stocks you want to buy: "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        cost = stock_prices[stock] * quantity
        total_investment += cost
        print("Cost for", stock, "=", cost)
    else:
        print("Stock not available")

print("\nTotal Investment Value =", total_investment)

save = input("Do you want to save the result? (yes/no): ").lower()
if save == "yes":
    file = open("portfolio.txt", "w")
    file.write("Total Investment Value = " + str(total_investment))
    file.close()
    print("Saved to portfolio.txt")
