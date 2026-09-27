import sys
from pathlib import Path

import streamlit as st


# ============================================================
# CONFIG
# ============================================================

st.set_page_config(
    page_title="Linux System Monitor",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PROJECT PATH
# ============================================================

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


# ============================================================
# BACKEND
# ============================================================

from src.system_info import get_system_info
from src.log_analyzer import analyze_log_file
from src.system_commands import get_system_commands


LOG_FILE = ROOT / "logs" / "system.log"


# ============================================================
# PALETTE
# ============================================================

# Streamlit exposes the active light/dark theme at runtime.
# We keep the same brand language in both modes, but darken the
# complete visual system when the user switches to Dark in Settings.
try:
    DARK_MODE = st.context.theme.type == "dark"
except Exception:
    DARK_MODE = False

if DARK_MODE:
    INK = "#E9E6DE"        # warm light text
    NAVY = "#344650"        # deep slate navigation
    HEADER = "#222E3E"      # deep navy header
    SLATE = "#3F514E"       # dark teal-slate cards
    SAGE = "#718C7D"        # muted sage accent
    APP_BG = "#252D31"      # dark neutral background
    CHART_BG = "#343234"    # dark warm chart surface
    SURFACE = "#30373A"     # dark soft panels
    WHITE = "#F7F4EE"
    RED = "#A15D56"
    AMBER = "#A98552"
    GREEN = "#678163"
else:
    INK = "#26344A"        # deep ink blue
    NAVY = "#526775"       # slate-blue navigation
    HEADER = "#2F3E52"     # deep navy header
    SLATE = "#5B706B"      # muted teal cards
    SAGE = "#95AA9A"       # soft sage accent
    APP_BG = "#E9E4DC"     # warm stone application background
    CHART_BG = "#F5F1EA"   # warm chart surface
    SURFACE = "#F8F6F0"    # soft neutral panels
    WHITE = "#FCFBF8"
    RED = "#B35F55"
    AMBER = "#B4874D"
    GREEN = "#6E8A6A"

# Backward-compatible names used throughout the existing dashboard.
FOREST = INK
TEAL = NAVY
PALE_SAGE = APP_BG
GRAY = APP_BG


# ============================================================
# DATA
# ============================================================

@st.cache_data(ttl=5)
def system_data():
    return get_system_info()


@st.cache_data(ttl=5)
def log_data():
    return analyze_log_file(str(LOG_FILE))


@st.cache_data(ttl=5)
def command_data():
    return get_system_commands()


info = system_data()
logs = log_data()
commands = command_data()


# ============================================================
# CSS
# ============================================================

st.html(
    f"""
    <style>
    :root {{
        --ink: {INK};
        --navy: {NAVY};
        --header: {HEADER};
        --slate: {SLATE};
        --sage: {SAGE};
        --app-bg: {APP_BG};
        --chart-bg: {CHART_BG};
        --surface: {SURFACE};
        --white: #FAFAF7;
        --red: {RED};
        --amber: {AMBER};
        --green: {GREEN};
        --shadow: 0 10px 28px rgba(47,52,86,0.10);
        --shadow-soft: 0 6px 18px rgba(47,52,86,0.08);
    }}

    .stApp {{
        background: {APP_BG} !important;
        color: {INK} !important;
        min-height: 100vh;
    }}

    [data-testid="stAppViewContainer"] {{
        background:
            linear-gradient(180deg, {APP_BG} 0%, #C2CCC2 50%, {APP_BG} 100%) !important;
    }}

    [data-testid="stMain"] {{ background: transparent !important; }}

    [data-testid="stMainBlockContainer"] {{
        max-width: 1440px !important;
        padding-top: 4.25rem !important;
        padding-bottom: 3rem !important;
    }}

    /* Real Streamlit top bar */
    header[data-testid="stHeader"] {{
        background: {INK} !important;
        border-bottom: 1px solid rgba(255,255,255,0.08) !important;
        box-shadow: 0 2px 14px rgba(47,52,86,0.16);
    }}

    header[data-testid="stHeader"]::before {{
        content: "Linux System Monitor";
        position: absolute;
        left: 20px;
        top: 50%;
        transform: translateY(-50%);
        color: #FAFAF7;
        font-size: 14px;
        font-weight: 800;
        letter-spacing: 0.05px;
        pointer-events: none;
        white-space: nowrap;
    }}

    header[data-testid="stHeader"] button,
    header[data-testid="stHeader"] svg {{
        color: #FAFAF7 !important;
        fill: #FAFAF7 !important;
    }}

    /* Sidebar */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {NAVY} 0%, #566970 58%, {SLATE} 100%) !important;
        border-right: 1px solid rgba(255,255,255,0.09);
    }}

    [data-testid="stSidebar"] > div:first-child {{
        background: transparent !important;
    }}

    [data-testid="stSidebar"] [data-testid="stSidebarContent"] {{
        padding: 1.3rem 1rem 1rem 1rem !important;
    }}

    [data-testid="stSidebar"] .lm-sidebar-brand,
    [data-testid="stSidebar"] .lm-sidebar-brand * {{
        color: #FAFAF7 !important;
    }}

    [data-testid="stSidebar"] [data-testid="stRadio"] > label {{
        color: rgba(250,250,247,0.72) !important;
        font-weight: 750 !important;
        font-size: 11px !important;
    }}

    [data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] {{
        gap: 4px !important;
    }}

    [data-testid="stSidebar"] [data-testid="stRadio"] div[role="radio"] {{
        color: #FAFAF7 !important;
        background: transparent !important;
        border-radius: 10px !important;
        padding: 8px 10px !important;
        min-height: 34px !important;
    }}

    [data-testid="stSidebar"] [data-testid="stRadio"] div[role="radio"]:hover {{
        background: rgba(233,228,220,0.12) !important;
    }}

    [data-testid="stSidebar"] [data-testid="stRadio"] div[role="radio"][aria-checked="true"] {{
        background: rgba(233,228,220,0.15) !important;
        box-shadow: inset 3px 0 0 {SAGE};
    }}

    [data-testid="stSidebar"] [data-testid="stRadio"] div[role="radio"] *,
    [data-testid="stSidebar"] [data-testid="stRadio"] div[role="radio"] p {{
        color: #FAFAF7 !important;
    }}

    [data-testid="stSidebar"] [data-testid="stRadio"] div[role="radio"] svg {{
        color: {SAGE} !important;
        fill: {SAGE} !important;
    }}

    [data-testid="stSidebar"] hr {{
        border-color: rgba(233,228,220,0.15) !important;
    }}

    [data-testid="stSidebar"] [data-testid="stCaptionContainer"] {{
        color: rgba(250,250,247,0.64) !important;
    }}

    /* ========================================================
       BUTTONS / REFRESH BUTTON
       ======================================================== */

    .stButton > button,
    [data-testid="stSidebar"] .stButton > button,
    [data-testid="stSidebar"] button[data-testid^="stBaseButton"] {{
        background: {HEADER} !important;
        color: #F5F2EA !important;
        border: 1px solid rgba(255,255,255,0.10) !important;
        border-radius: 10px !important;
        font-weight: 750 !important;
        box-shadow: 0 5px 14px rgba(47,52,86,0.10) !important;
        outline: none !important;
        outline-width: 0 !important;
        outline-style: none !important;
        outline-color: transparent !important;
        -webkit-tap-highlight-color: transparent !important;
        appearance: none !important;
        -webkit-appearance: none !important;
    }}

    .stButton > button *,
    [data-testid="stSidebar"] .stButton > button *,
    [data-testid="stSidebar"] button[data-testid^="stBaseButton"] * {{
        color: #F5F2EA !important;
        outline: none !important;
        outline-width: 0 !important;
        box-shadow: none !important;
    }}

    .stButton > button:focus,
    .stButton > button:focus-visible,
    .stButton > button:active,
    [data-testid="stSidebar"] .stButton > button:focus,
    [data-testid="stSidebar"] .stButton > button:focus-visible,
    [data-testid="stSidebar"] .stButton > button:active,
    [data-testid="stSidebar"] button[data-testid^="stBaseButton"]:focus,
    [data-testid="stSidebar"] button[data-testid^="stBaseButton"]:focus-visible,
    [data-testid="stSidebar"] button[data-testid^="stBaseButton"]:active {{
        outline: none !important;
        outline-width: 0 !important;
        outline-style: none !important;
        outline-color: transparent !important;
        box-shadow: 0 5px 14px rgba(47,52,86,0.10) !important;
        border-color: rgba(255,255,255,0.10) !important;
    }}

    .stButton > button:hover,
    [data-testid="stSidebar"] .stButton > button:hover,
    [data-testid="stSidebar"] button[data-testid^="stBaseButton"]:hover {{
        background: {SLATE} !important;
        color: #F5F2EA !important;
    }}

    /* Remove any focus-ring pseudo-elements used by the button wrapper. */
    .stButton > button::before,
    .stButton > button::after,
    [data-testid="stSidebar"] .stButton::before,
    [data-testid="stSidebar"] .stButton::after,
    [data-testid="stSidebar"] .stButton > button::before,
    [data-testid="stSidebar"] .stButton > button::after {{
        content: none !important;
        display: none !important;
        box-shadow: none !important;
        outline: none !important;
    }}

    /* Hero header */
    .lm-brand {{
        position: relative;
        z-index: 1;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 20px;
        padding: 20px 24px;
        background: linear-gradient(115deg, {HEADER} 0%, {SLATE} 100%);
        border: 1px solid rgba(255,255,255,0.13);
        border-radius: 18px;
        margin-bottom: 28px;
        box-shadow: 0 12px 30px rgba(47,52,86,0.16);
    }}

    .lm-brand-left {{
        display: flex;
        align-items: center;
        gap: 14px;
        min-width: 0;
    }}

    .lm-logo {{
        width: 44px;
        height: 44px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        background: {CHART_BG};
        color: {INK};
        font-size: 21px;
        font-weight: 900;
        flex: 0 0 auto;
        box-shadow: 0 5px 14px rgba(47,52,86,0.16);
    }}

    .lm-title {{
        color: #FAFAF7 !important;
        font-size: 24px;
        line-height: 1.08;
        font-weight: 850;
        letter-spacing: -0.55px;
    }}

    .lm-subtitle {{
        color: rgba(250,250,247,0.78) !important;
        font-size: 11px;
        margin-top: 5px;
    }}

    .lm-live {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        color: #FAFAF7 !important;
        font-size: 11px;
        font-weight: 800;
        background: rgba(233,228,220,0.13);
        border: 1px solid rgba(233,228,220,0.18);
        padding: 8px 12px;
        border-radius: 999px;
        white-space: nowrap;
    }}

    .lm-live-dot {{
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: {SAGE};
        box-shadow: 0 0 0 4px rgba(139,167,148,0.18);
    }}

    /* Headings */
    .lm-section-title {{
        font-size: 20px;
        line-height: 1.15;
        font-weight: 850;
        color: {INK} !important;
        margin-top: 22px;
        margin-bottom: 5px;
        letter-spacing: -0.25px;
    }}

    .lm-section-sub {{
        font-size: 11px;
        line-height: 1.5;
        color: {INK} !important;
        opacity: 0.66;
        margin-bottom: 15px;
    }}

    /* Dark metric cards */
    .lm-card {{
        min-height: 136px;
        padding: 20px;
        border-radius: 16px;
        background: linear-gradient(145deg, {SLATE} 0%, {HEADER} 100%) !important;
        border: 1px solid rgba(255,255,255,0.10);
        box-shadow: var(--shadow);
        position: relative;
        overflow: hidden;
        color: #FAFAF7 !important;
    }}

    .lm-card::after {{
        content: "";
        position: absolute;
        width: 120px;
        height: 120px;
        right: -48px;
        top: -50px;
        border-radius: 50%;
        background: rgba(233,228,220,0.08);
        pointer-events: none;
    }}

    .lm-card::before {{
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 4px;
        background: {SAGE};
        pointer-events: none;
    }}

    .lm-label {{
        font-size: 9px;
        text-transform: uppercase;
        letter-spacing: 1.25px;
        font-weight: 800;
        color: rgba(233,228,220,0.76) !important;
    }}

    .lm-number {{
        font-size: 29px;
        line-height: 1;
        font-weight: 850;
        letter-spacing: -1px;
        margin-top: 17px;
        color: #FAFAF7 !important;
    }}

    .lm-description {{
        font-size: 10px;
        line-height: 1.5;
        color: rgba(250,250,247,0.73) !important;
        margin-top: 7px;
        max-width: 92%;
    }}

    /* Light information panels */
    .lm-info {{
        padding: 16px 17px;
        margin-bottom: 10px;
        border-radius: 13px;
        background: rgba(244,241,235,0.64) !important;
        border: 1px solid rgba(47,52,86,0.10);
        box-shadow: var(--shadow-soft);
        color: {INK} !important;
        backdrop-filter: blur(4px);
    }}

    .lm-info-label {{
        font-size: 9px;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: {NAVY} !important;
        font-weight: 800;
    }}

    .lm-info-value {{
        margin-top: 5px;
        font-size: 14px;
        font-weight: 750;
        color: {INK} !important;
        word-break: break-word;
    }}

    /* Health */
    .lm-health {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 16px;
        padding: 14px 2px;
        border-bottom: 1px solid rgba(233,228,220,0.15);
    }}

    .lm-health:last-child {{ border-bottom: none; }}

    .lm-health-name {{
        font-size: 12px;
        font-weight: 700;
        color: #FAFAF7 !important;
    }}

    .lm-health-state {{
        font-size: 10px;
        font-weight: 800;
        white-space: nowrap;
    }}

    /* Custom progress: removes native blue */
    .lm-progress {{
        width: 100%;
        height: 8px;
        margin: 12px 0 6px 0;
        background: rgba(47,52,86,0.14);
        border-radius: 999px;
        overflow: hidden;
        border: 1px solid rgba(47,52,86,0.05);
    }}

    .lm-progress > div {{
        height: 100%;
        border-radius: inherit;
        background: linear-gradient(90deg, {SAGE} 0%, {HEADER} 100%);
        box-shadow: 0 0 10px rgba(139,167,148,0.16);
    }}

    /* Chart container: keep the rendered plot fully inside its card. */
    [data-testid="stVegaLiteChart"],
    [data-testid="stArrowVegaLiteChart"] {{
        width: 100% !important;
        max-width: 100% !important;
        min-width: 0 !important;
        box-sizing: border-box !important;
        overflow: hidden !important;
        background: {CHART_BG} !important;
        border: 1px solid rgba(38,52,74,0.12) !important;
        border-radius: 15px !important;
        padding: 0 !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
        box-shadow: var(--shadow-soft);
    }}

    [data-testid="stVegaLiteChart"] > div,
    [data-testid="stArrowVegaLiteChart"] > div {{
        width: 100% !important;
        max-width: 100% !important;
        min-width: 0 !important;
        box-sizing: border-box !important;
        overflow: hidden !important;
    }}

    [data-testid="stVegaLiteChart"] canvas,
    [data-testid="stVegaLiteChart"] svg,
    [data-testid="stArrowVegaLiteChart"] canvas,
    [data-testid="stArrowVegaLiteChart"] svg {{
        max-width: 100% !important;
        box-sizing: border-box !important;
    }}


    /* Native Streamlit surface fallback for dark mode. */
    [data-testid="stAppViewContainer"] > .main,
    [data-testid="stMain"] {{
        color-scheme: {"dark" if DARK_MODE else "light"};
    }}

    .stCaption,
    [data-testid="stCaptionContainer"] {{
        color: {INK} !important;
    }}

    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li {{
        color: {INK};
    }}

    [data-testid="stCodeBlock"] {{
        border: 1px solid rgba(47,52,86,0.13) !important;
        border-radius: 12px !important;
        box-shadow: var(--shadow-soft);
    }}

    [data-testid="stAlert"] {{ border-radius: 12px !important; }}

    hr {{ border-color: rgba(47,52,86,0.15) !important; }}

    .lm-footer {{
        text-align: center;
        margin-top: 46px;
        padding-top: 18px;
        border-top: 1px solid rgba(47,52,86,0.15);
        color: {INK} !important;
        font-size: 9px;
        opacity: 0.62;
    }}

    /* Final focus-ring override for Streamlit's current button DOM. */
    [data-testid="stSidebar"] .stButton,
    [data-testid="stSidebar"] .stButton > div,
    [data-testid="stSidebar"] .stButton > div > div,
    [data-testid="stSidebar"] .stButton > div > div > button {{
        outline: none !important;
        outline-width: 0 !important;
        outline-style: none !important;
        box-shadow: none !important;
    }}

    [data-testid="stSidebar"] .stButton > div > div > button:focus,
    [data-testid="stSidebar"] .stButton > div > div > button:focus-visible,
    [data-testid="stSidebar"] .stButton > div > div > button:active {{
        outline: none !important;
        outline-width: 0 !important;
        outline-style: none !important;
        outline-color: transparent !important;
        box-shadow: 0 5px 14px rgba(47,52,86,0.10) !important;
    }}

    </style>
    """
)

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.html(
        """
        <div class="lm-sidebar-brand" style="padding:10px 4px 15px 4px;">
            <div style="
                font-size:18px;
                font-weight:800;
                letter-spacing:-0.2px;
            ">
                ◈ Linux Monitor
            </div>

            <div style="
                font-size:10px;
                opacity:0.70;
                margin-top:5px;
            ">
                System diagnostics console
            </div>
        </div>
        """
    )

    st.divider()

    page = st.radio(
        "Dashboard",
        [
            "Overview",
            "System Information",
            "Log Analysis",
            "Linux Commands",
        ],
    )

    st.divider()

    if st.button(
        "↻  Refresh data",
        use_container_width=True,
    ):
        system_data.clear()
        log_data.clear()
        command_data.clear()
        st.rerun()

    st.caption("Backend refresh: 5 seconds")


# ============================================================
# TOP HEADER
# ============================================================

st.html(
    f"""
    <div class="lm-brand">

        <div class="lm-brand-left">

            <div class="lm-logo">
                ◈
            </div>

            <div>

                <div class="lm-title">
                    Linux System Monitor
                </div>

                <div class="lm-subtitle">
                    System resources · diagnostics · log intelligence
                </div>

            </div>

        </div>

        <div class="lm-live">
            <span class="lm-live-dot"></span>
            LIVE SYSTEM
        </div>

    </div>
    """
)


# ============================================================
# CALCULATIONS
# ============================================================

total_memory = float(info.get("total_memory", 0))
available_memory = float(info.get("memory_available", 0))

used_memory = max(
    total_memory - available_memory,
    0,
)

memory_percent = (
    used_memory / total_memory * 100
    if total_memory
    else 0
)

disk_usage = float(
    info.get("disk_usage", 0)
)

disk_used = float(
    info.get("used_disk", 0)
)

def progress_html(percent):
    percent = max(0.0, min(float(percent), 100.0))
    return f"""
        <div class="lm-progress" aria-label="{percent:.1f}%">
            <div style="width:{percent:.2f}%;"></div>
        </div>
    """


error_counts = {
    key: value
    for key, value in logs.items()
    if isinstance(value, (int, float))
}

total_errors = int(
    sum(error_counts.values())
)


# ============================================================
# OVERVIEW
# ============================================================

if page == "Overview":

    st.html(
        """
        <div class="lm-section-title">
            System overview
        </div>

        <div class="lm-section-sub">
            Current performance snapshot from your Linux backend.
        </div>
        """
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.html(
            f"""
            <div class="lm-card" style="--accent:{SAGE};">

                <div class="lm-label">
                    Memory used
                </div>

                <div class="lm-number">
                    {used_memory:.2f} GB
                </div>

                <div class="lm-description">
                    {memory_percent:.1f}% of available system memory
                </div>

            </div>
            """
        )

    with c2:

        st.html(
            f"""
            <div class="lm-card" style="--accent:{NAVY};">

                <div class="lm-label">
                    Memory available
                </div>

                <div class="lm-number">
                    {available_memory:.2f} GB
                </div>

                <div class="lm-description">
                    Currently available memory
                </div>

            </div>
            """
        )

    with c3:

        st.html(
            f"""
            <div class="lm-card" style="--accent:{HEADER};">

                <div class="lm-label">
                    Disk usage
                </div>

                <div class="lm-number">
                    {disk_usage:.1f}%
                </div>

                <div class="lm-description">
                    {disk_used:.2f} GB currently used
                </div>

            </div>
            """
        )

    with c4:

        error_color = RED if total_errors else SAGE

        st.html(
            f"""
            <div class="lm-card" style="--accent:{error_color};">

                <div class="lm-label">
                    Log errors
                </div>

                <div class="lm-number">
                    {total_errors}
                </div>

                <div class="lm-description">
                    Detected by log analyzer
                </div>

            </div>
            """
        )


    # --------------------------------------------------------
    # RESOURCE SECTION
    # --------------------------------------------------------

    left, right = st.columns([1.5, 1])

    with left:

        st.html(
            """
            <div class="lm-section-title">
                Resource utilization
            </div>

            <div class="lm-section-sub">
                Memory and storage consumption.
            </div>
            """
        )

        st.html(
            f"""
            <div class="lm-card" style="--accent:{SAGE};">

                <div class="lm-label">
                    Memory
                </div>

                <div class="lm-number">
                    {memory_percent:.1f}%
                </div>

            </div>
            """
        )

        st.html(progress_html(memory_percent))

        st.caption(
            f"{used_memory:.2f} GB used of "
            f"{total_memory:.2f} GB"
        )

        st.html(
            f"""
            <div class="lm-card"
                 style="--accent:{TEAL}; margin-top:14px;">

                <div class="lm-label">
                    Storage
                </div>

                <div class="lm-number">
                    {disk_usage:.1f}%
                </div>

            </div>
            """
        )

        st.html(progress_html(disk_usage))

        st.caption(
            f"{disk_used:.2f} GB used"
        )


    with right:

        st.html(
            """
            <div class="lm-section-title">
                System health
            </div>

            <div class="lm-section-sub">
                Status derived from current monitoring data.
            </div>
            """
        )

        health_color = (
            SAGE
            if total_errors == 0
            else AMBER
            if total_errors <= 5
            else RED
        )

        health_text = (
            "Healthy"
            if total_errors == 0
            else "Attention"
            if total_errors <= 5
            else "Critical"
        )

        st.html(
            f"""
            <div class="lm-card" style="--accent:{health_color};">

                <div class="lm-label">
                    Overall status
                </div>

                <div class="lm-number"
                     style="font-size:25px;">
                    {health_text}
                </div>

                <div class="lm-description">
                    {total_errors} log errors detected
                </div>

                <div class="lm-health">

                    <span class="lm-health-name">
                        Memory
                    </span>

                    <span class="lm-health-state"
                          style="color:{GREEN};">
                        ● Normal
                    </span>

                </div>

                <div class="lm-health">

                    <span class="lm-health-name">
                        Storage
                    </span>

                    <span class="lm-health-state"
                          style="color:{GREEN};">
                        ● Normal
                    </span>

                </div>

                <div class="lm-health">

                    <span class="lm-health-name">
                        Log analysis
                    </span>

                    <span class="lm-health-state"
                          style="color:{health_color};">
                        ● {health_text}
                    </span>

                </div>

            </div>
            """
        )


    # --------------------------------------------------------
    # ERROR CHART
    # --------------------------------------------------------

    st.html(
        """
        <div class="lm-section-title">
            Error distribution
        </div>

        <div class="lm-section-sub">
            Classification produced by the project's log analyzer.
        </div>
        """
    )

    if total_errors > 0:

        st.bar_chart(
            error_counts,
            width="stretch",
            height=280,
            color=HEADER,
        )

    else:

        st.success(
            "No errors detected in the current log."
        )


# ============================================================
# SYSTEM INFORMATION
# ============================================================

elif page == "System Information":

    st.html(
        """
        <div class="lm-section-title">
            System information
        </div>

        <div class="lm-section-sub">
            Hardware and operating-system information collected
            from the Linux environment.
        </div>
        """
    )

    left, right = st.columns(2)

    with left:

        st.html(
            f"""
            <div class="lm-info">

                <div class="lm-info-label">
                    Hostname
                </div>

                <div class="lm-info-value">
                    {info.get("hostname", "Unknown")}
                </div>

            </div>

            <div class="lm-info">

                <div class="lm-info-label">
                    Operating system
                </div>

                <div class="lm-info-value">
                    {info.get("os_name", "Unknown")}
                </div>

            </div>

            <div class="lm-info">

                <div class="lm-info-label">
                    OS version
                </div>

                <div class="lm-info-value">
                    {info.get("os_version", "Unknown")}
                </div>

            </div>

            <div class="lm-info">

                <div class="lm-info-label">
                    CPU model
                </div>

                <div class="lm-info-value">
                    {info.get("cpu_model", "Unknown")}
                </div>

            </div>
            """
        )

    with right:

        st.html(
            f"""
            <div class="lm-info">

                <div class="lm-info-label">
                    Total memory
                </div>

                <div class="lm-info-value">
                    {total_memory:.2f} GB
                </div>

            </div>

            <div class="lm-info">

                <div class="lm-info-label">
                    Available memory
                </div>

                <div class="lm-info-value">
                    {available_memory:.2f} GB
                </div>

            </div>

            <div class="lm-info">

                <div class="lm-info-label">
                    Total disk
                </div>

                <div class="lm-info-value">
                    {float(info.get("total_disk", 0)):.2f} GB
                </div>

            </div>

            <div class="lm-info">

                <div class="lm-info-label">
                    Used disk
                </div>

                <div class="lm-info-value">
                    {disk_used:.2f} GB
                </div>

            </div>
            """
        )

    st.html(
        """
        <div class="lm-section-title">
            Storage utilization
        </div>
        """
    )

    st.html(progress_html(disk_usage))

    st.caption(
        f"{disk_usage:.2f}% of disk capacity is currently used."
    )


# ============================================================
# LOG ANALYSIS
# ============================================================

elif page == "Log Analysis":

    st.html(
        """
        <div class="lm-section-title">
            Log analysis
        </div>

        <div class="lm-section-sub">
            Real-time classification from logs/system.log.
        </div>
        """
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.html(
            f"""
            <div class="lm-card" style="--accent:{RED};">

                <div class="lm-label">
                    Total errors
                </div>

                <div class="lm-number">
                    {total_errors}
                </div>

                <div class="lm-description">
                    All detected categories
                </div>

            </div>
            """
        )

    with c2:

        st.html(
            f"""
            <div class="lm-card" style="--accent:{NAVY};">

                <div class="lm-label">
                    Categories
                </div>

                <div class="lm-number">
                    {len(error_counts)}
                </div>

                <div class="lm-description">
                    Analyzer classifications
                </div>

            </div>
            """
        )

    with c3:

        color = SAGE if total_errors == 0 else AMBER

        text = "Clean" if total_errors == 0 else "Review"

        st.html(
            f"""
            <div class="lm-card" style="--accent:{color};">

                <div class="lm-label">
                    Log status
                </div>

                <div class="lm-number"
                     style="font-size:25px;">
                    {text}
                </div>

                <div class="lm-description">
                    Current analysis
                </div>

            </div>
            """
        )

    st.html(
        """
        <div class="lm-section-title">
            Error breakdown
        </div>
        """
    )

    st.bar_chart(
        error_counts,
        width="stretch",
        height=320,
        color=HEADER,
    )

    for name, count in error_counts.items():

        st.write(
            f"**{name}** — {int(count)}"
        )


# ============================================================
# LINUX COMMANDS
# ============================================================

elif page == "Linux Commands":

    st.html(
        """
        <div class="lm-section-title">
            Linux command information
        </div>

        <div class="lm-section-sub">
            Output collected through the project's subprocess
            command layer.
        </div>
        """
    )

    if isinstance(commands, dict):

        for key, value in commands.items():

            st.html(
                f"""
                <div class="lm-info">

                    <div class="lm-info-label">
                        {str(key).replace("_", " ").title()}
                    </div>

                    <div class="lm-info-value">
                        {str(value).replace("<", "&lt;")
                                      .replace(">", "&gt;")}
                    </div>

                </div>
                """
            )

    else:

        st.code(
            str(commands),
            language="text",
        )


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="lm-footer">
        Linux System Monitor
        · Python
        · Linux subprocess
        · Bash
        · pytest
        · Streamlit
    </div>
    """
)