from os import getenv

cmc_api_key = getenv("CMC_API_KEY")
cmc_base_api_url = getenv("CMC_BASE_API_URL")
cmc_api_url = f"{cmc_base_api_url}/v1/cryptocurrency/listings/latest?start=1&limit=5000&convert=USD"
