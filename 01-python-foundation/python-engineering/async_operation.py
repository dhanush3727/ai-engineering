# async/await:
import asyncio

async def get_equipment():
    print("Fetching equipment...")
    await asyncio.sleep(2)
    print("Equipment received")

asyncio.run(get_equipment())

# Simulate both async task concurrently
async def summarize_breakdown(equipment: str) -> str:
    print(f"Requesting summary for {equipment}")

    await asyncio.sleep(2) # Simulate an AI API call

    return f"Summary ready for {equipment}"

async def main():
    # simulate both concurrently
    results = await asyncio.gather(summarize_breakdown("Pump"), summarize_breakdown("Motor"))

    for result in results:
        print("Equipment",result)

asyncio.run(main())

# Practical Exercise
async def check_equipment():
    print("Checking equipment...")
    await asyncio.sleep(1)
    print("Equipment check complete")
asyncio.run(check_equipment())