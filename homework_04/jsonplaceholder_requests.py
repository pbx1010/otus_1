"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import aiohttp
import asyncio


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users/1"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts/1"


async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(USERS_DATA_URL) as resp:
            print(resp.status)
            print(await resp.text())
            return await resp.json()

if __name__ == '__main__':
    asyncio.run(fetch_json(USERS_DATA_URL))



# async def users():
#     async with aiohttp.ClientSession() as session:
#         async with session.get(USERS_DATA_URL) as resp:
#             print(resp.status)
#             #print(await resp.text())
#             #print(await resp.json())
#             response_json = (await resp.json())
#             print(response_json['address'], response_json['website'])
#             #print(response_json)
#             #print(type(response_json))
#
# async def posts():
#     async with aiohttp.ClientSession() as session:
#         async with session.get(POSTS_DATA_URL) as resp:
#             print(resp.status)
#             print(await resp.text())
#             print(await resp.json())
#
# asyncio.run(users())
# asyncio.run(posts())
