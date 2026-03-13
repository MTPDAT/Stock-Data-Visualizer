from typing import Dict, Any

import pandas as pd
import plotly.graph_objs as go


def time_series_to_dataframe(raw_data: Dict[str, Any]) -> pd.DataFrame:
    """
    Convert Alpha Vantage daily time series JSON into a tidy DataFrame.

    The API response is expected to have a 'Time Series (Daily)' key with
    nested date dictionaries.
    """
    time_series = raw_data.get("Time Series (Daily)", {})
    if not time_series:
        raise ValueError("No 'Time Series (Daily)' data found in API response.")

    records = []
    for date_str, values in time_series.items():
        records.append(
            {
                "date": pd.to_datetime(date_str),
                "open": float(values["1. open"]),
                "high": float(values["2. high"]),
                "low": float(values["3. low"]),
                "close": float(values["4. close"]),
                "adjusted_close": float(values["5. adjusted close"]),
                "volume": int(values["6. volume"]),
            }
        )

    df = pd.DataFrame(records).sort_values("date")
    df.reset_index(drop=True, inplace=True)
    return df


def create_price_figure(df: pd.DataFrame, symbol: str) -> go.Figure:
    """
    Create an interactive line chart for closing prices using Plotly.
    """
    if df.empty:
        raise ValueError("DataFrame is empty; cannot create visualization.")

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["close"],
            mode="lines",
            name=f"{symbol.upper()} Close",
        )
    )

    fig.update_layout(
        title=f"Daily Closing Prices for {symbol.upper()}",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        template="plotly_dark",
        hovermode="x unified",
    )

    return fig
