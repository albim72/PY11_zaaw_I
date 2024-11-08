import asyncio
import aiohttp

async def fetch_price(session, url):
    async with session.get(url) as response:
        data = await response.json()
        return data

async def monitor_prices():
    urls = [
        'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd',
        'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'
    ]
    async with aiohttp.ClientSession() as session:
        while True:
            tasks = [fetch_price(session, url) for url in urls]
            results = await asyncio.gather(*tasks)
            print(f"Bitcoin price: ${results[0]['bitcoin']['usd']}")
            print(f"Ethereum price: ${results[1]['ethereum']['usd']}")
            await asyncio.sleep(10)  # Wait 10 seconds before fetching again

# Instead of asyncio.run, use await in a Jupyter cell
await monitor_prices()
