from dataclasses import dataclass
from typing import Optional 

@dataclass
class Project:
    name: str
    location: str
    developer: str
    category: str
    logo_path: Optional[str] = None
    background_path: Optional[str] = None

@dataclass
class Creative:
    poster_category: str
    aspect_ratio: str
    headline: str
    subline: str
    cta: str
