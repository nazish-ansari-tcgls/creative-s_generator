def visual_agent(poster_category, background_provided: bool):
    ''' Generate visual composition based on poster category and background presence '''
    base_visuals = {
        "Awareness": "cinematic skyline or aspirational aerial view",
        "Location": "project with contextual surroundings and connectivity cues",
        "Testimonials": "architecture with warm human presence silhouettes",
        "Lead Gen": "clean tower hero with clear CTA space",
        "Amenities & Lifestyle": "clubhouse, greenery, lifestyle amenities",
        "Festive & Seasonal": "architecture with subtle festive lighting",
        "Offers & Promotions": "bold architecture with uncluttered layout",
        "Brand Corp. Comms": "clean geometric architectural composition",
        "Milestone Achieved": "wide aerial showing project scale and progress",
        "Events & Experience": "architecture with live-event energy",
        "Retargeting": "calm, reassuring residential view"
    }

    visual = base_visuals.get(poster_category, "luxury aerial view")

    if background_provided:
        visual += (
            ", blended seamlessly with the provided background image "
            "while preserving background image realism"
        )

    return visual