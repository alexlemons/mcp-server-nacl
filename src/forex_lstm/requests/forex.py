from datetime import datetime
import json
import os
import requests
from typing import cast

from ..types.instrument import Instrument

BASE_URL = "https://api-fxpractice.oanda.com"

s = requests.Session()
s.headers = {
    "Authorization": f"Bearer {cast(str, os.getenv("OANDA_API_KEY"))}",
}

def get_instrument_candles(
    instrument: Instrument,
    from_timestamp: float, 
    to_timestamp: float, 
):
    """
    See:
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