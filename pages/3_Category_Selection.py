import streamlit as st
import json
from backend.utils.storage import load_project_json
from frontend.utils.ui_base import boot_ui, render_topbar, render_breadcrumb, render_section_header
from backend.agents.category_agent import category_agent_info
from backend.agents.messaging_agent import category_messaging_agent
from frontend.ui_creative_details import (
    inject_creative_details_css,
    render_category_pills,
    render_format_grid,
    render_format_grid_clickable,
)


def _init_state():

    if "creative" not in st.session_state:
        st.session_state["creative"] = {
            "category": "Awareness", 
            "formats": set(["square"]), # default same as screenshot highlight "headline": "",
            "target_emotion": None,
            "bg_source": "upload",  # upload | pool
            "bg_file_path": None,
            "optional": {
                "brand_story": "",
                "visual_metaphor": "",
                "price_range": "",
                "price_offers": "",
            },
        }


st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
boot_ui(hide_streamlit_sidebar=True)
inject_creative_details_css()
_init_state()


# top chrome
render_topbar("Nazish Ali", "Admin")
render_breadcrumb("Content Vault > Project Details", st.session_state["project"].get("project_name", "Hiranandani Gardens"), "🏘️")
render_section_header("Category Selection", "✨")


# ====== Card 1: Category ======
st.markdown('<div class="cg-title">Creatives Category</div>', unsafe_allow_html=True)
render_category_pills(active=st.session_state["creative"]["category"])
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

# ====== Card 2: Format ======
st.markdown('<div class="cg-title">Creative Format</div>', unsafe_allow_html=True)
st.markdown('<div class="cg-sub">Select Aspect Ratios (Choose all that apply)</div>', unsafe_allow_html=True)

render_format_grid_clickable(st.session_state["creative"]["formats"])
st.markdown("</div>", unsafe_allow_html=True)
print(st.session_state["creative"]["formats"])
print(type(st.session_state["creative"]["formats"]))

# ====== Bottom Action ======
st.markdown('<div class="overlay-btn">', unsafe_allow_html=True)
if st.button("Add Creative Details →", key="creative_details", use_container_width=True):
    print(st.session_state["creative"])
    st.switch_page("pages/4_Creative_Details_Awareness.py")
st.markdown('</div>', unsafe_allow_html=True)
















