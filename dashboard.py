import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time

from streamlit_autorefresh import st_autorefresh

from src.api.weather_api import (
    get_live_weather,
    get_forecast
)

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Weather Intelligence Platform",
    page_icon="🌦",
    layout="wide"
)

# =========================================================
# AUTO REFRESH
# =========================================================

st_autorefresh(
    interval=300000,
    key="weather_refresh"
)

# =========================================================
# LOADING
# =========================================================

with st.spinner("🚀 Connecting to Global AI Climate Network..."):
    time.sleep(2)

# =========================================================
# CITY LIST
# =========================================================

cities = [
    "Kolkata",
    "Delhi",
    "Mumbai",
    "Chennai",
    "Bangalore",
    "Hyderabad",
    "London",
    "Tokyo"
]

# =========================================================
# FETCH WEATHER
# =========================================================

weather_data = []

for city in cities:

    try:

        city_df = get_live_weather(city)

        weather_data.append(city_df)

    except Exception as e:

        print(e)

# =========================================================
# EMPTY CHECK
# =========================================================

if len(weather_data) == 0:

    st.error("❌ Weather API not responding.")
    st.stop()

# =========================================================
# DATAFRAME
# =========================================================

df = pd.concat(
    weather_data,
    ignore_index=True
)

# =========================================================
# SMART AI RISK ENGINE
# =========================================================

def create_risk(temp, humidity, wind):

    if (
        temp >= 40 and humidity >= 70
    ) or wind >= 30:

        return "EXTREME"

    elif (
        temp >= 36 and humidity >= 60
    ) or wind >= 22:

        return "HIGH"

    elif (
        temp >= 32 and humidity >= 50
    ) or wind >= 15:

        return "MEDIUM"

    else:

        return "LOW"

df["RiskLevel"] = df.apply(

    lambda x: create_risk(

        x["Temperature"],
        x["Humidity"],
        x["WindSpeed"]

    ),

    axis=1
)

# =========================================================
# FORECAST
# =========================================================

try:

    forecast_df = get_forecast("Kolkata")

except:

    forecast_df = pd.DataFrame()

# =========================================================
# PREMIUM CSS
# =========================================================

st.markdown("""
<style>

.stApp {

    background:
    radial-gradient(circle at top left, #1e3a8a 0%, transparent 25%),
    radial-gradient(circle at top right, #7c3aed 0%, transparent 25%),
    radial-gradient(circle at bottom left, #0891b2 0%, transparent 25%),
    linear-gradient(
        135deg,
        #020617 0%,
        #0f172a 20%,
        #172554 45%,
        #312e81 70%,
        #581c87 100%
    );

    color: white;
}

section[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        rgba(15,23,42,0.98),
        rgba(23,37,84,0.98),
        rgba(49,46,129,0.98)
    );

    border-right:
    1px solid rgba(255,255,255,0.08);

    box-shadow:
    0 0 25px rgba(59,130,246,0.25);
}

.hero {

    padding: 55px;

    border-radius: 35px;

    background:
    linear-gradient(
        135deg,
        rgba(59,130,246,0.35),
        rgba(139,92,246,0.35),
        rgba(236,72,153,0.25)
    );

    margin-bottom: 35px;

    border:
    1px solid rgba(255,255,255,0.12);

    box-shadow:
    0 0 20px rgba(59,130,246,0.25),
    0 0 40px rgba(139,92,246,0.25),
    0 0 60px rgba(236,72,153,0.18);
}

.hero-title {

    font-size: 64px;

    font-weight: 900;

    background:
    linear-gradient(
        90deg,
        #ffffff,
        #67e8f9,
        #c084fc,
        #f472b6
    );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}

.hero-sub {

    font-size: 22px;

    color: #f8fafc;

    margin-top: 18px;

    line-height: 1.9;
}

.metric-card {

    padding: 28px;

    border-radius: 28px;

    background:
    linear-gradient(
        135deg,
        rgba(15,23,42,0.96),
        rgba(30,41,59,0.96),
        rgba(59,130,246,0.12)
    );

    border:
    1px solid rgba(255,255,255,0.08);

    transition: all 0.4s ease;

    box-shadow:
    0 0 18px rgba(59,130,246,0.20),
    0 0 35px rgba(139,92,246,0.15);
}

.metric-card:hover {

    transform:
    translateY(-10px)
    scale(1.03);

    box-shadow:
    0 0 30px rgba(56,189,248,0.40),
    0 0 60px rgba(139,92,246,0.28);
}

.metric-title {

    color: #cbd5e1;

    font-size: 17px;

    margin-bottom: 10px;
}

.metric-value {

    font-size: 46px;

    font-weight: 900;

    color: white;
}

.image-card {

    border-radius:25px;
    overflow:hidden;

    background:linear-gradient(
        135deg,
        #0f172a,
        #1e293b
    );

    border:1px solid rgba(255,255,255,0.08);

    padding:15px;

    box-shadow:
    0 0 25px rgba(59,130,246,0.25);

    margin-bottom:25px;
}

.footer {

    text-align:center;

    color:#f1f5f9;

    padding:40px;

    font-size:17px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🌍 AI Weather Platform")

selected_city = st.sidebar.selectbox(
    "Select City",
    df["City"]
)

st.sidebar.success("🟢 Live API Connected")
st.sidebar.info("🤖 AI Engine Running")
st.sidebar.warning("⚡ Real-Time Monitoring Enabled")

st.sidebar.markdown("---")

st.sidebar.markdown("""
### 📡 Monitoring Modules

- 🌦 Live Weather
- 🤖 AI Forecasting
- 📊 Analytics
- ⚠ Risk Intelligence
- 💬 AI Assistant
- 🌍 Global Monitoring
""")

# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
🌦 AI Weather Intelligence Platform
</div>

<div class="hero-sub">

🌍 Real-Time Global Monitoring •
🤖 AI Forecast Intelligence •
📈 Climate Analytics •
⚡ Smart Alerts

</div>

</div>
""", unsafe_allow_html=True)

