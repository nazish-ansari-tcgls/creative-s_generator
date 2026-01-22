import streamlit as st

# --- Theme tokens (easy to tweak later) ---
BG = "#4A4472"             # page background
SURFACE = "#3C376A"        # large section surface
CARD = "#343064"           # cards
CARD_2 = "#2D2A5A"         # deeper cards
BORDER = "rgba(255,255,255,0.10)"
TEXT = "#F2F3FF"
MUTED = "rgba(242,243,255,0.70)"
ACCENT = "#2BF0B6"

def boot_ui(hide_streamlit_sidebar: bool = True):
    """Call this at top of EVERY page (after st.set_page_config)."""
    st.markdown(
        f"""
<style>
/* ---- Hide Streamlit chrome ---- */
header[data-testid="stHeader"] {{ display:none; }}
div[data-testid="stToolbar"] {{ display:none; }}
#MainMenu {{ visibility:hidden; }}
footer {{ visibility:hidden; }}

/* optional: hide sidebar (page list) */
{"section[data-testid='stSidebar']{display:none;}" if hide_streamlit_sidebar else ""}

/* ---- App canvas ---- */
[data-testid="stAppViewContainer"] {{ background: {BG}; }}
.stApp {{ background: {BG}; }}
.block-container {{
  max-width: 1400px;
  padding-top: 10px !important;
  padding-left: 26px !important;
  padding-right: 26px !important;
}}

/* ---- Global text ---- */
html, body, p, div, span, label {{ color: {TEXT}; }}
a {{ text-decoration: none !important; }}

/* ---- Topbar ---- */
.topbar {{
  display:flex;
  align-items:center;
  justify-content:space-between;
  margin-bottom: 6px;
}}
.brand {{
  font-size: 1.75rem;
  font-weight: 900;
  letter-spacing: -0.02em;
}}
.brand .dot {{ color: #FF4D6D; }}
.userpill {{
  display:flex; align-items:center; gap:12px;
  background: rgba(0,0,0,0.18);
  border: 1px solid {BORDER};
  border-radius: 16px;
  padding: 8px 16px;
}}
.avatar {{
  width: 30px; height: 30px; border-radius: 999px;
  background: rgba(255,255,255,0.10);
  border: 1px solid rgba(255,255,255,0.12);
  display:flex; align-items:center; justify-content:center;
}}
.user-name {{ font-weight: 600; line-height: 1.0; }}
.user-role {{ font-size: 0.85rem; opacity: 0.75; }}

/* ---- Breadcrumb row ---- */
.breadcrumb-row {{
  display:flex;
  align-items:center;
  justify-content:space-between;
  margin-bottom: 6px;
}}
.breadcrumb {{
  font-size: 1.00rem;         
  font-weight: 800;
  letter-spacing: -0.01em;
  opacity: 0.92;
}}
.project-pill {{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap: 12px;
  background: rgba(0,0,0,0.22);
  border: 1px solid {BORDER};
  border-radius: 16px;
  padding: 10px 14px;
  min-width: 260px;
}}
.proj-left {{ display:flex; align-items:center; gap: 12px; }}
.logo-badge {{
  width: 30px; height: 30px;
  border-radius: 10px;
  background: rgba(255,255,255,0.10);
  border: 1px solid rgba(255,255,255,0.12);
  display:flex; align-items:center; justify-content:center;
}}
.proj-name {{ font-weight: 500; font-size: 1.00rem; }}
.chev {{ opacity: 0.85; font-size: 1.1rem; }}

/* ---- Section header panel ---- */
.section {{
  background: rgba(0,0,0,0.18);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 20px;
  padding: 10px 12px;
  margin-bottom: 10px;
}}
.section-head {{
  display:flex; align-items:center; gap: 14px;
}}
.section-icon {{
  width: 50px; height: 50px;
  border-radius: 15px;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.10);
  display:flex; align-items:center; justify-content:center;
  font-size: 1.75rem;
}}
.section-title {{
  font-size: 1.45rem;
  font-weight: 950;
}}
.section:first-of-type {{
  margin-top: 2px;
}}


/* ---- Generic card ---- */
.card {{
  background: rgba(0,0,0,0.22);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 26px;
  padding: 22px;
}}
.card.outlined {{
  border: 2px solid rgba(255,255,255,0.22);
}}
.muted {{ color: {MUTED}; }}

/* ---- Streamlit widgets (we will refine later) ---- */
.stButton>button {{
  border-radius: 999px !important;
  height: 52px !important;
  font-weight: 850 !important;
}}

/* ===== Dashboard cards grid ===== */
.dash-grid{{
  display:grid;
  grid-template-columns: 1fr 1fr;
  gap: 22px;
  margin-top: 14px;
}}

.dash-card{{
  background: rgba(0,0,0,0.20);
  border: 1px solid rgba(255,255,255,0.10);
  border-radius: 26px;
  padding: 22px 22px 20px 22px;
  min-height: 210px;
  position: relative;
  overflow: hidden;
}}

.dash-card.outlined{{
  border: 2px solid rgba(255,255,255,0.22);
}}

.dash-icon{{
  width: 54px;
  height: 54px;
  border-radius: 18px;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.12);
  display:flex;
  align-items:center;
  justify-content:center;
  font-size: 18px; /* keeps emojis under control */
  margin-bottom: 16px;
}}

.dash-arrow{{
  position:absolute;
  top: 22px;
  right: 22px;
  color: #2BF0B6;
  font-size: 28px;
  font-weight: 900;
  line-height: 1;
}}

.dash-title{{
  font-size: 2.05rem;
  font-weight: 950;
  letter-spacing: -0.02em;
  margin: 0 0 10px 0;
}}

.dash-desc{{
  color: rgba(242,243,255,0.72);
  font-size: 1.02rem;
  line-height: 1.45rem;
  max-width: 520px;
}}

.stButton > button:disabled,
.stButton > button[disabled]{{
  background: rgba(255,255,255,0.06) !important;
  border: 1px solid rgba(255,255,255,0.12) !important;
  color: rgba(242,243,255,0.35) !important;
  opacity: 1 !important;            /* prevent greyed-out blur */
  box-shadow: none !important;
}}

/* keep hover from changing anything */
.stButton > button:disabled:hover{{
  background: rgba(255,255,255,0.06) !important;
  border: 1px solid rgba(255,255,255,0.12) !important;
}}


.dash-pill{{
  margin-top: 18px;
  height: 54px;
  width: 100%;
  border-radius: 999px;
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.12);
  display:flex;
  align-items:center;
  justify-content:center;
  font-weight: 800;
  color: rgba(242,243,255,0.90);
}}

.dash-pill:hover{{
  border: 1px solid rgba(43,240,182,0.55);
}}

/* --- invisible overlay buttons to capture clicks --- */
.overlay-btn .stButton>button{{
  width: 100% !important;
  height: 54px !important;
  border-radius: 999px !important;

  /* make it invisible but clickable */
  background: rgba(0,0,0,0) !important;
  border: 0px solid transparent !important;
  color: rgba(0,0,0,0) !important;
  box-shadow: none !important;
  padding: 0 !important;
}}

.overlay-btn .stButton>button:hover{{
  background: rgba(0,0,0,0) !important;
  border: 0px solid transparent !important;
}}

/* remove Streamlit default spacing around buttons */
.overlay-btn div[data-testid="stVerticalBlock"]{{
  gap: 0rem !important;
}}


</style>
""",
        unsafe_allow_html=True,
    )

def render_topbar(user_name="Nazish Ali", user_role="Admin"):
    st.markdown(
        f"""
<div class="topbar">
  <div class="brand">sir<span class="dot">r</span>us.ai</div>
  <div class="userpill">
    <div class="avatar">👤</div>
    <div>
      <div class="user-name">{user_name}</div>
      <div class="user-role">{user_role}</div>
    </div>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

def render_breadcrumb(title_left="Content Vault > Project Details", project_name="Hiranandani Gardens"):
    st.markdown(
        f"""
<div class="breadcrumb-row">
  <div class="breadcrumb">{title_left}</div>
  <div class="project-pill">
    <div class="proj-left">
      <div class="logo-badge">🏘️</div>
      <div class="proj-name">{project_name}</div>
    </div>
    <div class="chev">▾</div>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

def render_section_header(title: str, icon: str = "✨"):
    st.markdown(
        f"""
<div class="section">
  <div class="section-head">
    <div class="section-icon">{icon}</div>
    <div class="section-title">{title}</div>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )
