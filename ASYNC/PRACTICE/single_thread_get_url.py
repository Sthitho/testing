from bs4 import BeautifulSoup as bs
from tqdm.auto import tqdm
import asyncio
import aiohttp

class TqdmUpTo(tqdm):
    def update_to(self, b=1, bsize=1, tsize=1):
        if size is not None:
            self.total = tsize
        self.update(b*size-self.n)

class Scrape:
    def __init__(self, urls):
        self.urls = urls


    async def scrape_urls(self):
        async with aiohttp.ClientSession() as session:
            return await asyncio.gather(
                *(fetch_and_parse(session, url) for url in self.urls)
            )

    async def fetch_and_parse(self, session, url):
        html = await fetch(session, url)
        para = parse(html)
        return para

    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    def parse(self, html):
        soup = bs(html, )

    def print_urls(self):
        print(self.urls)

def main(urls):
    Scrape(urls)

if __name__ == '__main__':
    opener = build_opener()  # handle ERROR403
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    install_opener(opener)
    from sys import argv
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(argv[1:]))
    print('HELLO WORLD')
