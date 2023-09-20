from dataclasses import dataclass
from decimal import Decimal


@dataclass(eq=True, frozen=True)
class Token:
    name: str
    symbol: str
    denom: str
    address: str
    decimals: int
    logo: str
    updated: int

    def chain_formatted_value(self, human_readable_value: Decimal) -> Decimal:
        return human_readable_value * Decimal(f"1e{self.decimals}")
