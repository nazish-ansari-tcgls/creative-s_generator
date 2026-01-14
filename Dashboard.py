import sys
from pathlib import Path

# -------------------------------------------------------------------
# PATH FIX (so backend imports work in Streamlit)
# -------------------------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

# -------------------------------------------------------------------
# IMPORTS
# -------------------------------------------------------------------
import streamlit as st
from PIL import Image

from backend.schemas import Project, Creative
from backend.orchestrator import generate_poster_prompt
from backend.utils.storage import save_uploaded_image, save_pil_image
from backend.utils.image_utils import crop_to_aspect_ratio
from backend.agents.creative_generation import generate_creative_image

# -------------------------------------------------------------------
# STREAMLIT CONFIG
# -------------------------------------------------------------------
st.set_page_config(
    page_title="Real Estate Poster Generator",
    layout="wide"
)

st.title("🏢 Real Estate Poster Generator")

# -------------------------------------------------------------------
# SESSION STATE INIT
# -------------------------------------------------------------------
for key in [
    "output",
    "bg_image_path",
    "logo_image_path",
    "cropped_img",
    "project",
    "creative"
]:
    if key not in st.session_state:
        st.session_state[key] = None

# -------------------------------------------------------------------
# UI – POSTER CATEGORY
# -------------------------------------------------------------------
poster_category = st.selectbox(
    "Poster Category",
    [
        "Awareness",
        "Location",
        "Testimonials",
        "Lead Gen",
        "Amenities & Lifestyle",
        "Festive & Seasonal",
        "Offers & Promotions",
        "Brand Corp. Comms",
        "Milestone Achieved",
        "Events & Experience",
        "Retargeting"
    ]
)

# -------------------------------------------------------------------
# UI – INPUTS
# -------------------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    project_name = st.text_input("Project Name")
    location = st.text_input("Location")
    developer = st.text_input("Developer Name")

    logo_file = st.file_uploader(
        "Upload Project Logo (PNG/JPG)",
        type=["png", "jpg", "jpeg"]
    )

    bg_file = st.file_uploader(
        "Upload Background Image",
        type=["png", "jpg", "jpeg"]
    )

with col2:
    headline = st.text_input("Headline")
    subline = st.text_input("Supporting Line")
    cta = st.text_input("CTA", value="ENQUIRE")

aspect_ratio = st.selectbox("Aspect Ratio", ["1:1", "9:16", "16:9"])

st.divider()

# -------------------------------------------------------------------
# BUTTON 1 – GENERATE PROMPT
# -------------------------------------------------------------------
if st.button("🧠 Generate Creative Prompt", use_container_width=True):

    # ---- LOGO SAVE ----
    logo_image_path = (
        save_uploaded_image(
            uploaded_file=logo_file,
            folder="assets/inputs",
            prefix="logo"
        )
        if logo_file else None
    )

    # ---- BACKGROUND CROP ----
    cropped_img = (
        crop_to_aspect_ratio(bg_file, aspect_ratio)
        if bg_file else None
    )

    bg_image_path = (
        save_pil_image(
            image=cropped_img,
            folder="assets/inputs",
            prefix="bg"
        )
        if cropped_img else None
    )

    # ---- DATA OBJECTS ----
    project = Project(
        name=project_name,
        location=location,
        developer=developer,
        category="Category-A",
        logo_path=logo_image_path,
        background_path=bg_image_path
    )

    creative = Creative(
        poster_category=poster_category,
        aspect_ratio=aspect_ratio,
        headline=headline,
        subline=subline,
        cta=cta
    )

    # ---- PROMPT GENERATION ----
    output = generate_poster_prompt(project, creative)

    # ---- SAVE TO SESSION ----
    st.session_state.output = output
    st.session_state.bg_image_path = bg_image_path
    st.session_state.logo_image_path = logo_image_path
    st.session_state.cropped_img = cropped_img
    st.session_state.project = project
    st.session_state.creative = creative

    st.success("Prompt generated successfully!")

# -------------------------------------------------------------------
# SHOW PROMPT + IMAGE PREVIEW
# -------------------------------------------------------------------
if st.session_state.output:

    col_img, col_text = st.columns([1, 1.3])

    with col_img:
        st.subheader("🖼️ Background Preview")
        if st.session_state.cropped_img:
            st.image(
                st.session_state.cropped_img,
                caption=f"Cropped to {aspect_ratio}",
                width="content"
            )
        else:
            st.warning("No background image uploaded.")

    with col_text:
        st.subheader("🎯 Final Image Generation Prompt")
        st.text_area(
            "Prompt",
            st.session_state.output["final_prompt"],
            height=400
        )

        st.subheader("🚫 Negative Prompt")
        st.text_area(
            "Negative Prompt",
            st.session_state.output["negative_prompt"],
            height=160
        )

st.divider()

# -------------------------------------------------------------------
# BUTTON 2 – GENERATE CREATIVE IMAGE
# -------------------------------------------------------------------
if st.button("🎨 Generate Creative Image", use_container_width=True):

    if not st.session_state.output:
        st.error("Please generate the creative prompt first.")
    elif not st.session_state.bg_image_path:
        st.error("Please upload a background image.")
    else:
        with st.spinner("Generating creative image..."):
            generated_image_path = generate_creative_image(
                prompt=st.session_state.output["final_prompt"],
                negative_prompt=st.session_state.output["negative_prompt"],
                aspect_ratio=st.session_state.creative.aspect_ratio,
                background_path=st.session_state.bg_image_path,
                logo_path=st.session_state.logo_image_path
            )

            generated_image = Image.open(generated_image_path)

        st.success("Creative image generated successfully!")
        st.image(
            generated_image,
            caption="Generated Creative",
            width='stretch'
        )
