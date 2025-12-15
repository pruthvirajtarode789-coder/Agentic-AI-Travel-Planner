from langchain_core.tools import tool
from tools.flights import search_flights
from tools.hotels import recommend_hotels
from tools.places import suggest_places
from tools.weather import get_weather
from tools.budget import estimate_budget

@tool
def flight_search_tool(src: str, dest: str):
    """Search for flights between two cities."""
    return search_flights(src, dest)

@tool
def hotel_recommendation_tool(city: str):
    """Recommend hotels in a city."""
    return recommend_hotels(city)

@tool
def places_discovery_tool(city: str):
    """Suggest places to visit in a city."""
    return suggest_places(city)

@tool
def weather_tool(lat: float, lon: float):
    """Get weather forecast for a location."""
    return get_weather(lat, lon)

@tool
def budget_tool(flight: dict, hotel: dict, days: int):
    """Estimate budget for a trip."""
    return estimate_budget(flight, hotel, days)
