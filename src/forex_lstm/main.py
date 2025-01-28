import json
from datetime import datetime
import numpy as np

from .requests.forex import get_instrument_candles

from_timestamp = datetime(2024, 1, 1).timestamp()
to_timestamp = datetime.now().timestamp()

candles = get_instrument_candles(
    instrument="USD_JPY",
    from_timestamp=from_timestamp,
    to_timestamp=to_timestamp,
)

print(json.dumps(candles, indent=4))
