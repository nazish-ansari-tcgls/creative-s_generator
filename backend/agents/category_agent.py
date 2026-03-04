CATEGORY_STRATEGY = {
    "Awareness": "brand-first, emotional, aspirational",
    "Location": "map cues, connectivity, landmarks",
    "Testimonials": "trust-led, human warmth, credibility",
    "Lead Gen": "clear CTA, value-driven",
    "Amenities & Lifestyle": "lifestyle storytelling, experiential",
    "Festive & Seasonal": "emotional, cultural, celebratory",
    "Offers & Promotions": "urgency, clarity, contrast",
    "Brand Corp. Comms": "corporate, minimal, authoritative",
    "Milestone Achieved": "achievement, scale, pride",
    "Events & Experience": "live energy, people presence",
    "Retargeting": "familiarity, reassurance, conversion-focused"
}

# backend/constants.py
# backend/agents/category_agent.py

CATEGORY_RULES = {
    "Awareness": {
        "required_fields": ["headline"],
        "constraints": {"hero_weight": 0.7, "text_density": "low", "cta_style": "soft"},
        "do": [
            "Use aspirational hero image (dominant).",
            "Keep copy minimal and premium.",
            "Use soft CTA (Explore / Discover).",
        ],
        "dont": [
            "No discounts/urgency tags.",
            "No cluttered layout or too much text.",
            "No multiple CTAs.",
        ],
    },
    "Location": {
        "required_fields": ["project_location_name", "connectivity_points"],
        "constraints": {"hero_weight": 0.6, "text_density": "medium", "cta_style": "info", "poi_max": 6},
        "do": [
            "Use aerial/context view.",
            "Show POIs + travel time badges (3–6).",
            "Keep overlay clean and readable.",
        ],
        "dont": [
            "No overloaded map with too many POIs.",
            "No vague landmarks.",
            "No text directly on busy areas without panels.",
        ],
    },
    "Amenities & Lifestyle": {
        "required_fields": ["headline", "amenities_list"],
        "constraints": {"hero_weight": 0.7, "text_density": "low", "cta_style": "soft", "amenities_focus_max": 2},
        "do": [
            "Show lifestyle scenes with people if possible.",
            "Focus on 1–2 amenities per creative.",
            "Use warm premium lighting.",
        ],
        "dont": [
            "No long amenity list dump.",
            "No infographic-heavy layout.",
            "No urgency/offer language.",
        ],
    },
    "Offers & Promotions": {
        "required_fields": ["offer_text", "deadline", "cta"],
        "constraints": {"hero_weight": 0.35, "text_density": "high", "cta_style": "hard", "offer_primary": True},
        "do": [
            "Offer must be the biggest element.",
            "Use high contrast badges/blocks.",
            "Use strong CTA (Book Now / Claim Offer).",
        ],
        "dont": [
            "No hiding offer in small text.",
            "No multiple offers.",
            "No long paragraphs of terms.",
        ],
    },
}


def category_agent(category: str) -> dict:
    """
    Returns:
      - constraints (layout + behavior hints)
      - do/dont rules
      - missing_required_fields
    """
    if category not in CATEGORY_RULES:
        raise ValueError(f"Unsupported category: {category}")

    rules = CATEGORY_RULES[category]
    required = rules["required_fields"]

    return {
        "category": category,
        "required_fields": required,
        "constraints": rules["constraints"],
        "do": rules["do"],
        "dont": rules["dont"],
    }


def category_agent_info():
    return CATEGORY_STRATEGY
