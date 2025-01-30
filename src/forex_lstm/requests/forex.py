import json
import os
import requests
from typing import cast, TypedDict

from ..types.instrument import Instrument
from ..types.granularity import Candlestick_Granularity

# open, high, low, close
Candlestick_Data = TypedDict("Candlestick_Data", {
    "o": str,
    "h": str,
    "l": str,
    "c": str,
})

Instrument_Candle = TypedDict("Instrument_Candle", {
    "complete": bool,
    "mid": Candlestick_Data,
    "volume": int,
    "time": str
})

Instrument_Candles_Response = TypedDict("Instrument_Candles_Response", {
    "candles": list[Instrument_Candle],
    "granularity": Candlestick_Granularity,
    "instrument": Instrument,
})

BASE_URL = "https://api-fxpractice.oanda.com"
OANDA_API_KEY = cast(str, os.getenv("OANDA_API_KEY"))

s = requests.Session()
s.headers = {
    "Authorization": f"Bearer {OANDA_API_KEY}",
}

def get_instrument_candles(
    instrument: Instrument,
    from_timestamp: float, 
    to_timestamp: float, 
) -> Instrument_Candles_Response:
    """
    See:
        developer.oanda.com/rest-live-v20/instrument-ep
        oanda.com/uk-en/trading/instruments
    """
    try:        
        r = s.get(f"{BASE_URL}/v3/instruments/{instrument}/candles?price=M&granularity=D&from={from_timestamp}&to={to_timestamp}")
        r.raise_for_status()
        return r.json()
    except requests.exceptions.HTTPError as e_http:
        print(json.dumps(r.json(), indent=4))
        raise SystemExit(e_http)
    except requests.JSONDecodeError as e_decode:
        print("JSON body decode error")
        raise SystemExit(e_decode)
    except requests.exceptions.RequestException as e_exeption:
        raise SystemExit(e_exeption)