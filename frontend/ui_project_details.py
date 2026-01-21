import streamlit as st
from typing import Dict, Any


def inject_project_details_css():
    st.markdown(
        """
<style>
/* ===== Left Rail Nav (like screenshot) ===== */
.left-rail{
  position: fixed;
  top: 0;
  left: 0;
  width: 92px;
  height: 100vh;
  background: rgba(0,0,0,0.16);
  border-right: 1px solid rgba(255,255,255,0.06);
  padding-top: 88px;  /* below topbar */
  z-index: 999;
}
.rail-item{
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  gap: 6px;
  margin: 14px auto;
  width: 68px;
  height: 74px;
  border-radius: 18px;
  border: 1px solid rgba(255,255,255,0.08);
  background: rgba(0,0,0,0.10);
  color: rgba(242,243,255,0.85);
  font-size: 18px;
}
.rail-item span{
  font-size: 11px;
  opacity: 0.80;
  margin-top: -2px;
}
.rail-item.active{
  border: 1px solid rgba(43,240,182,0.55);
  background: rgba(43,240,182,0.10);
}
.rail-divider{
  width: 46px;
  height: 1px;
  background: rgba(255,255,255,0.10);
  margin: 18px auto;
  border-radius: 999px;
}

/* Shift app content right because rail is fixed */
.block-container{
  padding-left: 132px !important;
}

/* ===== Panels / Cards ===== */
.pd-shell{
  background: rgba(0,0,0,0.12);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 26px;
  padding: 18px;
  margin-top: 8px;
}

.pd-title{
  font-size: 15px;
  font-weight: 800;
  opacity: 0.95;
  margin: 2px 0 14px 4px;
}

.pd-grid{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
}

.pd-card{
  background: rgba(0,0,0,0.18);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 22px;
  padding: 18px;
  position: relative;
}

.pd-label{
  color: #2BF0B6;
  font-weight: 900;
  font-size: 18px;
  margin-bottom: 12px;
}

.pd-value-big{
  font-size: 22px;
  font-weight: 900;
  margin-bottom: 0px;
}
.pd-value-med{
  font-size: 16px;
  font-weight: 700;
  opacity: 0.92;
}

.pd-left-stack{
  display:flex;
  flex-direction:column;
  gap: 16px;
}

.pd-mini-row{
  display:grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
}

.pd-mini{
  background: rgba(0,0,0,0.18);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 22px;
  padding: 16px 16px 14px 16px;
}

.pd-address{
  background: rgba(0,0,0,0.18);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 22px;
  padding: 18px;
}

.pd-address-line{
  display:flex;
  align-items:center;
  gap: 14px;
  margin-top: 10px;
}

.pd-pin{
  width: 44px;
  height: 44px;
  border-radius: 14px;
  display:flex;
  align-items:center;
  justify-content:center;
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.10);
  font-size: 18px;
}

.hr{
  height: 1px;
  background: rgba(255,255,255,0.10);
  border-radius: 999px;
  margin: 18px 0;
}

.pd-sub{
  font-size: 14px;
  opacity: 0.75;
  margin-bottom: 6px;
}
.pd-subval{
  font-size: 16px;
  font-weight: 800;
  opacity: 0.92;
}

.pd-social{
  display:flex;
  gap: 12px;
  margin-top: 10px;
}

.pd-social a{
  width: 44px;
  height: 44px;
  border-radius: 14px;
  display:flex;
  align-items:center;
  justify-content:center;
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.10);
  color: rgba(242,243,255,0.90);
  font-weight: 900;
}

.pd-brief-head{
  display:flex;
  align-items:center;
  justify-content:space-between;
  margin-bottom: 8px;
}
.pd-brief-text{
  opacity: 0.78;
  line-height: 1.65rem;
  font-size: 15px;
  padding-right: 4px;
}

.pencil-btn .stButton>button{
  width: 42px !important;
  height: 42px !important;
  border-radius: 14px !important;
  background: rgba(0,0,0,0.0) !important;
  border: 1px solid rgba(43,240,182,0.45) !important;
  color: rgba(43,240,182,0.95) !important;
  box-shadow: none !important;
  font-weight: 900 !important;
}
.pencil-btn .stButton>button:hover{
  background: rgba(43,240,182,0.08) !important;
}

/* ===== Brand section ===== */
.brand-shell{
  background: rgba(0,0,0,0.12);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 26px;
  padding: 18px;
  margin-top: 14px;
}

.brand-grid{
  display:grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
}

.brand-card{
  background: rgba(0,0,0,0.18);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 22px;
  padding: 18px;
  position: relative;
  min-height: 140px;
}

.brand-head{
  display:flex;
  align-items:center;
  justify-content:space-between;
  margin-bottom: 14px;
}
.brand-head .title{
  color: #2BF0B6;
  font-weight: 900;
  font-size: 16px;
}

.brand-edit{
  width: 38px; height: 38px;
  border-radius: 14px;
  display:flex; align-items:center; justify-content:center;
  border: 1px solid rgba(43,240,182,0.35);
  color: rgba(43,240,182,0.90);
  opacity: 0.85;
}

.logo-box{
  display:flex;
  align-items:center;
  justify-content:center;
  height: 50px;
  border-radius: 18px;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.06);
}

.font-grid{
  display:grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

.font-tile{
  border-radius: 18px;
  background: rgba(0,0,0,0.14);
  border: 1px solid rgba(255,255,255,0.08);
  padding: 14px;
}

.font-tile .small{
  font-size: 12px;
  opacity: 0.75;
  margin-bottom: 6px;
}
.font-tile .big{
  font-size: 34px;
  font-weight: 950;
  line-height: 1;
}
.font-tile .name{
  margin-top: 6px;
  opacity: 0.88;
  font-weight: 800;
}

.chips{
  display:flex;
  flex-wrap: wrap;
  gap: 10px;
}
.chip{
  padding: 8px 12px;
  border-radius: 999px;
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.10);
  opacity: 0.92;
  font-size: 13px;
  font-weight: 700;
}

.color-row{
  display:grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}
.swatches{
  display:flex;
  gap: 10px;
  align-items:center;
  flex-wrap: wrap;
}
.swatch{
  width: 32px;
  height: 32px;
  border-radius: 10px;
  border: 1px solid rgba(255,255,255,0.18);
}

/* Bottom action buttons (Cancel / Save & Next) */
.bottom-actions{
  display:flex;
  align-items:center;
  justify-content:flex-end;
  gap: 14px;
  margin-top: 16px;
}

.btn-outline .stButton>button{
  height: 52px !important;
  border-radius: 999px !important;
  background: rgba(0,0,0,0.00) !important;
  border: 1px solid rgba(43,240,182,0.55) !important;
  color: rgba(43,240,182,0.95) !important;
  box-shadow: none !important;
}
.btn-solid .stButton>button{
  height: 52px !important;
  border-radius: 999px !important;
  background: #2BF0B6 !important;
  border: 1px solid rgba(0,0,0,0.0) !important;
  color: #1D1A3A !important;
  box-shadow: none !important;
  font-weight: 950 !important;
}
</style>
""",
        unsafe_allow_html=True,
    )


