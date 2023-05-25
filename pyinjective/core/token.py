from decimal import Decimal


class Token:

    def __init__(
        self,
        name: str,
        symbol: str,
        denom: str,
        address: str,
        decimals: int,
        logo: str,
        updated: int,
    ):
        self.name = name
        self.symbol = symbol
        self.denom = denom
        self.address = address
        self.decimals = decimals
        self.logo = logo
        self.updated = updated

    def chain_formatted_value(self, human_readable_value: Decimal) -> Decimal:
        return human_readable_value * Decimal(f"1e{self.decimals}")