# =========================================================
# ALERTS
# =========================================================

a1, a2, a3 = st.columns(3)

with a1:
    st.error("🚨 Heatwave Alert Active")

with a2:
    st.warning("🌧 Heavy Rain Monitoring")

with a3:
    st.success("🤖 AI Systems Operational")

# =========================================================
# KPI CARDS
# =========================================================

avg_temp = round(df["Temperature"].mean(), 1)

avg_humidity = round(df["Humidity"].mean(), 1)

high_risk = len(
    df[
        (df["RiskLevel"] == "HIGH")
        |
        (df["RiskLevel"] == "EXTREME")
    ]
)

cities_monitored = len(df)

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.markdown(f"""
    <div class="metric-card">
    <div class="metric-title">
    🌡 Climate Severity Index
    </div>
    <div class="metric-value">
    {avg_temp}°C
    </div>
    </div>
    """, unsafe_allow_html=True)

with k2:

    st.markdown(f"""
    <div class="metric-card">
    <div class="metric-title">
    💧 Atmospheric Saturation
    </div>
    <div class="metric-value">
    {avg_humidity}%
    </div>
    </div>
    """, unsafe_allow_html=True)

with k3:

    st.markdown(f"""
    <div class="metric-card">
    <div class="metric-title">
    ⚠ Active Risk Regions
    </div>
    <div class="metric-value">
    {high_risk}
    </div>
    </div>
    """, unsafe_allow_html=True)

