from typing import Literal, Union

Currency = Literal["CHF_HKD", "CHF_JPY", "EUR_CHF", "EUR_GBP", "EUR_HKD", "EUR_JPY", "EUR_SGD", "EUR_USD", "GBP_CHF", "GBP_HKD", "GBP_JPY", "GBP_SGD", "GBP_USD", "HKD_JPY", "SGD_CHF", "SGD_JPY", "USD_CHF", "USD_HKD", "USD_JPY", "USD_SGD"]

Metals = Literal["Gold", "Gold_CHF", "Gold_EUR", "Gold_GBP", "Gold_HKD", "Gold_JPY", "Gold_SGD"]

Instrument = Union[Currency, Metals]