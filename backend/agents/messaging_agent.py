from google import genai
from google.genai import types
import requests
import os
import json
from backend.utils.image_utils import image_path_to_bytes
from dotenv import load_dotenv
from pathlib import Path
from backend.agents.category_agent import category_agent_info


load_dotenv(Path("/Users/nazishansari/Documents/creative's_generator/.env"))
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
client = genai.Client(api_key="AIzaSyCB_IwCTC7iKEJH8boDO04Y3MKH1iUitcU")

def messaging_agent(headline, subline, cta):
    return {
        "headline": headline.upper(),
        "subline": subline,
        "cta": cta
    }

def category_messaging_agent(project_info: str, category: str) -> str:

    categories_info = category_agent_info()

    prompt = f'''
    Give a suitable headline for this {category}.
    Do consider the project Information: {json.dumps(project_info)} 
    and poster categories : {', '.join(categories_info.keys())} to' give best headline.
    Your response should be concise and catchy.'''

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt],
    )

    # print(response.text)
    return response.text
