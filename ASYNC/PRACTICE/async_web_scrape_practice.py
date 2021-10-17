import asyncio
from atiohttp import ClientSession
from bs4 import BeautifulSoup as bs
from sys import argv

async def main(word):


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(argv[1]))