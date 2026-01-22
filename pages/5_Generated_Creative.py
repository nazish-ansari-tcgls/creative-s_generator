import streamlit as st
import json
from backend.utils.image_utils import crop_to_aspect_ratio
from backend.utils.storage import load_project_json, save_uploaded_image, save_pil_image
from frontend.utils.ui_base import boot_ui, render_topbar, render_breadcrumb, render_section_header
from backend.orchestrator import generate_poster_prompt
from backend.agents.creative_generation import generate_creative_image
from frontend.ui_creative_details import (
    inject_creative_details_css,
    render_category_pills,
    render_format_grid,
)

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
boot_ui(hide_streamlit_sidebar=True)
inject_creative_details_css()


# top chrome
render_topbar("Nazish Ali", "Admin")
render_breadcrumb("Content Vault > Project Details", st.session_state["project"].get("project_name", "Hiranandani Gardens"), "🏘️")
render_section_header("Generated Creative", "✨")

prompt = generate_poster_prompt(project, creative)

with st.spinner("Generating creative image..."):
    generated_image_path = generate_creative_image(
        prompt=st.session_state.output["final_prompt"],
        negative_prompt=st.session_state.output["negative_prompt"],
        aspect_ratio=st.session_state.creative["formats"],
        background_path=st.session_state.creative["bg_file_path"],
        logo_path="assets/logo/Hiranandani-Gardens-Logo.png"     
         )




