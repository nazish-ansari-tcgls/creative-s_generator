import streamlit as st

from frontend.utils.ui_base import (
    boot_ui,
    render_topbar,
    render_breadcrumb,
    render_section_header,
)
from frontend.ui_creative_details import inject_creative_details_css
from backend.orchestrator import generate_poster_prompt
from backend.agents.creative_generation import generate_creative_image, regenerate_creative_image


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
    st.session_state["final_prompt"] = generate_poster_prompt(
        st.session_state["project"],
        st.session_state["creative"],
    )
    print("abcd")
    print(st.session_state["final_prompt"])

# ------------------ DEFAULT IMAGE GENERATION ------------------
if "generated_image_path" not in st.session_state:
    st.session_state["generated_image_path"] = None

if "output" not in st.session_state:
    st.session_state["output"] = None

if st.session_state["generated_image_path"] is None:
    aspect_ratio = normalize_aspect_ratio(
        st.session_state["creative"].get("formats")
    )

    with st.spinner("Generating creative image..."):
        st.session_state["generated_image_path"] = generate_creative_image(
            prompt=st.session_state["final_prompt"],
            aspect_ratio=aspect_ratio,
            background_path=st.session_state["creative"]["bg_file_path"],
            logo_path="assets/logo/Hiranandani-Gardens-Logo.png",
        )

col_img, col_text = st.columns([2, 1])
# ------------------ RIGHT: TEXT STYLING CONTROLS ------------------

with col_text:
    st.subheader("🎨 Text Styling")

    # ---- Text Colors ----
    col1, col2 = st.columns(2)

    with col1:
        st.session_state["primary_text_color"] = st.color_picker(
            "Primary Text Color",
            value=st.session_state.get("primary_text_color", "#FFFFFF"),
        )

    with col2:
        st.session_state["secondary_text_color"] = st.color_picker(
            "Secondary Text Color",
            value=st.session_state.get("secondary_text_color", "#FFD700"),
        )

    # ---- Text Position ----
    options = [
        "top-left",
        "top-center",
        "top-right",
        "center",
        "bottom-left",
        "bottom-center",
        "bottom-right",
    ]

    default_position = st.session_state.get("text_position", "bottom-center")
    if default_position not in options:
        default_position = "bottom-center"

    st.session_state["text_position"] = st.selectbox(
        "Text Position",
        options=options,
        index=options.index(default_position)
    )

    st.divider()

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
        st.session_state["generated_image_path"] = regenerate_creative_image(
            text_position=st.session_state["text_position"],
            primary_text_color=st.session_state["primary_text_color"],
            secondary_text_color=st.session_state["secondary_text_color"],
            aspect_ratio=aspect_ratio,
            background_path=st.session_state["generated_image_path"]
        )


# ------------------ LEFT: IMAGE DISPLAY ------------------
with col_img:

    if st.session_state.get("generated_image_path"):
        st.image(
            st.session_state["generated_image_path"],
            width="content",
        )

        with open(st.session_state["generated_image_path"], "rb") as f:
            st.download_button(
                label="⬇️ Download Image",
                data=f,
                file_name="creative.png",
                mime="image/png",
                use_container_width=True,
            )
            
    else:
        st.warning("Image generation failed.")
