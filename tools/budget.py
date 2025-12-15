def estimate_budget(flight, hotel, days):
    flight_cost = flight.get("price", 0) if isinstance(flight, dict) else 0
    hotel_cost = hotel.get("price_per_night", 0) * max(days - 1, 1) if isinstance(hotel, dict) else 0
    food_and_local = days * 800

    return {
        "flight_cost": flight_cost,
        "hotel_cost": hotel_cost,
        "food_and_local": food_and_local,
        "total_cost": flight_cost + hotel_cost + food_and_local
    }
