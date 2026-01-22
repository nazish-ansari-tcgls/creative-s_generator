# frontend/ui_creative_details.py
import streamlit as st

ACCENT = "#2BF0B6"
BORDER = "rgba(255,255,255,0.10)"
TEXT_MUTED = "rgba(242,243,255,0.72)"

def inject_creative_details_css():
    st.markdown(
        f"""
<style>
/* ===== Creative Details shell ===== */
.cg-card {{
  background: rgba(0,0,0,0.18);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 22px;
  padding: 18px;
}}
.cg-title {{
  font-weight: 900;
  font-size: 1.15rem;
  margin-bottom: 12px;
}}
.cg-sub {{
  color: {TEXT_MUTED};
  font-size: 0.92rem;
  margin-top: -6px;
  margin-bottom: 10px;
}}

/* ===== Category pills ===== */
/* Category pills */
/* ===== Fixed-size category pills ===== */

.pill-wrap{{
  position: relative;
  width: 100%;
}}

/* pill body */
.pill{{
  height: 44px;                 /* FIXED HEIGHT */
  min-width: 200px;             /* FIXED WIDTH */
  max-width: 160px;

  display: flex;
  align-items: center;
  justify-content: center;

  padding: 0 10px;
  border-radius: 14px;
  border: 1px solid rgba(255,255,255,0.16);
  background: rgba(255,255,255,0.06);

  font-weight: 800;
  font-size: 0.82rem;
  line-height: 1.1;
  text-align: center;

  color: rgba(242,243,255,0.85);

  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}}

/* active state */
.pill.active{{
  background: rgba(43,240,182,0.22);
  border: 1px solid rgba(43,240,182,0.70);
  color: #2BF0B6;
}}

/* invisible click overlay */
.pill-btn{{
  position: relative;
  margin-top: -44px;            /* MUST MATCH HEIGHT */
  height: 44px;
}}

.pill-btn .stButton>button{{
  width: 100% !important;
  height: 44px !important;
  background: transparent !important;
  border: 0 !important;
  color: transparent !important;
  box-shadow: none !important;
  padding: 0 !important;
}}



/* ===== Format cards ===== */
/* ===== Format cards (exactly like screenshot) ===== */
.format-grid {{
  display:grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  margin-top: 10px;
}}

.format-wrap {{
  position: relative;
}}

.format-card {{
  border-radius: 18px;
  border: 1px solid rgba(255,255,255,0.12);
  background: rgba(255,255,255,0.05);
  padding: 14px;
  min-height: 110px;
}}

.format-card.selected {{
  border: 1px solid rgba(43,240,182,0.75);
  background: rgba(43,240,182,0.08);
}}

.format-head {{
  display:flex; align-items:center; justify-content:space-between;
  margin-bottom: 10px;
}}

.format-name {{
  font-weight: 900;
  font-size: 0.98rem;
}}

.format-ratio {{
  font-size: 0.78rem;
  padding: 5px 10px;
  border-radius: 999px;
  background: rgba(0,0,0,0.18);
  border: 1px solid rgba(255,255,255,0.10);
}}

.tag-row {{
  display:flex; flex-wrap:wrap; gap: 8px;
}}

.tag {{
  font-size: 0.74rem;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(0,0,0,0.18);
  border: 1px solid rgba(255,255,255,0.10);
  color: rgba(242,243,255,0.85);
}}

/* Invisible click button overlay (so card is clickable) */
.format-btn {{
  position:absolute;
  inset: 0;
  z-index: 5;
}}
.format-btn .stButton>button {{
  width: 100% !important;
  height: 100% !important;
  background: rgba(0,0,0,0) !important;
  border: 0 !important;
  color: rgba(0,0,0,0) !important;
  box-shadow: none !important;
  padding: 0 !important;
}}
.format-btn .stButton>button:hover {{
  background: rgba(0,0,0,0) !important;
}}

/* ===== Inputs ===== */
label {{
  font-weight: 700 !important;
}}
.smallhint {{
  color: {TEXT_MUTED};
  font-size: 0.82rem;
  margin-top: -6px;
  margin-bottom: 8px;
}}

/* Streamlit inputs polish */
div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea,
div[data-baseweb="select"] > div {{
  background: rgba(0,0,0,0.18) !important;
  border: 1px solid rgba(255,255,255,0.12) !important;
  color: rgba(242,243,255,0.92) !important;
  border-radius: 14px !important;
}}
div[data-baseweb="textarea"] textarea {{
  min-height: 90px;
}}

/* ===== Background uploader tabs ===== */
.bg-tabs {{
  display:flex; gap: 10px;
  margin-bottom: 10px;
}}
.bg-tab {{
  flex: 1;
  text-align:center;
  padding: 12px 14px;
  border-radius: 14px;
  border: 1px solid rgba(255,255,255,0.14);
  background: rgba(255,255,255,0.06);
  font-weight: 800;
}}
.bg-tab.active {{
  background: rgba(43,240,182,0.18);
  border: 1px solid rgba(43,240,182,0.55);
  color: {ACCENT};
}}

/* ===== Bottom buttons ===== */
.bottom-row {{
  display:flex;
  gap: 14px;
  margin-top: 14px;
}}
.btn-ghost .stButton>button {{
  width: 100% !important;
  background: rgba(0,0,0,0.18) !important;
  border: 1px solid rgba(43,240,182,0.45) !important;
  color: {ACCENT} !important;
}}
.btn-primary .stButton>button {{
  width: 100% !important;
  background: linear-gradient(90deg, rgba(43,240,182,0.30), rgba(122,90,255,0.55), rgba(255,120,220,0.55)) !important;
  border: 1px solid rgba(255,255,255,0.10) !important;
  color: rgba(242,243,255,0.95) !important;
}}
.btn-primary .stButton>button:hover {{
  border: 1px solid rgba(43,240,182,0.55) !important;
}}
</style>
""",
        unsafe_allow_html=True,
    )