def _safe_get(d: Dict[str, Any], path: str, default=""):
    cur = d
    for key in path.split("."):
        if not isinstance(cur, dict) or key not in cur:
            return default
        cur = cur[key]
    return cur


def render_project_details(project: Dict[str, Any]):
    rera = project.get("rera_number", "")
    tagline = project.get("tagline", "")
    address = project.get("address", "")
    phone = project.get("phone", "")
    ig = _safe_get(project, "social.instagram", "")
    li = _safe_get(project, "social.linkedin", "")
    brief = project.get("project_brief", "")
    st.markdown(
        f"""
        <div class="pd-mini">
        <div class="pd-label">RERA Number</div>
        <div class="pd-value-big">{rera}</div>
        </div>
        <div class="pd-mini">
        <div class="pd-label">Tagline</div>
        <div class="pd-value-big" style="font-size:18px; font-weight:900; opacity:0.92;">{tagline}</div>
        </div>

        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="pd-address">
        <div class="pd-label">Address</div>
        <div class="pd-address-line">
            <div class="pd-pin">📍</div>
            <div class="pd-value-med">{address}</div>
        </div>

        <div class="hr"></div>

        <div class="pd-sub">Phone Number</div>
        <div class="pd-subval">{phone}</div>

        <div class="hr"></div>

        <div class="pd-sub">Social Media Links</div>
        <div class="pd-social">
            <a href="{ig}" target="_blank" title="Instagram">⌁</a>
            <a href="{li}" target="_blank" title="LinkedIn">in</a>
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="pd-mini">
            <div class="pd-label">Project Brief</div>
            <div class="pd-value-big" style="font-size:18px; font-weight:900; opacity:0.92;">{brief}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)  # end pd-grid
    st.markdown("</div>", unsafe_allow_html=True)  # end pd-shell


def render_brand_details(project: Dict[str, Any]):
    brand = project.get("brand", {})
    logo_path = brand.get("logo_path", "")
    fonts = brand.get("fonts", {})
    primary_font = fonts.get("primary", "Primary")
    secondary_font = fonts.get("secondary", "Secondary")
    values = brand.get("values", [])
    aesthetic = brand.get("aesthetic", [])
    colors = brand.get("colors", {})
    primary_colors = colors.get("primary", [])
    secondary_colors = colors.get("secondary", [])

    st.markdown(
    f"""
        <div class="brand-card">
            <div class="brand-head">
                <div class="title">Logo</div>
                <img src="{logo_path}" class="brand-logo" />
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Brand Font card
    st.markdown(
        """
        <div class="brand-card">
        <div class="brand-head">
            <div class="title">Brand Font</div>
            
        </div>
        <div class="font-grid">
            <div class="font-tile">
            <div class="small">Primary</div>
            <div class="big">Ag</div>
            <div class="name">""" + str(primary_font) + """</div>
            </div>
            <div class="font-tile">
            <div class="small">Secondary</div>
            <div class="big">Ag</div>
            <div class="name">""" + str(secondary_font) + """</div>
            </div>
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Brand Values
    chips_html = "".join([f'<div class="chip">{v}</div>' for v in values])
    st.markdown(
        f"""
        <div class="brand-card">
        <div class="brand-head">
            <div class="title">Brand Values</div>
            
        </div>
        <div class="chips">{chips_html}</div>
        </div>
        """,
                unsafe_allow_html=True,
    )

    # Colors
    sw_primary = "".join([f'<div class="swatch" style="background:{c};"></div>' for c in primary_colors])
    sw_secondary = "".join([f'<div class="swatch" style="background:{c};"></div>' for c in secondary_colors])

    st.markdown(
        f"""
<div class="brand-card">
  <div class="brand-head">
    <div class="title">Project Brand Colors</div>
    
  </div>

  <div class="color-row">
    <div>
      <div class="pd-sub" style="margin-bottom:10px;">Primary</div>
      <div class="swatches">{sw_primary}</div>
    </div>
    <div>
      <div class="pd-sub" style="margin-bottom:10px;">Secondary</div>
      <div class="swatches">{sw_secondary}</div>
    </div>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

    # Aesthetic
    aest_html = "".join([f'<div class="chip">{a}</div>' for a in aesthetic])
    st.markdown(
        f"""
<div class="brand-card">
  <div class="brand-head">
    <div class="title">Brand Aesthetic</div>
    
  </div>
  <div class="chips">{aest_html}</div>
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)  # end brand-grid
    st.markdown("</div>", unsafe_allow_html=True)  # end brand-shell



    
