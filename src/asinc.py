import aiohttp
import asyncio
import time


async def main():
    base_url = 'https://api.nasa.gov/'
    api_key = '5nUO0WVdkgzd5OTUVf4omtmopY705py3xXDWPBDz'

    urls = [
        f'{base_url}neo/rest/v1/feed?api_key={api_key}',
        f'{base_url}planetary/apod?api_key={api_key}',
        f'{base_url}EPIC/api/natural/images?api_key={api_key}',
    ]

    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        for url in urls:
            print(await session.get(url))

    end_time = time.time()

    print(end_time - start_time)


if __name__ == '__main__':
    asyncio.run(main())
