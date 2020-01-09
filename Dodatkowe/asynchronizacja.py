import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

# async def main():
#     print(f"started at {time.strftime('%X')}")

#     await say_after(1, 'hello') 
#     await say_after(2, 'world')

#     print(f"finished at {time.strftime('%X')}")

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def main2():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A", 5),
        factorial("B", 10),
        factorial("C", 6),
    )


async def eternity():
    # Sleep for one hour
    await asyncio.sleep(6)
    print('yay!')

async def main3():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=6.1)
    except asyncio.TimeoutError:
        print('timeout!')

# asyncio.run(main())
# asyncio.run(main2())
asyncio.run(main3())