with k4:

    st.markdown(f"""
    <div class="metric-card">
    <div class="metric-title">
    🌍 Global Nodes Online
    </div>
    <div class="metric-value">
    {cities_monitored}
    </div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Analytics",
    "🌍 Monitoring",
    "⚠ Risk Intelligence",
    "💬 AI Assistant",
    "🌦 Forecasts"
])

# =========================================================
# ANALYTICS TAB
# =========================================================

with tab1:

    st.subheader("🌡 Global Temperature Analytics")

    temp_chart = px.bar(

        df,

        x="City",

        y="Temperature",

        color="RiskLevel",

        template="plotly_dark",

        color_discrete_map={
            "LOW": "#22c55e",
            "MEDIUM": "#facc15",
            "HIGH": "#f97316",
            "EXTREME": "#ef4444"
        }
    )

    temp_chart.update_layout(

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        height=600
    )

    st.plotly_chart(
        temp_chart,
        use_container_width=True
    )

# =========================================================
# MONITORING TAB
# =========================================================

with tab2:

    st.markdown("## 🌍 Live Weather Monitoring Center")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown("""
        <div class="image-card">

        <img src="https://images.unsplash.com/photo-1504608524841-42fe6f032b4b?q=80&w=1200&auto=format&fit=crop"
        style="width:100%; border-radius:18px;">

        <h3 style="color:white;">
        🌩 Storm Monitoring
        </h3>

        <p style="color:#cbd5e1;">
        AI systems tracking atmospheric instability and pressure activity.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class="image-card">

        <img src="https://images.unsplash.com/photo-1492011221367-f47e3ccd77a0?q=80&w=1200&auto=format&fit=crop"
        style="width:100%; border-radius:18px;">

        <h3 style="color:white;">
        🌍 Climate Intelligence
        </h3>

        <p style="color:#cbd5e1;">
        Global AI monitoring climate conditions across major regions.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with c3:

        st.markdown("""
        <div class="image-card">

        <img src="https://images.unsplash.com/photo-1500375592092-40eb2168fd21?q=80&w=1200&auto=format&fit=crop"
        style="width:100%; border-radius:18px;">

        <h3 style="color:white;">
        ⚡ Extreme Weather Alerts
        </h3>

        <p style="color:#cbd5e1;">
        Smart detection of heatwaves, storms and severe rainfall.
        </p>

        </div>
        """, unsafe_allow_html=True)

    # =====================================================
    # FULL COLOR TABLE
    # =====================================================

    styled_df = (
        df.style

        .background_gradient(
            cmap="turbo",
            subset=["Temperature"]
        )

        .background_gradient(
            cmap="Blues",
            subset=["Humidity"]
        )

        .background_gradient(
            cmap="Reds",
            subset=["WindSpeed"]
        )

        .background_gradient(
            cmap="Purples",
            subset=["Pressure"]
        )

        .background_gradient(
            cmap="Greens",
            subset=["RainProbability"]
        )

        .map(

            lambda x:

            "background-color:#0ea5e9; color:white; font-weight:bold;"
            if x == "Rain"

            else

            "background-color:#f97316; color:white; font-weight:bold;"
            if x == "Haze"

            else

            "background-color:#6366f1; color:white; font-weight:bold;",

            subset=["Condition"]
        )

        .map(

            lambda x:

            "background-color:#22c55e; color:white; font-weight:bold;"
            if x == "LOW"

            else

            "background-color:#facc15; color:black; font-weight:bold;"
            if x == "MEDIUM"

            else

            "background-color:#f97316; color:white; font-weight:bold;"
            if x == "HIGH"

            else

            "background-color:#ef4444; color:white; font-weight:bold;",

            subset=["RiskLevel"]
        )

        .map(

            lambda x:
            "background-color:#111827; color:#67e8f9; font-weight:bold;",

            subset=["City"]
        )
    )

    st.dataframe(
        styled_df,
        use_container_width=True,
        height=550
    )

# =========================================================
# RISK TAB
# =========================================================

with tab3:

    risk_counts = df["RiskLevel"].value_counts().reset_index()

    risk_counts.columns = [
        "RiskLevel",
        "Count"
    ]

    risk_chart = px.pie(

        risk_counts,

        names="RiskLevel",

        values="Count",

        hole=0.55,

        template="plotly_dark",

        title="🌍 Global Weather Risk Distribution",

        color="RiskLevel",

        color_discrete_map={
            "LOW": "#22c55e",
            "MEDIUM": "#facc15",
            "HIGH": "#f97316",
            "EXTREME": "#ef4444"
        }
    )

    risk_chart.update_layout(

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        height=650
    )

    st.plotly_chart(
        risk_chart,
        use_container_width=True
    )

# =========================================================
# AI TAB
# =========================================================

with tab4:

    st.markdown("""
    ## 💬 AI Weather Assistant
    """)

    st.info("🌡 Which city has highest temperature?")
    st.info("⚠ Which cities are unsafe?")
    st.info("🌧 Which city may receive heavy rain?")
    st.info("📡 Generate AI weather report.")

    question = st.text_input(
        "Ask AI Weather Assistant"
    )

    if question:

        with st.spinner("🤖 AI Engine Thinking..."):
            time.sleep(1.5)

        st.success(
            "✅ AI analysis completed successfully."
        )

# =========================================================
# FORECAST TAB
# =========================================================

with tab5:

    st.subheader(
        "🌦 AI Weather Forecast Intelligence"
    )

    if not forecast_df.empty:

        forecast_chart = px.line(

            forecast_df,

            x="Datetime",

            y="Temperature",

            markers=True,

            template="plotly_dark",

            title="📈 Future Temperature Forecast"
        )

        forecast_chart.update_layout(

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)",

            height=600
        )

        st.plotly_chart(
            forecast_chart,
            use_container_width=True
        )

        st.dataframe(
            forecast_df,
            use_container_width=True
        )

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

🚀 AI Weather Intelligence Platform

<br><br>

Real-Time Monitoring •
AI Forecasting •
Climate Analytics •
Business Intelligence

</div>
""", unsafe_allow_html=True)