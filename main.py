from datetime import datetime
from visualizer import createGraph

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

"""
get_time_series_option() - Asks the user for the time series they would like.
"""

def get_time_series_option():
    print("\nSelect the Time Series of the chart\n----------------------------------------")
    print("1. Intraday")
    print("2. Daily")
    print("3. Weekly")
    print("4. Monthly")

    while True:
        time_series_choice = input("\nEnter the time series you want (1, 2, 3, 4): ").strip()
        
        if time_series_choice in ['1', '2', '3', '4']:
            return time_series_choice
        else:
            print("Error: Please enter a valid option (1, 2, 3, or 4).")

def main():
    print("Stock Data Visualizer\n--------------------------")

    while True:
        stock_symbol = get_stock_symbol()
        chart_type = get_chart_type()
        time_series = get_time_series_option()
        start_date, end_date = get_date_range()

        createGraph(
            start_date.strftime("%Y-%m-%d"),
            end_date.strftime("%Y-%m-%d"),
            chart_type,
            stock_symbol,
            time_series
        )

        user_choice = input("\nWould you like to view more stock data? Press 'y' to continue: ")
        if user_choice.lower() != 'y':
            print("Thank you and goodbye!")
            break
if __name__ == "__main__":
    main()

      