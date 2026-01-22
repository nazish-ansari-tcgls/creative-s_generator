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

def category_agent(poster_category: str):
    return CATEGORY_STRATEGY.get(poster_category, "premium real estate")

def category_agent_info():
    return CATEGORY_STRATEGY
