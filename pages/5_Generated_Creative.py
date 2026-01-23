import streamlit as st

from frontend.utils.ui_base import (
    boot_ui,
    render_topbar,
    render_breadcrumb,
    render_section_header,
)
from frontend.ui_creative_details import inject_creative_details_css
from backend.orchestrator import generate_poster_prompt
from backend.agents.creative_generation import generate_creative_image


# ------------------ CONFIG ------------------
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
boot_ui(hide_streamlit_sidebar=True)
inject_creative_details_css()


# ------------------ HELPERS ------------------
def normalize_aspect_ratio(fmt):
    if isinstance(fmt, str):
        return fmt.strip().lower()
    if isinstance(fmt, (list, tuple, set)) and fmt:
        return str(next(iter(fmt))).strip().lower()
    return "square"


# ------------------ TOP UI ------------------
render_topbar("Nazish Ali", "Admin")
render_breadcrumb(
    "Content Vault > Project Details",
    st.session_state["project"].get("project_name", "Hiranandani Gardens"),
    "🏘️",
)
render_section_header("Generated Creative", "✨")


# ------------------ INITIAL PROMPT GENERATION ------------------
if "final_prompt" not in st.session_state:
    output = generate_poster_prompt(
        st.session_state["project"],
        st.session_state["creative"],
    )

    st.session_state["final_prompt"] = output["final_prompt"]
    st.session_state["negative_prompt"] = output["negative_prompt"]
    st.session_state["generated_image_path"] = None


# ------------------ DEFAULT IMAGE GENERATION ------------------
if st.session_state["generated_image_path"] is None:
    aspect_ratio = normalize_aspect_ratio(
        st.session_state["creative"].get("formats")
    )

    with st.spinner("Generating creative image..."):
        st.session_state["generated_image_path"] = generate_creative_image(
            prompt=st.session_state["final_prompt"],
            negative_prompt=st.session_state["negative_prompt"],
            aspect_ratio=aspect_ratio,
            background_path=st.session_state["creative"]["bg_file_path"],
            logo_path="assets/logo/Hiranandani-Gardens-Logo.png",
        )


# ------------------ UI LAYOUT ------------------
col_img, col_text = st.columns([1, 1.3])


# ------------------ RIGHT: PROMPT EDITING ------------------
with col_text:
    st.subheader("🎯 Edit Final Prompt")

    st.session_state["final_prompt"] = st.text_area(
        "Final Prompt",
        value=st.session_state["final_prompt"],
        height=450,
    )

    regenerate = st.button(
        "🔁 Re-Generate Image",
        use_container_width=True,
    )


# ------------------ RE-GENERATE ON CLICK ------------------
if regenerate:
    aspect_ratio = normalize_aspect_ratio(
        st.session_state["creative"].get("formats")
    )

    with st.spinner("Re-generating creative image..."):
        st.session_state["generated_image_path"] = generate_creative_image(
            prompt=st.session_state["final_prompt"],
            negative_prompt=st.session_state["negative_prompt"],
            aspect_ratio=aspect_ratio,
            background_path=st.session_state["creative"]["bg_file_path"],
            logo_path="assets/logo/Hiranandani-Gardens-Logo.png",
        )


# ------------------ LEFT: IMAGE DISPLAY ------------------
with col_img:

    if st.session_state.get("generated_image_path"):
        st.image(
            st.session_state["generated_image_path"],
            width="content",
        )
    else:
        st.warning("Image generation failed.")
