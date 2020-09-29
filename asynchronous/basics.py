import asyncio
import time
import random


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())


def async_mode_run():
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

def count_sync():
    print("One")
    time.sleep(1)
    print("Two")

def main_sync():
    for _ in range(3):
        count_sync()    


def sync_mode_run():
    s = time.perf_counter()
    main_sync()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

########################################################################
# ANSI colors
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)

async def makerandom(idx: int, threshold: int = 6) -> int:
    print(c[idx + 1] + f"Initiated makerandom({idx}).")
    i = random.randint(0, 10)
    while i <= threshold:
        print(c[idx + 1] + f"makerandom({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
    return i

async def main():
    # uses one main coroutine, makerandom(), and runs it concurrently across 3 different inputs.
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    return res


def random_colored_op():
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")

if __name__ == "__main__":
    # async_mode_run()
    # sync_mode_run()
    random_colored_op()