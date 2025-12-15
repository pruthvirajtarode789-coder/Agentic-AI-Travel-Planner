
import json

def search_flights(src, dest):
    with open("data/flights.json") as f:
        flights = json.load(f)
    results = [f for f in flights if f["from"].lower()==src.lower() and f["to"].lower()==dest.lower()]
    results.sort(key=lambda x: x["price"])
    return results[:3]
