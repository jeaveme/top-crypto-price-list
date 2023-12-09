from enum import Enum
from os import getenv

import httpx


class RankingService:
    api_key = getenv("CRYPTOCOMPARE_API_KEY")
    api_url = f"{getenv('CRYPTOCOMPARE_BASE_API_URL')}/data/top/totalvolfull"

    async def getToplistBy24hVolume(self) -> list[str]:
        response = await httpx.get(
            self.api_url,
            params={"limit": 100, "tsym": "usd"},
            headers={"authorization": f"Apikey {self.api_key}"},
        )
        return map(lambda item: item["Name"], response["Data"])
