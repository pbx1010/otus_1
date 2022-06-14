"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import aiohttp
import asyncio


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users/"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts/"


async def users():
    async with aiohttp.ClientSession() as session:
        async with session.get(USERS_DATA_URL) as resp:
            print(resp.status)
            print(await resp.text())

async def posts():
    async with aiohttp.ClientSession() as session:
        async with session.get(POSTS_DATA_URL) as resp:
            print(resp.status)
            print(await resp.text())

asyncio.run(users())
asyncio.run(posts())