def render_category_pills(active: str):
    CATEGORIES = [
        "Awareness",
        "Location",
        "Testimonials",
        "Lead Gen",
        "Amenities & Lifestyle",
        "Festive & Seasonal",
        "Offers & Promotions",
        "Brand Corp. Comms",
        "Milestone Achieved",
        "Events & Experience",
        "Retargeting",
    ]

    PER_ROW = 6

    for i in range(0, len(CATEGORIES), PER_ROW):
        row = CATEGORIES[i:i + PER_ROW]
        cols = st.columns(PER_ROW, gap="small")

        for col_idx, col in enumerate(cols):
            if col_idx >= len(row):
                # empty column filler (keeps grid aligned)
                with col:
                    st.empty()
                continue

            cat = row[col_idx]
            is_active = (cat == active)
            pill_class = "pill active" if is_active else "pill"

            with col:
                # Visual pill
                st.markdown(
                    f"""
                    <div class="pill-wrap">
                      <div class="{pill_class}" title="{cat}">{cat}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                # Invisible clickable overlay
                st.markdown('<div class="pill-btn">', unsafe_allow_html=True)
                if st.button("select", key=f"cat_{cat}", use_container_width=True):
                    st.session_state["category"] = cat
                    st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)


def render_format_grid(selected: set[str]):
    # keys are internal ids
    formats = [
        ("square", "Square", "1:1", ["Instagram Post", "LinkedIn", "X (Twitter)", "Facebook"]),
        ("portrait", "Portrait", "4:5", ["Instagram Post", "LinkedIn", "X (Twitter)", "Facebook"]),
        ("landscape", "Landscape", "16:9", ["Instagram Post", "LinkedIn", "X (Twitter)", "YouTube"]),
        ("story", "Story, Reel, Shorts", "9:16", ["Instagram Post", "LinkedIn", "Facebook"]),
    ]
    cards_html = []
    for key, name, ratio, tags in formats:
        cls = "format-card selected" if key in selected else "format-card"
        tag_html = "".join([f'<span class="tag">{t}</span>' for t in tags])
        print(tag_html)
        
        cards_html.append(
            f"""
            <div class="{cls}">
              <div class="format-head">
                <div class="format-name">{name}</div>
                <div class="format-ratio">{ratio}</div>
              </div>
              <div class="tag-row">{tag_html}</div>
            </div>
            """
        )
    st.markdown(f'<div class="format-grid">{"".join(cards_html)}</div>', unsafe_allow_html=True)


def toggle_format(key: str):
    fmts = st.session_state.get("creative", {}).get("formats", set())
    if key in fmts:
        fmts.remove(key)
    else:
        fmts.add(key)
    st.session_state["creative"]["formats"] = fmts


def render_format_grid_clickable(selected: set[str]):
    formats = [
        ("square", "Square", "1:1", ["Instagram Post", "LinkedIn", "X (Twitter)", "Facebook"]),
        ("portrait", "Portrait", "4:5", ["Instagram Post", "LinkedIn", "X (Twitter)", "Facebook"]),
        ("landscape", "Landscape", "16:9", ["Instagram Post", "LinkedIn", "X (Twitter)", "YouTube"]),
        ("story", "Story, Reel, Shorts", "9:16", ["Instagram Post", "LinkedIn", "Facebook"]),
    ]

    # Render as 4 streamlit columns so each card can have a real button overlay
    cols = st.columns(4, gap="large")

    for i, (k, name, ratio, tags) in enumerate(formats):
        with cols[i]:
            is_sel = k in selected
            card_cls = "format-card selected" if is_sel else "format-card"
            tag_html = "".join([f'<span class="tag">{t}</span>' for t in tags])

            st.markdown(
                f"""
                <div class="format-wrap">
                  <div class="{card_cls}">
                    <div class="format-head">
                      <div class="format-name">{name}</div>
                      <div class="format-ratio">{ratio}</div>
                    </div>
                    <div class="tag-row">{tag_html}</div>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )


            st.markdown('<div class="format-btn">', unsafe_allow_html=True)
            if st.button("Select", key=f"toggle_fmt_{k}", use_container_width=True):
                toggle_format(k)
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)





