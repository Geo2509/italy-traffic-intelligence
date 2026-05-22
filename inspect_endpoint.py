import requests
import pandas as pd

URL = "https://viabilita.autostrade.it/json/eventi.json"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)

print("Status code:", response.status_code)
print("Content type:", response.headers.get("Content-Type"))

data = response.json()

print("\nPython type:")
print(type(data))

print("\nLength:")
print(len(data))

print("\nDictionary keys:")
print(data.keys())

df = pd.DataFrame(data)

events = data["events"]

print("\nNumber of events:")
print(len(events))

print("\nFirst event:")
print(events[0])

print("\nKeys in first event:")
print(events[0].keys())

df = pd.DataFrame(events)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

df.to_csv("data/events_raw.csv", index=False)

print("\nSaved to data/events_raw.csv")