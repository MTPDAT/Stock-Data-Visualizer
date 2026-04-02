from datetime import datetime

"""
get_valid_date() - Gets date in YYYY-MM-DD format.
"""
def get_valid_date(prompt):
    while True:
        date_str = input(prompt)
        try:
           return datetime.strptime(date_str, "%Y-%m-%d") 
        except ValueError: 
            print("Error: Please use YYYY-MM-DD.")

"""
get_date_range() - Uses get_valid_date() and checks that the end date should not be before the begin date
"""
def get_date_range():
    start_date = get_valid_date("Enter the beginning date (YYYY-MM-DD): ")

    while True:
        end_date = get_valid_date("Enter the end date (YYYY-MM-DD): ")

        #Logic: End date should not be before the begin date
        if end_date >= start_date:
            return start_date, end_date
        else:
            print(f"Error: End date cannot be before start date.")

"""
Stock symbol query function that prompts the user for a stock symbol and validates
"""

def get_stock_symbol():
    while True:
        stock_symbol = input("Enter the stock symbol you are looking for: ")
        if stock_symbol != "":
            return stock_symbol.upper()
        else:
            print("Enter a valid stock symbol.")

"""
get_chart_type() - Asks the user for the chart type they would like.
"""
def get_chart_type():
    print("\nChart Types:")
    print("------------")
    print("1. Bar Chart")
    print("2. Line Chart")
    
    while True:
        chart_choice = input("\nEnter the chart type you want (1, 2): ").strip()
        
        if chart_choice == '1':
            return "bar"
        elif chart_choice == '2':
            return "line"
        else:
            print("Error: Please enter 1 for Bar or 2 for Line.")

stock_symbol = get_stock_symbol()
chart_type = get_chart_type()
date = get_date_range()