from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Pet:
    id: int
    name: str
    status: str
    photoUrls: List[str]  # Возвращаем поле photoUrls
    category: Optional[dict] = None
    tags: Optional[List[dict]] = None
