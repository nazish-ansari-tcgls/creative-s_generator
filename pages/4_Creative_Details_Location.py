import streamlit as st
import json
from backend.utils.image_utils import crop_to_aspect_ratio
from backend.utils.storage import load_project_json, save_uploaded_image, save_pil_image
from frontend.utils.ui_base import boot_ui, render_topbar, render_breadcrumb, render_section_header
from backend.agents.category_agent import category_agent_info
from backend.agents.messaging_agent import category_messaging_agent
from frontend.ui_creative_details import (
    inject_creative_details_css,
    render_category_pills,
    render_format_grid,
)

def _safe_list(x):
    if x is None:
        return []
    if isinstance(x, list):
        return x
    if isinstance(x, tuple):
        return list(x)
    if isinstance(x, str):
        return [x]
    return []

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
boot_ui(hide_streamlit_sidebar=True)
inject_creative_details_css()


# top chrome
render_topbar("Nazish Ali", "Admin")
render_breadcrumb("Content Vault > Project Details", st.session_state["project"].get("project_name", "Hiranandani Gardens"), "🏘️")
render_section_header("Creative Details", "✨")

headline = category_messaging_agent(st.session_state["project"], st.session_state["creative"]["category"])
st.session_state["creative"]["headline"] = headline



# ====== Card 1: Mandatory Details ======
# st.markdown('<div class="cg-card">', unsafe_allow_html=True)
st.markdown('<div class="cg-title">Enter the Details Below</div>', unsafe_allow_html=True)


# ---------- Headline / Core Thought (MANDATORY) ----------
st.markdown('<div class="field-label">Headline / Core Thought <span class="req">*</span></div>', unsafe_allow_html=True)

headline_val = st.text_input(
    label="Headline / Core Thought",
    value=st.session_state["creative"].get("headline"),
    placeholder='e.g., "Where Dreams Find Home"',
    key="headline_input",
    label_visibility="collapsed",
)