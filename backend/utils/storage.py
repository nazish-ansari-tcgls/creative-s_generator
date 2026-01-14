from pathlib import Path
import uuid
from PIL import Image

def save_pil_image(
    image: Image.Image,
    folder: str = "assets/inputs",
    prefix: str = "bg",
    format: str = "JPEG"
) -> str:
    Path(folder).mkdir(parents=True, exist_ok=True)

    filename = f"{prefix}_{uuid.uuid4().hex}.jpg"
    path = Path(folder) / filename

    image.save(path, format=format, quality=95)
    return str(path)

def save_uploaded_image(uploaded_file, folder="assets/inputs", prefix="input") -> str:
    if uploaded_file is None:
        return None

    Path(folder).mkdir(parents=True, exist_ok=True)

    ext = uploaded_file.name.split(".")[-1]
    filename = f"{prefix}_{uuid.uuid4().hex}.{ext}"
    file_path = Path(folder) / filename

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return str(file_path)
