import argparse

from api_handler import fetch_time_series_daily
from visualizer import time_series_to_dataframe, create_price_figure


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch and visualize stock price data using Alpha Vantage."
    )
    parser.add_argument(
        "symbol",
        type=str,
        help="Stock ticker symbol (e.g., AAPL, MSFT).",
    )
    parser.add_argument(
        "--outputsize",
        type=str,
        choices=["compact", "full"],
        default="compact",
        help="Amount of historical data to fetch from Alpha Vantage.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    print(f"Fetching data for {args.symbol} from Alpha Vantage...")
    raw_data = fetch_time_series_daily(args.symbol, output_size=args.outputsize)

    print("Transforming data into DataFrame...")
    df = time_series_to_dataframe(raw_data)

    print("Creating interactive Plotly figure...")
    fig = create_price_figure(df, args.symbol)

    # Display in a browser window
    fig.show()


if __name__ == "__main__":
    main()

