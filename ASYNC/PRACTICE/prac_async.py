import asyncio
from aiohttp import ClientSession
from bs4 import BeautifulSoup as Abs
from sys import argv
import logging
import os


handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


async def web_scraper(urls):
    async with ClientSession() as session:
        list_of_hrefs = await asyncio.gather(
            *(fetch_and_parse(session, url) for url in urls)
        )
        total = 0
        print()
        for dict_ in list_of_hrefs:
            for key in dict_:
                print(f'[{key}] hrefs: {len(dict_[key])}')
                total += len(dict_[key])
        print(f'The total amount of hrefs: {total}\n')


async def fetch_and_parse(session, url):
    logger.debug('Crawling %s', url)
    async with session.get(url) as response:
        html = await response.text()
    para = parse(html)
    return para


def parse(html):
    soup = Abs(html, features='html.parser')
    links = [tag['href'] for tag in soup.find_all('a', {'class': 'fileThumb'})]
    thread = soup.find('div', {'class': 'thread'})['id'][1:] + " " + soup.find('span', {'class': 'subject'}).getText()
    return {thread: links}


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(web_scraper(argv[1:]))
