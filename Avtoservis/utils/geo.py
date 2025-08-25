# utils/geo.py
import math
from database.db import Provider, PROVIDERS
from typing import List, Tuple

def haversine_km(lat1, lon1, lat2, lon2) -> float:
    R = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlmb = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dlmb/2)**2
    return 2 * R * math.asin(math.sqrt(a))

def find_nearby_providers(user_lat: float, user_lon: float, tag: str, limit: int = 3) -> List[Tuple[Provider, float]]:
    filtered = []
    for p in PROVIDERS:
        if tag == "universal":
            if "universal" in p.tags:
                dist = haversine_km(user_lat, user_lon, p.lat, p.lon)
                filtered.append((p, dist))
        else:
            if tag in p.tags:
                dist = haversine_km(user_lat, user_lon, p.lat, p.lon)
                filtered.append((p, dist))
    filtered.sort(key=lambda x: x[1])
    return filtered[:limit]
