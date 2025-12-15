from tools.flights import search_flights
from tools.hotels import recommend_hotels
from tools.places import suggest_places
from tools.weather import get_weather


def plan_trip(src, dest, days, lat, lon):
    flights = search_flights(src, dest) or []
    hotels = recommend_hotels(dest) or []
    places = suggest_places(dest) or []
    weather = get_weather(lat, lon) or {}

    # ---------- SAFE FLIGHT ----------
    if isinstance(flights, list) and len(flights) > 0:
        selected_flight = flights[0]
    else:
        selected_flight = {
            "message": f"No direct flights found from {src} to {dest}"
        }

    # ---------- SAFE HOTEL ----------
    if isinstance(hotels, list) and len(hotels) > 0:
        selected_hotel = hotels[0]
    else:
        selected_hotel = {
            "message": f"No hotels found in {dest}"
        }

    # ---------- SAFE ITINERARY ----------
    itinerary = {}

    if isinstance(places, list) and len(places) > 0:
        for i in range(days):
            day_places = places[i::days]
            itinerary[f"Day {i + 1}"] = day_places if day_places else places[:2]
    else:
        itinerary["Day 1"] = [{
            "name": "No places found",
            "rating": "-",
            "type": "-"
        }]

    return {
        "flight": selected_flight,
        "hotel": selected_hotel,
        "itinerary": itinerary,
        "weather": weather.get("daily", {}).get("temperature_2m_max", [])
    }
