
"""
Single source of truth for colors/tokens.
Import from here in ui_base / ui_dashboard / other pages.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class Theme:
    BG: str = "#4A4472"              # page background
    SURFACE: str = "#3C376A"         # large section surface
    CARD: str = "#343064"            # cards
    CARD_2: str = "#2D2A5A"          # deeper cards
    BORDER: str = "rgba(255,255,255,0.10)"
    TEXT: str = "#F2F3FF"
    MUTED: str = "rgba(242,243,255,0.70)"
    ACCENT: str = "#2BF0B6"
    DOT: str = "#FF4D6D"             # sirrus red dot

THEME = Theme()
