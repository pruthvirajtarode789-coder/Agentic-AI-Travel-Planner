import json
import os

def recommend_hotels(city):
    try:
        data_path = os.path.join("data", "hotels.json")

        with open(data_path, "r", encoding="utf-8") as f:
            hotels = json.load(f)

        results = [
            h for h in hotels
            if isinstance(h, dict)
            and h.get("city", "").lower() == city.lower()
        ]

        # Always return a LIST
        if not results:
            return []

        results.sort(
            key=lambda x: (-x.get("stars", 0), x.get("price_per_night", 0))
        )

        return results[:3]

    except Exception as e:
        print("Hotel tool error:", e)
        return []
