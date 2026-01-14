from backend.constants import QUALITY_BOOSTER

def synthesizer_agent(project, creative, strategy, visual, styling, messaging):
    logo_instruction = ""
    background_instruction = ""

    if project.logo_path:
        logo_instruction = (
            "Reserve a clean, high-contrast logo-safe area "
            "in the top or bottom corner. "
            "Do not stylize, distort, or recreate the logo."
        )

    if project.background_path:
        background_instruction = (
            "Use the provided background image as contextual inspiration, "
            "blending it softly without overpowering and modifying the architecture."
        )

    return f"""
A premium Category-A real estate social post image prompt with taking provided image as background image for this poster.

Project: {project.name}, {project.location}
Developer: {project.developer}

Creative intent:
{strategy}

Hero visual:
{visual}

Background guidance:
{background_instruction}

Branding guidance:
{logo_instruction}

Text to include:
Headline: "{messaging['headline']}"
Subline: "{messaging['subline']}"
CTA: "{messaging['cta']}"

Styling:
{styling['palette']}, {styling['typography']}, {styling['spacing']}.

Layout rules:
- Clear hierarchy
- Generous negative space
- Architecture remains the hero
- Logo area must remain uncluttered

Overall mood:
Luxury, calm, trustworthy, corporate credibility.

{QUALITY_BOOSTER}
""".strip()
