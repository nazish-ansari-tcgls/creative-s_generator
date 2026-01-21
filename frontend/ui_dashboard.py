
import streamlit as st
from frontend.utils.theme import THEME

def inject_dashboard_css():
    """Call AFTER boot_ui() on dashboard page (adds dashboard-only styles)."""
    st.markdown(
        f"""
<style>
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
  font-size: 18px;
  margin-bottom: 16px;
}}

.dash-arrow{{
  position:absolute;
  top: 22px;
  right: 22px;
  color: {THEME.ACCENT};
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

/* --- invisible overlay buttons to capture clicks (prevents white bar) --- */
/* --- REAL clickable button styled like pill (default themed) --- */
.overlay-btn .stButton>button{{
  width: 100% !important;
  height: 54px !important;
  border-radius: 999px !important;

  /* DEFAULT = THEME */
  background: rgba(255,255,255,0.06) !important;
  border: 1px solid rgba(255,255,255,0.12) !important;
  color: rgba(242,243,255,0.92) !important;
  box-shadow: none !important;
  font-weight: 850 !important;
}}

/* HOVER = lighter / more “white-ish” */
.overlay-btn .stButton>button:hover{{
  background: rgba(255,255,255,0.14) !important;
  border: 1px solid rgba(43,240,182,0.55) !important;
}}

/* ACTIVE press */
.overlay-btn .stButton>button:active{{
  transform: scale(0.99);
}}

/* remove extra spacing around buttons */
.overlay-btn div[data-testid="stVerticalBlock"]{{
  gap: 0rem !important;
}}

</style>
""",
        unsafe_allow_html=True,
    )

def render_dashboard_cards():
    st.markdown(
        """
<div class="dash-grid">

  <div class="dash-card">
    <div class="dash-arrow">↗</div>
    <div class="dash-icon">👥</div>
    <div class="dash-title">Project DNA</div>
    <div class="dash-desc">
      View all your customers in one place and maintain a strong relationship with them.
    </div>
  </div>

  <div class="dash-card outlined">
    <div class="dash-arrow">↗</div>
    <div class="dash-icon">📄</div>
    <div class="dash-title">Creative Ad Magic</div>
    <div class="dash-desc">
      View cost sheets, create custom payment plans for clients. Manage all your payments with ease
    </div>
  </div>

</div>
""",
        unsafe_allow_html=True,
    )
