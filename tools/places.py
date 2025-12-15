
import json

def suggest_places(city):
    with open("data/places.json") as f:
        places = json.load(f)
    results = [p for p in places if p["city"].lower()==city.lower()]
    results.sort(key=lambda x: -x["rating"])
    return results[:5]
