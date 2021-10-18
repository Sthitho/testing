import asyncio
from aiohttp import ClientSession
from bs4 import BeautifulSoup as Abs
from sys import argv


async def web_scraper(urls):
    async with ClientSession() as session:
        list_of_hrefs = await asyncio.gather(
            *(fetch_and_parse(session, url) for url in urls)
        )
        total = 0
        print()
        for dict_ in list_of_hrefs:
            for key in dict_:
                print(f'[{key}] thread hrefs: {len(dict_[key])}')
                total += len(dict_[key])
        print('\nThe total amount of hrefs: '+str(total))


async def fetch_and_parse(session, url):
    html = await fetch(session, url)
    para = parse(html)
    return para


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


def parse(html):
    soup = Abs(html, features='html.parser')
    links = [tag['href'] for tag in soup.find_all('a', {'class': 'fileThumb'})]
    thread = soup.find('input', {'name': 'resto'})['value'] + " " + soup.find('span', {'class': 'subject'}).getText()
    return {thread: links}


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(web_scraper(argv[1:]))
