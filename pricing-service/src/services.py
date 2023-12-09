from enum import Enum
from os import getenv

import httpx


class PricingService:
    api_key = getenv("CMC_API_KEY")
    api_url = f"{getenv('CMC_BASE_API_URL')}/v2/tools/price-conversion"

    async def getLatestUsdPrice(self, symbols: list[str]) -> float:
        return await httpx.get(
            self.api_url,
            params={"amount": 1, "symbol": ",".join(symbols), "convert": "usd"},
            headers={"X-CMC_PRO_API_KEY": self.api_key},
        )
