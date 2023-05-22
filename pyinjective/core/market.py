from dataclasses import dataclass
from decimal import Decimal

from pyinjective.core.token import Token


@dataclass
class Market:
    id: str
    status: str
    ticker: str
    base_token: Token
    quote_token: Token
    maker_fee_rate: Decimal
    taker_fee_rate: Decimal
    service_provider_fee: Decimal
    min_price_tick_size: Decimal
    min_quantity_tick_size: Decimal