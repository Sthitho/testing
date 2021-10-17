import asyncio
from time import sleep
from concurrent.futures import ProcessPoolExecutor
from sys import argv

def blocking_func(x):
   sleep(3) # Pretend this is expensive calculations
   return x + x

async def main(word):
    #pool = multiprocessing.Pool()
    #out = pool.apply(blocking_func, args=(10,)) # This blocks the event loop.
    executor = ProcessPoolExecutor()
    out = await loop.run_in_executor(executor, blocking_func, word)  # This does not
    print(out)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(argv[1]))