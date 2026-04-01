def get_stock_symbol():
    while True:
        stock_symbol = input("Enter the stock symbol you are looking for: ")
        if stock_symbol != "":
            return stock_symbol.upper()
        else:
            print("Enter a valid stock symbol.")

