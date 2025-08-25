# database/db.py
from dataclasses import dataclass
from typing import List

@dataclass
class Provider:
    id: int
    name: str
    tags: List[str]
    lat: float
    lon: float
    phone: str
    is_open_24_7: bool
    info: str
    photo_url: str

# Demo ma'lumotlar
PROVIDERS = [
    Provider(
        id=1,
        name="AutoFix Elektrik",
        tags=["elektrik", "universal"],
        lat=41.311081, lon=69.240562,
        phone="+998901112233",
        is_open_24_7=True,
        info="Электрика, диагностика, стартер/генератор, выездной осмотр.",
        photo_url="https://picsum.photos/seed/1/800/500"
    ),
    Provider(
        id=2,
        name="Kasotprav Master",
        tags=["kasoprav", "universal"],
        lat=41.327, lon=69.281,
        phone="+998933334455",
        is_open_24_7=False,
        info="Кастоправ, кузовной ремонт, покраска.",
        photo_url="https://picsum.photos/seed/2/800/500"
    ),
]
