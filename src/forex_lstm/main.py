from datetime import datetime
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt

from .requests.forex import get_instrument_candles

from_timestamp = datetime(2024, 1, 1).timestamp()
to_timestamp = datetime(2024, 12, 31).timestamp()

res = get_instrument_candles(
    instrument="GBP_JPY",
    from_timestamp=from_timestamp,
    to_timestamp=to_timestamp,
)

# import json
# with open('data.json', 'w') as f:
#     json.dump(res, f)

# Convert ISO date to np.datetime64
# Convert str close price to float 
l_dates, l_close_price = [], []
for _idx, day in enumerate(res["candles"]):
    l_dates.append(np.datetime64(day["time"]))
    l_close_price.append(float(day["mid"]["c"]))

dates = np.array(l_dates)
close_price = np.array(l_close_price)
plt.plot(dates, close_price)
plt.show()
