import os
from typing import Dict, Any

import requests
from dotenv import load_dotenv


load_dotenv()


ALPHA_VANTAGE_BASE_URL = "https://www.alphavantage.co/query"


def get_api_key() -> str:
    """Fetch Alpha Vantage API key from environment."""
    api_key = os.getenv("ALPHA_VANTAGE_KEY")
    if not api_key:
        raise RuntimeError(
            "ALPHA_VANTAGE_KEY is not set. Please update your .env file."
        )
    return api_key


def fetch_time_series_daily(symbol: str, output_size: str = "compact") -> Dict[str, Any]:
    """
    Fetch daily time series data for a given stock symbol from Alpha Vantage.

    Parameters
    ----------
    symbol: str
        Stock ticker symbol (e.g., 'AAPL').
    output_size: str
        'compact' (latest 100 points) or 'full' (full-length series).
    """
    params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": symbol,
        "outputsize": output_size,
        "apikey": get_api_key(),
    }

    response = requests.get(ALPHA_VANTAGE_BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    if "Error Message" in data:
        raise ValueError(f"API error for symbol '{symbol}': {data['Error Message']}")
    if "Time Series (Daily)" not in data:
        raise ValueError("Unexpected API response format: 'Time Series (Daily)' missing.")

    return data
