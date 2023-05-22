from typing import Dict


class TokenSource:

    def __init__(
        self,
        denom: str,
        symbol: str,
        address: str,
        decimals: int,
        updated: int,
    ):
        self.denom = denom
        self.symbol = symbol
        self.address = address
        self.decimals = decimals
        self.updated = updated


class Token:

    def __init__(
        self,
        name: str,
        symbol: str,
        decimals: int,
        logo: str,
    ):
        self.name = name
        self.symbol = symbol
        self.decimals = decimals
        self.logo = logo

        self._sources = Dict[str, TokenSource]

    def add_source(self, denom: str, symbol: str, address: str, decimals: int, updated: int):
        if denom not in self._sources:
            token_source = TokenSource(
                denom=denom,
                symbol=symbol,
                address=address,
                decimals=decimals,
                updated=updated,
            )
            self._sources[denom] = token_source