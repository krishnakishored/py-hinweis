import requests
import asyncio
from aiohttp import ClientSession
import pathlib

def hello_synchronous():
    """multiple synchronous requests"""
    here = pathlib.Path(__file__).parent
    urls = []
    with open(here.joinpath("urls.txt")) as infile:
        urls = set(map(str.strip, infile))
    for url in urls:
        print(requests.get(url).text)
    # return requests.get("http://httpbin.org/get")

async def hello_async(url):
    """First it fetches response asynchronously, then it reads response body in asynchronous manner.:"""
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            print(response)

def run_single_async():
    """To start your program you need to run it in event loop,
     so you need to create instance of asyncio loop and put task into this loop."""
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello_async("http://httpbin.org/headers"))

def run_multiple_async_wait():
    loop = asyncio.get_event_loop()
    tasks = []
    # I'm using test server localhost, but you can use any url
    # url = "http://localhost:8080/{}"
    url = "http://httpbin.org/get"
    for i in range(5):
        task = asyncio.ensure_future(hello_async(url.format(i)))
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))            

"""asyncio.gather() collects bunch of Future objects in one place and waits for all of them to finish."""
async def fetch(url, session):
    async with session.get(url) as response:
        """NOT: return response.read():  async operation must be preceded by await """
        return await response.read() 

async def run_with_async_gather(r):
    """Fetch all responses within one Client session"""
    url = "http://httpbin.org/get"
    tasks = []
    # keep connection alive for all requests.
    async with ClientSession() as session:
        for i in range(r):
            task = asyncio.ensure_future(fetch(url.format(i), session))
            tasks.append(task)
        # responses =  asyncio.gather(*tasks)  # missing await  -- <_GatheringFuture pending>
        responses = await asyncio.gather(*tasks)
        # you now have all response bodies in this variable
        print(responses)

def run_multiple_async_gather():
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run_with_async_gather(4))
    loop.run_until_complete(future)



if __name__ == "__main__":
    # hello_synchronous()
    # run_single_async()
    # run_multiple_async_wait()
    run_multiple_async_gather()
