import requests
from typing import TypedDict, TypeAlias

# Get Request
res = requests.get("https://httpbin.org/get", timeout=10)
print(res.status_code)
print(res.json())

# Post Request
JSONValue: TypeAlias = str | int | float | bool | None | list["JSONValue"] | dict[str, "JSONValue"]

class Equipment(TypedDict):
    name: str
    hours: int
    issue: str

url = "https://httpbin.org/post"

equipment: Equipment = {
    "name": "Industrial Pump",
    "hours": 2500,
    "issue": "Unusual vibration"
}

payload: dict[str, JSONValue] = equipment

try:
    res = requests.post(url, json=payload, timeout=10)
    res.raise_for_status()

    result = res.json()
    print("result", result["json"])
except requests.RequestException as error:
    print(f"Request failed: {error}")

# Practical exercise
try:
    res = requests.get("https://httpbin.org/get", timeout=10)
    res.raise_for_status()

    result = res.json()
    print("Get Result", result)
except requests.RequestException as error:
    print("Get Error", error)