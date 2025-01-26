# import os
from .requests.get_daily_adjusted import get_daily_adjusted

ALPHA_VANTAGE_API_KEY = "demo"  # os.getenv("ALPHA_VANTAGE_API_KEY")
ALPHA_VANTAGE_SYMBOL = "IBM"

(
    daily_adjusted,
    daily_adjusted_close_price,
    daily_adjusted_meta_data,
) = get_daily_adjusted(
    ALPHA_VANTAGE_API_KEY,
    ALPHA_VANTAGE_SYMBOL
)

print(daily_adjusted_meta_data)





