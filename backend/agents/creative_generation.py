from google import genai
from google.genai import types
from PIL import Image
from backend.utils.image_utils import image_path_to_bytes
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(Path("/Users/nazish/Documents/creative-s_generator/.env"))
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_creative_image(prompt: str, aspect_ratio: str, background_path: str, logo_path: str) -> str:

    bg_image_bytes = image_path_to_bytes(background_path)
    logo_image_bytes = image_path_to_bytes(logo_path)

    bg_image = types.Part.from_bytes(
    data=bg_image_bytes, mime_type="image/jpeg"
    )

    logo_image = types.Part.from_bytes(
    data=logo_image_bytes, mime_type="image/jpeg"
    )
    

    if  aspect_ratio == "square":
        aspect_ratio = "1:1"
    elif aspect_ratio == "portrait":
        aspect_ratio = "4:5"
    elif aspect_ratio == "landscape":
        aspect_ratio = "9:16"
    elif aspect_ratio == "story":
        aspect_ratio = "9:16"
    

    resolution = "2K" if aspect_ratio in ["16:9", "9:16"] else "1K"

    response = client.models.generate_content(
        model="gemini-3-pro-image-preview",
        contents=[prompt+"Mandatory** Use both background and logo images for generating poster creative's along with all mentioned specifications", bg_image, logo_image],
        config=types.GenerateContentConfig(
        response_modalities=['IMAGE'],
        image_config=types.ImageConfig(
            aspect_ratio=aspect_ratio,
            image_size=resolution,
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


def regenerate_creative_image(text_position: str, primary_text_color: str, secondary_text_color: str, aspect_ratio: str, background_path: str) -> str:
    bg_image_bytes = image_path_to_bytes(background_path)

    bg_image = types.Part.from_bytes(
    data=bg_image_bytes, mime_type="image/jpeg"
    )
    

    if  aspect_ratio == "square":
        aspect_ratio = "1:1"
    elif aspect_ratio == "portrait":
        aspect_ratio = "4:5"
    elif aspect_ratio == "landscape":
        aspect_ratio = "9:16"
    elif aspect_ratio == "story":
        aspect_ratio = "9:16"
    

    resolution = "2K" if aspect_ratio in ["16:9", "9:16"] else "1K"

    response = client.models.generate_content(
        model="gemini-3-pro-image-preview",
        contents=["Change the position of text in this image to" + text_position + " . And all text colour should be " + primary_text_color + "and" + secondary_text_color + ". Must remove the existing text should not be replicated in generated image.", bg_image],
        config=types.GenerateContentConfig(
        response_modalities=['IMAGE'],
        image_config=types.ImageConfig(
            aspect_ratio=aspect_ratio,
            image_size=resolution,
            ),
        )
    )

    
    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = part.as_image()
            image_path = "assets/outputs/modified_image.png"
            image.save(image_path)

    return image_path