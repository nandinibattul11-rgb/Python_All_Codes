# Demo Program 2
import asyncio
async def fn():
    print('This is ')
    await asyncio.sleep(1)
    print('asynchronous programming')
    await asyncio.sleep(2)
    print('and not multi-threading')
asyncio.run(fn())
