import streamlit as st
from frontend.utils.ui_base import boot_ui, render_topbar, render_breadcrumb, render_section_header
from frontend.ui_dashboard import inject_dashboard_css, render_dashboard_cards

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
boot_ui(hide_streamlit_sidebar=True)
inject_dashboard_css()

render_topbar("Nazish Ali", "Admin")
render_breadcrumb("Content Vault > Project Details", "Hiranandani Gardens", "🏘️")
render_section_header("Creative Generation", "✨")

render_dashboard_cards()

# Invisible overlay click areas (keeps inside pill only, no white bar)
c1, c2 = st.columns(2, gap="large")

with c1:
    st.markdown('<div class="overlay-btn">', unsafe_allow_html=True)
    if st.button("Open Project DNA →", key="go_dna", use_container_width=True):
        st.switch_page("pages/2_Make_Your_Creative.py")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="overlay-btn">', unsafe_allow_html=True)
    if st.button("Open Creative Ad Magic →", key="go_admagic", use_container_width=True):
        st.switch_page("pages/1_Generate_Creative.py")
    st.markdown('</div>', unsafe_allow_html=True)

