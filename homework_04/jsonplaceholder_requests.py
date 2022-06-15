import aiohttp
import asyncio  # нужен только для пробного запуска

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

if __name__ == '__main__':
    # asyncio.get_event_loop().run_until_complete(fetch_json(USERS_DATA_URL))
    asyncio.run(fetch_json(USERS_DATA_URL))