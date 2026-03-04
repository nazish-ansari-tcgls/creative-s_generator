# def styling_agent():
#     ''' Branding and layout styling for premium real estate posters '''
#     return {
#         "palette": "muted luxury tones, brand-aligned",
#         "typography": "modern minimal sans-serif",
#         "spacing": "editorial, generous margins"
#     }


# backend/agents/styling_agent.py

def styling_agent(category: str, brand_colors: list, font_style: str, background_provided: bool, constraints: dict) -> dict:
    """
    Returns a simple style plan: tone, contrast, palette, typography, logo rules.
    """
    tone_map = {
        "Awareness": ("aspirational", "medium"),
        "Location": ("informative", "high"),
        "Amenities & Lifestyle": ("experiential", "medium"),
        "Offers & Promotions": ("urgent", "high"),
    }

    tone, contrast = tone_map.get(category, ("luxury", "medium"))

    # Palette: use brand colors if provided, otherwise fall back
    palette = brand_colors[:2] if brand_colors else ["#111111", "#FFFFFF"]

    # Offers need strong contrast always
    if category == "Offers & Promotions":
        palette = (brand_colors[:1] if brand_colors else []) + ["#111111", "#FFFFFF"]

    typography = {
        "headline": "refined sans-serif" if "serif" not in (font_style or "").lower() else "elegant serif",
        "cta": "soft label/underline" if constraints.get("cta_style") != "hard" else "high-contrast button",
    }

    logo_rules = {
        "Awareness": ["Logo small and subtle", "Avoid heavy emboss"],
        "Location": ["Logo visible but not dominant", "Align to grid"],
        "Amenities & Lifestyle": ["Logo subtle, calm", "Keep premium whitespace"],
        "Offers & Promotions": ["Logo secondary to offer", "Offer block must dominate"],
    }.get(category, ["Logo subtle and consistent."])

    bg_treatment = None
    if background_provided:
        bg_treatment = "Preserve realism; slightly blur/dim behind text blocks if needed."

    # Category-based don’ts (style)
    dont = {
        "Awareness": ["Avoid urgency reds/yellows and discount badges"],
        "Location": ["Avoid decorative fonts; prioritize readability"],
        "Amenities & Lifestyle": ["Avoid infographic style; keep experiential"],
        "Offers & Promotions": ["Avoid low-contrast palette; don’t hide offer text"],
    }.get(category, [])

    return {
        "category": category,
        "tone": tone,
        "contrast": contrast,
        "palette": palette,
        "typography": typography,
        "logo_rules": logo_rules,
        "background_treatment": bg_treatment,
        "dont_style": dont,
    }
