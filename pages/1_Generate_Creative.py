import streamlit as st
from frontend.utils.ui_base import boot_ui, render_topbar, render_breadcrumb, render_section_header

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
boot_ui(hide_streamlit_sidebar=True)

render_topbar()
render_breadcrumb("Content Vault > Project Details", "Hiranandani Gardens")

# Page-specific section header:
render_section_header("Creative Generation", "✨")

# Page-specific content starts here...
st.write("Page content here...")