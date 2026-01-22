from pathlib import Path
import uuid
from PIL import Image
import json
from typing import Any, Dict

# frontend/utils/project_store.py
import json
from pathlib import Path
import streamlit as st

DEFAULT_PROJECT_PATH = Path("assets/project/project.json")  # change if needed


def load_project_json(path: str | Path = DEFAULT_PROJECT_PATH) -> dict:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"project.json not found at: {path.resolve()}")
    return json.loads(path.read_text(encoding="utf-8"))


def ensure_project_in_session(path: str | Path = DEFAULT_PROJECT_PATH) -> dict:
    """Call on every page that needs project details."""
    if "project" not in st.session_state or not st.session_state["project"]:
        st.session_state["project"] = load_project_json(path)
    return st.session_state["project"]


def save_project_to_disk(path: str | Path = DEFAULT_PROJECT_PATH):
    """Optional: persist edits back to disk."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(st.session_state["project"], indent=2), encoding="utf-8")


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
