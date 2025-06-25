import pytest

from pyinjective.core.tokens_file_loader import TokensFileLoader


class TestTokensFileLoader:
    def test_load_tokens(self):
        tokens_list = [
            {
                "address": "",
                "isNative": True,
                "decimals": 9,
                "symbol": "SOL",
                "name": "Solana",
                "logo": "https://imagedelivery.net/DYKOWp0iCc0sIkF-2e4dNw/2aa4deed-fa31-4d1a-ba0a-d698b84f3800/public",
                "coinGeckoId": "solana",
                "denom": "",
                "tokenType": "spl",
                "tokenVerification": "verified",
                "externalLogo": "solana.png",
            },
            {
                "address": "0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270",
                "isNative": False,
                "decimals": 18,
                "symbol": "WMATIC",
                "logo": "https://imagedelivery.net/DYKOWp0iCc0sIkF-2e4dNw/0d061e1e-a746-4b19-1399-8187b8bb1700/public",
                "name": "Wrapped Matic",
                "coinGeckoId": "wmatic",
                "denom": "0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270",
                "tokenType": "evm",
                "tokenVerification": "verified",
                "externalLogo": "polygon.png",
            },
        ]

        loader = TokensFileLoader()

        loaded_tokens = loader.load_json(json=tokens_list)

        assert len(loaded_tokens) == 2

        for token, token_info in zip(loaded_tokens, tokens_list):
            assert token.name == token_info["name"]
            assert token.symbol == token_info["symbol"]
            assert token.denom == token_info["denom"]
            assert token.address == token_info["address"]
            assert token.decimals == token_info["decimals"]
            assert token.logo == token_info["logo"]
            assert token.unique_symbol == ""

    @pytest.mark.asyncio
    async def test_load_tokens_from_url(self, aioresponses):
        loader = TokensFileLoader()
        tokens_list = [
            {
                "address": "",
                "isNative": True,
                "decimals": 9,
                "symbol": "SOL",
                "name": "Solana",
                "logo": "https://imagedelivery.net/DYKOWp0iCc0sIkF-2e4dNw/2aa4deed-fa31-4d1a-ba0a-d698b84f3800/public",
                "coinGeckoId": "solana",
                "denom": "",
                "tokenType": "spl",
                "tokenVerification": "verified",
                "externalLogo": "solana.png",
            },
            {
                "address": "0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270",
                "isNative": False,
                "decimals": 18,
                "symbol": "WMATIC",
                "logo": "https://imagedelivery.net/DYKOWp0iCc0sIkF-2e4dNw/0d061e1e-a746-4b19-1399-8187b8bb1700/public",
                "name": "Wrapped Matic",
                "coinGeckoId": "wmatic",
                "denom": "0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270",
                "tokenType": "evm",
                "tokenVerification": "verified",
                "externalLogo": "polygon.png",
            },
        ]

        aioresponses.get(
            "https://github.com/InjectiveLabs/injective-lists/raw/master/tokens/mainnet.json", payload=tokens_list
        )
        loaded_tokens = await loader.load_tokens(
            tokens_file_url="https://github.com/InjectiveLabs/injective-lists/raw/master/tokens/mainnet.json"
        )

        assert len(loaded_tokens) == 2

        for token, token_info in zip(loaded_tokens, tokens_list):
            assert token.name == token_info["name"]
            assert token.symbol == token_info["symbol"]
            assert token.denom == token_info["denom"]
            assert token.address == token_info["address"]
            assert token.decimals == token_info["decimals"]
            assert token.logo == token_info["logo"]
            assert token.unique_symbol == ""

    @pytest.mark.asyncio
    async def test_load_tokens_from_url_returns_nothing_when_request_fails(self, aioresponses):
        loader = TokensFileLoader()

        aioresponses.get(
            "https://github.com/InjectiveLabs/injective-lists/raw/master/tokens/mainnet.json",
            status=404,
        )
        loaded_tokens = await loader.load_tokens(
            tokens_file_url="https://github.com/InjectiveLabs/injective-lists/raw/master/tokens/mainnet.json"
        )

        assert len(loaded_tokens) == 0
