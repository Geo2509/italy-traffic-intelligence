import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

URL = os.getenv("TRAFFIC_ENDPOINT")

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)

print("Status code:", response.status_code)
print("Content type:", response.headers.get("Content-Type"))

data = response.json()

print("\nMain Python type:")
print(type(data))

if isinstance(data, dict):
    print("\nDictionary keys:")
    print(data.keys())

    if "events" in data:
        records = data["events"]
    else:
        first_key = list(data.keys())[0]
        records = data[first_key]

elif isinstance(data, list):
    records = data

else:
    raise TypeError("Unknown JSON structure")

print("\nRecords type:")
print(type(records))

print("\nNumber of records:")
print(len(records))

print("\nFirst record:")
print(records[0])

print("\nKeys in first record:")
print(records[0].keys())

df = pd.DataFrame(records)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

df.to_csv("data/events_raw.csv", index=False)

print("\nSaved to data/events_raw.csv")