#Student attendance system
import asyncio
async def mark_attendance(student):
    print(f"Marking attendance for {student}")
    await asyncio.sleep(2)
    print(f"{student} completed")
async def main():
    await asyncio.gather(
    mark_attendance("A"),
    mark_attendance("B"),
    mark_attendance("C")
    )
asyncio.run(main())