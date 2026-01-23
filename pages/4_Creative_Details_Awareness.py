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

st.session_state["creative"]["headline"] = headline_val

st.markdown(
    '<div class="smallhint">The main message that captures your brand essence</div>',
    unsafe_allow_html=True
)

st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)


# Brand tone + target emotion
tone_options = _safe_list(["Luxury", "Warm", "Bold", "Minimal"])
emotion_options = ["Trust-led", "Pride", "Aspirational", "Comfort"]

saved_tone = st.session_state.get("creative", {}).get("brand_tone")
saved_emotion = st.session_state.get("creative", {}).get("target_emotion")

if saved_tone in tone_options:
    default_index = tone_options.index(saved_tone)
else:
    default_index = 0  # fallback safely
if saved_emotion in emotion_options:
    default_index = emotion_options.index(saved_emotion)
else:
    default_index = 0  # fallback safely
# Two columns
t1, t2 = st.columns(2, gap="large")
with t1:
    st.session_state["creative"]["brand_tone"] = st.selectbox(
        "Brand Tone",
        options=tone_options,
        index=default_index,
        key="brand_tone_select"
    )
    
    st.markdown('<div class="smallhint">How your brand communicates</div>', unsafe_allow_html=True)

with t2:
    st.session_state["creative"]["target_emotion"] = st.selectbox(
        "Target Emotion",
        options=emotion_options,
        index=default_index,
        key="target_emotion_select"
    )
    st.markdown('<div class="smallhint">The feeling you want to evoke</div>', unsafe_allow_html=True)

# Background image selector
st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
st.markdown('<div style="font-weight:900; margin-bottom:6px;">Background Image *</div>', unsafe_allow_html=True)

tab_left, tab_right = st.columns(2, gap="large")
with tab_left:
    if st.button("Upload New", use_container_width=True, key="bg_upload_tab"):
        st.session_state["creative"]["bg_source"] = "upload"
with tab_right:
    if st.button("Project Pool", use_container_width=True, key="bg_pool_tab"):
        st.session_state["creative"]["bg_source"] = "pool"

# Tabs look (HTML)
is_upload = st.session_state["creative"]["bg_source"] == "upload"

if is_upload:
    bg = st.file_uploader(
        "Upload background image",
        type=["png", "jpg", "jpeg"],
        key="bg_uploader",
        label_visibility="collapsed",
    )
    if bg is not None:
        cropped_img = crop_to_aspect_ratio(
            bg,
            st.session_state["creative"].get("formats")
        )
        if cropped_img:
            bg_image_path = save_pil_image(
                image=cropped_img,
                folder="assets/inputs",
                prefix="bg"
            )
        else:
            bg_image_path = None
        st.session_state["creative"]["bg_file_path"] = bg_image_path
else:
    # Placeholder: replace with your project pool gallery later
    st.info("Project Pool will be wired to your saved project images next.")
    st.session_state["creative"]["bg_file_path"] = None

st.markdown("</div>", unsafe_allow_html=True)

# ====== Optional section ======
st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
with st.expander("Additional Details", expanded=False):
    opt = st.session_state["creative"]["optional"]
    opt["brand_story"] = st.text_area("Brand Story", value=opt["brand_story"], placeholder="Tell your brand story in 1-2 lines", key="opt_brand_story")
    opt["visual_metaphor"] = st.text_input("Visual Metaphor", value=opt["visual_metaphor"], placeholder="e.g., sky, light, home, family, skyline", key="opt_visual_metaphor")
    opt["price_range"] = st.text_input("Price Range", value=opt["price_range"], placeholder="e.g., ₹45L – ₹1.2Cr", key="opt_price_range")
    opt["price_offers"] = st.text_input("Price Offers", value=opt["price_offers"], placeholder="e.g., Starting at ₹45 Lakhs*", key="opt_price_offers")

# ===== Bottom Buttons =====
left, right = st.columns([1, 1], gap="large")
with left:
    st.markdown('<div class="btn-ghost">', unsafe_allow_html=True)
    if st.button("Cancel", use_container_width=True, key="btn_cancel"):
        st.switch_page("Dashboard.py")
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
    if st.button("Generate", use_container_width=True, key="btn_generate"):
        # Example validation gate (keeps UI strict)
        if (
            not st.session_state["creative"]["headline"].strip()
            or st.session_state["creative"]["brand_tone"] in (None, "Select the Source")
            or st.session_state["creative"]["target_emotion"] in (None, "Select the Source")
            or (st.session_state["creative"]["bg_source"] == "upload" and st.session_state["creative"]["bg_file_path"] is None)
        ):
            st.warning("Please fill all mandatory fields.")
        else:
            # move to next page (your generation page)
            print(st.session_state["creative"])
            st.switch_page("pages/5_Generated_Creative.py")

        st.markdown("</div>", unsafe_allow_html=True)


