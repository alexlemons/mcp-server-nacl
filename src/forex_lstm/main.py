import json
import math
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler, Normalizer
from typing import cast

from .requests.forex import Instrument_Candles_Response

# Open saved response
with open('src/forex_lstm/response_data/GBP_JPY_2005_2025.json', 'r') as file:
    res = cast(Instrument_Candles_Response, json.load(file))

# Convert ISO date to np.datetime64
# Convert str close price to float 
l_dates, l_close_price = [], []
for _idx, day in enumerate(res["candles"]):
    l_dates.append(np.datetime64(day["time"]))
    l_close_price.append(float(day["mid"]["c"]))

dates = np.array(l_dates)
close_price = np.array(l_close_price)

# 90:10 split of data training:validation 
# Data split before any processing to avoid lookahead bias
split_index = math.ceil(len(l_dates) * 0.9)

dates_training, dates_validation = np.split(dates, [split_index])
close_price_training, close_price_validation = np.split(close_price, [split_index])

plt.plot(dates_training, close_price_training)
plt.plot(dates_validation, close_price_validation)
plt.show()

# # TODO normalization
# scaler = MinMaxScaler(feature_range=(-1, 1))