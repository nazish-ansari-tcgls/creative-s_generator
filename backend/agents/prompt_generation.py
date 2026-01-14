from google import genai
from google.genai import types
import requests
import os
from backend.utils.image_utils import image_path_to_bytes
from dotenv import load_dotenv
from pathlib import Path


load_dotenv(Path("/Users/nazishansari/Documents/creative's_generator/.env"))
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def llm_prompt_generator(text, image_path):
    image_bytes = image_path_to_bytes(image_path)

    image = types.Part.from_bytes(
    data=image_bytes, mime_type="image/jpeg"
    )

    prompt = f'''
    Create an enhanced image generation prompt for a real estate poster based on the following description.
    Focus on clarity, luxury appeal, and architectural accuracy.
    Integrate the provided image as a background reference, ensuring it complements the poster's theme.
    Emphasize premium design elements and a sophisticated visual style.
    Avoid clutter, unrealistic styles, and any distortions.
    Here is the initial description:
    {text}
    '''

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[text, image],
    )

    # print(response.text)
    return response.text