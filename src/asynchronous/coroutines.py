import asyncio


async def mycoro(number):
    print("Starting %d" % number)
    await asyncio.sleep(1)
    print("Finishing %d" % number)
    return str(number)


def run_my_coroutine_gather():
    # single future
    # myfuture1 = asyncio.ensure_future(mycoro(1)) # Runs mycoro!
    # print(myfuture1) # <Task pending name='Task-1' coro=<mycoro() running at coroutines.py:3>>
    """The right way to block waiting for a `future` outside of a coroutine is to ask the event loop to do it:"""
    # loop = asyncio.get_event_loop()
    # print(loop.run_until_complete(myfuture1))
    # loop.close()

    several_futures = asyncio.gather(mycoro(1), mycoro(2), mycoro(3))
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(several_futures))
    loop.close()


## to call a coroutine from a coroutine
async def f2():
    print("start f2")
    await asyncio.sleep(1)
    print("stop f2")


async def f1():
    print("start f1")
    await f2()
    print("stop f1")


def call_coro_from_coro():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(f1())
    loop.close()


async def print_when_done(tasks):
    for res in asyncio.as_completed(tasks):
        print("Result %s" % await res)


async def mygather(*args):
    """asyncio.gather is roughly equivalent to:"""
    ret = []
    for r in (await asyncio.wait(args))[0]:
        ret.append(await r)
    return ret


def run_my_coroutine_as_completed():
    coros = [mycoro(1), mycoro(2), mycoro(3)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_when_done(coros))
    loop.close()


if __name__ == "__main__":
    # call_coro_from_coro()
    # run_my_coroutine_gather()

    run_my_coroutine_as_completed()
