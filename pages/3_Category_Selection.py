import streamlit as st
from frontend.utils.ui_base import boot_ui, render_topbar, render_breadcrumb, render_section_header
from frontend.ui_creative_details import inject_creative_details_css  # import only CSS, not renderers

def _init_state():
    if "creative" not in st.session_state:
        st.session_state["creative"] = {
            "category": "Awareness",
            "format": "1:1",
            "target_emotion": None,
            "bg_source": "upload",
            "bg_file_path": None,
            "optional": {
                "brand_story": "",
                "visual_metaphor": "",
                "price_range": "",
                "price_offers": "",
            },
        }

# ---------- Callbacks ----------
def set_category(cat: str):
    st.session_state["creative"]["category"] = cat
    st.rerun()

def toggle_format(fmt: str):
    
    if fmt == "portrait":
        cur = "4:5"
    elif fmt == "landscape":
        cur = "16:9"
    elif fmt == "story":
        cur = "9:16"
    else:
        cur = "1:1"

    st.session_state["creative"]["format"] = cur
    st.rerun()

# ---------- Renderers ----------
def render_category_pills_local(active: str):
    cats = [
        "Awareness", "Location", "Testimonials", "Lead Gen",
        "Amenities & Lifestyle", "Festive & Seasonal",
        "Offers & Promotions", "Brand Corp. Comms",
        "Milestone Achieved", "Events & Experience", "Retargeting"
    ]
    cols = st.columns(6)
    for i, cat in enumerate(cats):
        with cols[i % 6]:
            st.button(
                cat,
                key=f"cat_{cat}",
                type="primary" if cat == active else "secondary",
                on_click=set_category,
                args=(cat,),
                use_container_width=True,
            )

def render_format_grid_clickable_local(active: str):
    fmts = ["square","portrait","landscape","story"]
    cols = st.columns(4)
    for i, fmt in enumerate(fmts):
        with cols[i%4]:
            st.button(
                fmt,
                key=f"fmt_{fmt}",
                type="primary" if fmt == active else "secondary",
                on_click=toggle_format,
                args=(fmt,),
                use_container_width=True,
            )

# ---------- Page ----------
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
boot_ui(hide_streamlit_sidebar=True)
inject_creative_details_css()
_init_state()

render_topbar("Nazish Ali", "Admin")
render_breadcrumb("Content Vault > Project Details", st.session_state["project"].get("project_name", "Hiranandani Gardens"), "🏘️")
render_section_header("Category Selection", "✨")

st.markdown('<div class="cg-title">Creatives Category</div>', unsafe_allow_html=True)
render_category_pills_local(active=st.session_state["creative"]["category"])

st.markdown('<div class="cg-title">Creative Format</div>', unsafe_allow_html=True)
st.markdown('<div class="cg-sub">Select Aspect Ratios (Choose all that apply)</div>', unsafe_allow_html=True)
render_format_grid_clickable_local(st.session_state["creative"]["format"])

# st.write("DEBUG creative:", st.session_state["creative"])  # better than print()
print(st.session_state["creative"])

CATEGORY_TO_PAGE = {
    "Awareness": "pages/4_Creative_Details_Awareness.py",
    "Location": "pages/4_Creative_Details_Location.py",
    "Testimonials": "pages/4_Creative_Details_Testimonials.py",
    "Lead Gen": "pages/4_Creative_Details_LeadGen.py",
}

if st.button("Add Creative Details →", key="creative_details", use_container_width=True):
    cat = st.session_state["creative"]["category"]
    st.switch_page(CATEGORY_TO_PAGE.get(cat, "pages/4_Creative_Details_Awareness.py"))
