import json
import streamlit as st
from backend.utils.storage import load_project_json
from frontend.utils.ui_base import boot_ui, render_topbar, render_breadcrumb, render_section_header
from frontend.ui_project_details import (
    inject_project_details_css,
    render_project_details,
    render_brand_details,
)

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

boot_ui(hide_streamlit_sidebar=True)
inject_project_details_css()

st.session_state["project"] = load_project_json()
project = st.session_state["project"]

# Top chrome + breadcrumb + section header (same as your design language)
render_topbar("Nazish Ali", "Admin")
render_breadcrumb("Content Vault > Project Details", project.get("project_name", "Project"), "🏘️")
render_section_header("Project Details", "✨")

# Main content
render_project_details(project)
render_section_header("Content Details", "✨")
render_brand_details(project)

# Bottom actions
st.markdown('<div class="bottom-actions">', unsafe_allow_html=True)
c1, c2 = st.columns([1, 1])
with c1:
    st.markdown('<div class="btn-outline">', unsafe_allow_html=True)
    if st.button("Cancel", use_container_width=True):
        st.session_state["project"] = {}
        st.switch_page("pages/0_Dashboard.py")
    st.markdown("</div>", unsafe_allow_html=True)
with c2:
    st.markdown('<div class="btn-solid">', unsafe_allow_html=True)
    if st.button("Save & Next", use_container_width=True):
        st.switch_page("pages/3_Category_Selection.py")
    st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)




