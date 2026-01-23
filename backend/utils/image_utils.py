# backend/utils/image_utils.py

from PIL import Image
import io

def crop_to_aspect_ratio(uploaded_file_path, aspect_ratio: str) -> Image.Image:
    """
    Takes a Streamlit UploadedFile and returns a cropped PIL Image.
    """

    # Convert UploadedFile → PIL Image
    image = Image.open(uploaded_file_path).convert("RGB")

    width, height = image.size

    if aspect_ratio == "1:1" or aspect_ratio == "square":
        target_ratio = 1 / 1
    elif aspect_ratio == "4:5"  or aspect_ratio == "portrait":
        target_ratio = 4 / 5
    elif aspect_ratio == "9:16"  or aspect_ratio == "landscape":
        target_ratio = 9 / 16
    elif aspect_ratio == "16:9"  or aspect_ratio == "story":
        target_ratio = 16 / 9
    else:
        return image

    current_ratio = width / height

    if current_ratio > target_ratio:
        # Crop width
        new_width = int(height * target_ratio)
        left = (width - new_width) // 2
        right = left + new_width
        top = 0
        bottom = height
    else:
        # Crop height
        new_height = int(width / target_ratio)
        top = (height - new_height) // 2
        bottom = top + new_height
        left = 0
        right = width

    return image.crop((left, top, right, bottom))

def image_path_to_bytes(image_path: str) -> bytes:
    """
    Convert an image file path into raw image bytes.
    """
    with open(image_path, "rb") as f:
        return f.read()