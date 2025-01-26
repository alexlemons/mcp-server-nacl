from collections import OrderedDict
from typing import cast, Dict, TypedDict
from alpha_vantage.timeseries import TimeSeries

Daily_Adjusted = TypedDict("Daily_Adjusted", {
    "1. open": str,
    "2. high": str,
    "3. low": str,
    "4. close": str,
    "5. adjusted close": str,
    "6. volume": str,
    "7. dividend amount": str,
    "8. split coefficient": str,
})

# keys: YYYY-MM-DD str
Time_Series_Daily_Adjusted = Dict[str, Daily_Adjusted]

Time_Series_Daily_Adjusted_Meta_Data = TypedDict("Time_Series_Daily_Adjusted_Meta_Data", {
    "1. Information": str,
    "2. Symbol": str,
    "3. Last Refreshed": str,
    "4. Output Size": str,
    "5. Time Zone": str,
})

def get_daily_adjusted(apiKey: str, symbol: str):
    """
    See: 
        alphavantage.co/documentation/#dailyadj
        investopedia.com/terms/s/splitadjusted.asp

    Split adjusted prices represent historical price data by
    anchoring to the current price and working backwards.
    This gives a more accurate representation of the amount 
    of growth the the shares have experienced.
    It is generally considered best practice to use split/dividend
    adjusted prices when modelling stock price movements.
    """

    ts = TimeSeries(key=apiKey)
    
    data, daily_adjusted_meta_data = cast(
        tuple[Time_Series_Daily_Adjusted, Time_Series_Daily_Adjusted_Meta_Data],
        ts.get_daily_adjusted(symbol, outputsize="full")
    )
    
    if not data:
        raise ValueError("No data") 
    if not daily_adjusted_meta_data:
        raise ValueError("No meta data")
    
    # Reverse data into chronological order
    daily_adjusted = OrderedDict(reversed(list(data.items())))

    daily_adjusted_close_price = list(map(
        lambda day: float(day["5. adjusted close"]),
        daily_adjusted.values()
    ))

    return daily_adjusted, daily_adjusted_close_price, daily_adjusted_meta_data