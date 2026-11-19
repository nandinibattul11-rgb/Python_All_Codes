# Simple program
import asyncio
async def example():
    print("Task started")
    await asyncio.sleep(2)
    print("Task completed")
asyncio.run(example()) 