from google import genai
from google.genai import types
from PIL import Image
from backend.utils.image_utils import image_path_to_bytes
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(Path("/Users/nazishansari/Documents/creative's_generator/.env"))
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_creative_image(prompt: str, negative_prompt: str, aspect_ratio: str, background_path: str, logo_path: str) -> str:

    bg_image_bytes = image_path_to_bytes(background_path)
    logo_image_bytes = image_path_to_bytes(logo_path)

    bg_image = types.Part.from_bytes(
    data=bg_image_bytes, mime_type="image/jpeg"
    )

    logo_image = types.Part.from_bytes(
    data=logo_image_bytes, mime_type="image/jpeg"
    )

    resolution = "2K" if aspect_ratio in ["16:9", "9:16"] else "1K"

    response = client.models.generate_content(
        model="gemini-3-pro-image-preview",
        contents=[prompt+"Mandatory** Use both background and logo images for generating poster creative's along with all mentioned specifications", bg_image, logo_image],
        config=types.GenerateContentConfig(
        response_modalities=['TEXT','IMAGE'],
        image_config=types.ImageConfig(
            aspect_ratio=aspect_ratio,
            resolution=resolution,
            ),
        )
    )

    
    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = part.as_image()
            image_path = "assets/outputs/generated_image.png"
            image.save(image_path)

    return image_path