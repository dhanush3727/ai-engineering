# async/await:
import asyncio
import httpx

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

# Implement real API with get method
async def get_equipment_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(url, timeout=10)

            res.raise_for_status()

            data = res.json()
            
            print(data)

    except httpx.HTTPError as error:
        print(f"API request failed: {error}")

asyncio.run(get_equipment_data())

# Post method
async def post_equipment(post_id: int):
    url=f"https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title": f"Equipment {post_id}",
        "body": "Equipment breakdown report",
        "userId": post_id
    }

    try:
        async with httpx.AsyncClient() as client:
            res = await client.post(url, json=payload, timeout=10)

            res.raise_for_status()

            return res.json()

    except httpx.HTTPError as error:
        print(f"API request failed: {error}")

async def main():
    results = await asyncio.gather(post_equipment(1), post_equipment(2), post_equipment(3))

    for result in results:
        print(result)

asyncio.run(main())