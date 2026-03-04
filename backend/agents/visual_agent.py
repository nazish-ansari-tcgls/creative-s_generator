# def visual_agent(poster_category, background_provided: bool):
#     ''' Generate visual composition based on poster category and background presence '''
#     base_visuals = {
#         "Awareness": "cinematic skyline or aspirational aerial view",
#         "Location": "project with contextual surroundings and connectivity cues",
#         "Testimonials": "architecture with warm human presence silhouettes",
#         "Lead Gen": "clean tower hero with clear CTA space",
#         "Amenities & Lifestyle": "clubhouse, greenery, lifestyle amenities",
#         "Festive & Seasonal": "architecture with subtle festive lighting",
#         "Offers & Promotions": "bold architecture with uncluttered layout",
#         "Brand Corp. Comms": "clean geometric architectural composition",
#         "Milestone Achieved": "wide aerial showing project scale and progress",
#         "Events & Experience": "architecture with live-event energy",
#         "Retargeting": "calm, reassuring residential view"
#     }

#     visual = base_visuals.get(poster_category, "luxury aerial view")

#     if background_provided:
#         visual += (
#             ", blended seamlessly with the provided background image "
#             "while preserving background image realism"
#         )

#     return visual

# backend/agents/visual_agent.py

def visual_agent(category: str, background_provided: bool, constraints: dict) -> dict:
    """
    Returns a simple layout plan with composition rules for Gemini prompt.
    """
    hero_weight = constraints.get("hero_weight", 0.6)
    text_density = constraints.get("text_density", "medium")

    base_composition = {
        "Awareness": "Cinematic aspirational hero image, minimal text, premium natural element composition with background.",
        "Location": "Aerial/context hero with clean POI overlay and travel-time badges.",
        "Amenities & Lifestyle": "Lifestyle amenity scene with warm cinematic feel and minimal overlays.",
        "Offers & Promotions": "Background supports offer; offer block + CTA dominates with high contrast.",
    }.get(category, "Luxury hero image with clean hierarchy.")

    overlays = {
        "Awareness": [],
        "Location": ["POI markers", "Travel time badges", "Connectivity strip/panel"],
        "Amenities & Lifestyle": [],
        "Offers & Promotions": ["Offer badge/block", "Deadline/scarcity tag", "CTA button"],
    }.get(category, [])

    spacing = {
        "Awareness": ["Safe margins 8–10%", "Headline in calm zone", "Logo subtle in corner"],
        "Location": ["Reserve overlay zone", "Use translucent panel behind labels", "Consistent icon style"],
        "Amenities & Lifestyle": ["One main focal scene", "Text on soft panel if needed", "Keep uncluttered"],
        "Offers & Promotions": ["Offer in primary zone", "CTA below offer", "Mute/blur background for legibility"],
    }.get(category, ["Use safe zones and maintain readability."])

    bg_note = None
    if background_provided:
        bg_note = "Blend with provided background; preserve realism; use subtle panels for text contrast."

    return {
        "category": category,
        "hero_weight": hero_weight,
        "text_density": text_density,
        "composition": base_composition,
        "overlays": overlays,
        "spacing_rules": spacing,
        "background_note": bg_note,
    }
