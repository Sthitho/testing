import asyncio
from timeit import default_timer
from aiohttp import ClientSession

def fetch_async(urls):
    start_time = default_timer()
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(fetch_all(urls))
    loop.run_until_complete(future)
    tot_elapsed = default_timer() - start_time
    print('Total time taken : '+str(tot_elapsed))

async def fetch_all(urls):
    tasks = []
    fetch.start_time = dict()
    async with ClientSession() as session:
        for url in urls:
            task = asyncio.create_task(fetch(url, session))
            tasks.append(task)
        _ = await asyncio.gather(*tasks)

async def fetch(url, session):
    fetch.start_time[url] = default_timer()
    async with session.get(url) as response:
        r = await response.read()
        elapsed = default_timer() - fetch.start_time[url]
        print(url+' took '+str(elapsed))
        return r

if __name__ == '__main__':
    urls = ['https://nytimes.com',
                'https://github.com',
                'https://google.com',
                'https://reddit.com',
                'https://producthunt.com']
    fetch_async(urls)