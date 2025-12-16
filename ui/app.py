import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ✅ Fix Python path so agent & tools modules are found
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
import plotly.graph_objects as go
import folium
from streamlit_folium import folium_static
from PIL import Image
from agent.agent import plan_trip
from agent.langchain_agent import run_agent
from tools.budget import estimate_budget

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Agentic AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Animated Background */
    .main {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        padding: 0 !important;
        margin: 0 !important;
    }
    
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        max-width: 100% !important;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Floating Animation */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    /* Pulse Animation */
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    /* Glow Animation */
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 20px rgba(255, 255, 255, 0.3); }
        50% { box-shadow: 0 0 40px rgba(255, 255, 255, 0.6), 0 0 60px rgba(102, 126, 234, 0.4); }
    }
    
    /* Header Styling with Animation */
    h1 {
        background: linear-gradient(45deg, #FFD700, #FFA500, #FFD700, #FF69B4);
        background-size: 300% 300%;
        animation: gradientShift 3s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 4rem !important;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: 2px;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.2);
        animation: float 3s ease-in-out infinite;
    }
    
    /* Subtitle with Glow */
    .subtitle {
        text-align: center;
        color: #ffffff;
        font-size: 1.4rem;
        margin-bottom: 2rem;
        font-weight: 400;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
        animation: pulse 2s ease-in-out infinite;
    }
    
    /* Enhanced Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(20px);
        border-radius: 25px;
        padding: 2.5rem;
        border: 2px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.4), 
                    inset 0 0 20px rgba(255, 255, 255, 0.1);
        margin-bottom: 2rem;
        animation: glow 3s ease-in-out infinite;
    }
    
    /* Enhanced Input Styling */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        border: 3px solid transparent;
        background-image: linear-gradient(white, white), 
                          linear-gradient(135deg, #667eea, #764ba2, #f093fb);
        background-origin: border-box;
        background-clip: padding-box, border-box;
        padding: 1rem;
        font-size: 1.1rem;
        font-weight: 500;
        transition: all 0.4s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .stTextInput > div > div > input:focus {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Premium Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 1.2rem 3rem;
        font-size: 1.3rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 10px 40px rgba(245, 87, 108, 0.5);
        text-transform: uppercase;
        letter-spacing: 1px;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button:before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover:before {
        left: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 15px 50px rgba(245, 87, 108, 0.7);
    }
    
    /* Section Headers with Icons */
    .section-header {
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.8rem;
        animation: float 3s ease-in-out infinite;
    }
    
    /* Enhanced Hotel Card */
    .hotel-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 15px 50px rgba(102, 126, 234, 0.4);
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    
    .hotel-card:before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: pulse 4s ease-in-out infinite;
    }
    
    .hotel-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.6);
    }
    
    .hotel-name {
        font-size: 2.5rem;
        font-weight: 800;
        color: white;
        margin-bottom: 0.8rem;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.2);
    }
    
    .hotel-price {
        font-size: 2rem;
        font-weight: 700;
        color: #FFD700;
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
    }
    
    /* Vibrant Itinerary Cards */
    .itinerary-day {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 40px rgba(250, 112, 154, 0.4);
        transition: all 0.3s ease;
    }
    
    .itinerary-day:hover {
        transform: scale(1.02);
        box-shadow: 0 15px 50px rgba(250, 112, 154, 0.6);
    }
    
    /* Enhanced Place Items */
    .place-item {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        display: flex;
        align-items: center;
        gap: 1.5rem;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #fa709a;
    }
    
    .place-item:hover {
        transform: translateX(15px) scale(1.03);
        box-shadow: 0 10px 30px rgba(250, 112, 154, 0.3);
        border-left-width: 8px;
    }
    
    /* Link hover effects */
    a:hover .place-item {
        background: #f8f9fa;
    }
    
    /* Stunning Budget Card */
    .budget-card {
        background: linear-gradient(135deg, #00d2ff 0%, #3a47d5 100%);
        border-radius: 25px;
        padding: 2.5rem;
        box-shadow: 0 15px 50px rgba(0, 210, 255, 0.4);
        color: white;
        position: relative;
        overflow: hidden;
    }
    
    .budget-card:before {
        content: '💰';
        position: absolute;
        font-size: 20rem;
        opacity: 0.1;
        right: -5rem;
        bottom: -5rem;
        animation: float 6s ease-in-out infinite;
    }
    
    .budget-item {
        display: flex;
        justify-content: space-between;
        padding: 1.2rem 0;
        border-bottom: 2px solid rgba(255,255,255,0.2);
        font-size: 1.2rem;
        font-weight: 500;
    }
    
    .budget-total {
        font-size: 2.2rem;
        font-weight: 900;
        color: #FFD700;
        margin-top: 1.5rem;
        text-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
        animation: pulse 2s ease-in-out infinite;
    }
    
    /* Premium Flight Card */
    .flight-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 15px 50px rgba(102, 126, 234, 0.5);
        color: white;
        transition: all 0.3s ease;
    }
    
    .flight-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.7);
    }
    
    /* AI Reasoning Card with Gradient Border */
    .ai-reasoning {
        background: white;
        border-radius: 25px;
        padding: 2.5rem;
        color: #2d3748;
        line-height: 2;
        font-size: 1.1rem;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.1);
        border: 3px solid transparent;
        background-image: linear-gradient(white, white), 
                          linear-gradient(135deg, #667eea, #764ba2, #f093fb, #43e97b);
        background-origin: border-box;
        background-clip: padding-box, border-box;
        position: relative;
        animation: glow 3s ease-in-out infinite;
    }
    
    /* Slider Enhancement */
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #f093fb 0%, #f5576c 100%) !important;
        height: 8px !important;
    }
    
    .stSlider > div > div > div > div {
        background: white !important;
        box-shadow: 0 0 15px rgba(245, 87, 108, 0.5) !important;
        width: 24px !important;
        height: 24px !important;
    }
    
    /* Hide Streamlit Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    
    /* Success Message Enhancement */
    .element-container .stAlert {
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
        border-radius: 15px;
        padding: 1.5rem;
        font-weight: 600;
        font-size: 1.1rem;
        box-shadow: 0 10px 30px rgba(67, 233, 123, 0.4);
        animation: pulse 1s ease-in-out;
    }
    
    /* Hero Banner Styling */
    .hero-banner {
        border-radius: 0 0 30px 30px;
        overflow: hidden;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        margin-bottom: 1.5rem;
        position: relative;
        animation: float 4s ease-in-out infinite;
        margin-top: 0 !important;
    }
    
    .hero-banner img {
        width: 100%;
        height: auto;
        display: block;
    }
    
    /* Content Wrapper */
    .content-wrapper {
        padding: 0 2rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- HERO BANNER (CSS-ONLY - GUARANTEED TO WORK!) ----------------
st.markdown('''
<div style="
    background: linear-gradient(135deg, 
        #667eea 0%, 
        #764ba2 25%, 
        #f093fb 50%, 
        #4facfe 75%, 
        #00f2fe 100%);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    padding: 4rem 2rem;
    border-radius: 25px;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 25px 70px rgba(102, 126, 234, 0.5);
    position: relative;
    overflow: hidden;
">
    <!-- Floating Emojis Background -->
    <div style="
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        opacity: 0.15;
        font-size: 4rem;
        display: flex;
        justify-content: space-around;
        align-items: center;
        flex-wrap: wrap;
        pointer-events: none;
    ">
        <span style="animation: float 6s ease-in-out infinite;">✈️</span>
        <span style="animation: float 8s ease-in-out infinite;">🌍</span>
        <span style="animation: float 7s ease-in-out infinite;">🏖️</span>
        <span style="animation: float 9s ease-in-out infinite;">🗺️</span>
        <span style="animation: float 5s ease-in-out infinite;">🧳</span>
        <span style="animation: float 10s ease-in-out infinite;">🏨</span>
        <span style="animation: float 6.5s ease-in-out infinite;">🎫</span>
        <span style="animation: float 8.5s ease-in-out infinite;">📸</span>
    </div>
    
    <!-- Main Content -->
    <div style="position: relative; z-index: 1;">
        <div style="
            font-size: 1rem;
            color: rgba(255,255,255,0.9);
            font-weight: 600;
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-bottom: 1rem;
            animation: fadeInDown 1s ease;
        ">
            ✨ Welcome to ✨
        </div>
        
        <h1 style="
            color: white;
            font-size: 4rem;
            font-weight: 900;
            margin: 1rem 0;
            text-shadow: 
                2px 2px 8px rgba(0,0,0,0.3),
                0 0 40px rgba(255,255,255,0.2);
            animation: fadeInScale 1.2s ease;
            line-height: 1.2;
        ">
            <span style="display: inline-block; animation: bounce 2s ease infinite;">✈️</span>
            Agentic AI Travel Planner
            <span style="display: inline-block; animation: bounce 2s ease 0.5s infinite;">🌍</span>
        </h1>
        
        <p style="
            color: rgba(255,255,255,0.95);
            font-size: 1.4rem;
            font-weight: 500;
            margin-top: 1.5rem;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
            animation: fadeInUp 1.4s ease;
        ">
            🤖 Your AI-Powered Trip Planning Assistant
        </p>
        
        <div style="
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 2rem;
            flex-wrap: wrap;
            animation: fadeInUp 1.6s ease;
        ">
            <div style="
                background: rgba(255,255,255,0.2);
                backdrop-filter: blur(10px);
                padding: 1rem 2rem;
                border-radius: 50px;
                border: 2px solid rgba(255,255,255,0.3);
                font-weight: 600;
                color: white;
            ">
                🌍 Any Destination Worldwide
            </div>
            <div style="
                background: rgba(255,255,255,0.2);
                backdrop-filter: blur(10px);
                padding: 1rem 2rem;
                border-radius: 50px;
                border: 2px solid rgba(255,255,255,0.3);
                font-weight: 600;
                color: white;
            ">
                🎯 AI-Powered Recommendations
            </div>
        </div>
    </div>
</div>

<style>
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeInScale {
        from {
            opacity: 0;
            transform: scale(0.9);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes bounce {
        0%, 100% {
            transform: translateY(0);
        }
        50% {
            transform: translateY(-10px);
        }
    }
</style>
''', unsafe_allow_html=True)


st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("# ✈️ Agentic AI Travel Planner")
st.markdown('''
<div style="
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 1rem 2rem;
    border-radius: 15px;
    margin: 0 auto 2rem auto;
    max-width: 900px;
    box-shadow: 0 10px 40px rgba(102, 126, 234, 0.4);
">
    <p style="
        text-align: center;
        color: #ffffff;
        font-size: 1.4rem;
        margin: 0;
        font-weight: 500;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    ">
        Plan your dream trip with AI-powered recommendations for flights, hotels, places & weather
    </p>
</div>
''', unsafe_allow_html=True)

# ---------------- INPUT SECTION ----------------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown("### 🧳 Enter Your Trip Details")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    src = st.text_input("📍 From City", placeholder="e.g., Delhi", label_visibility="visible")

with col2:
    dest = st.text_input("🎯 Destination City", placeholder="e.g., Goa", label_visibility="visible")

with col3:
    days = st.slider("📅 Trip Duration (days)", min_value=1, max_value=7, value=3)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- GENERATE BUTTON ----------------
if st.button("🚀 Generate My Dream Trip", use_container_width=True):

    if not src or not dest:
        st.error("❌ Please enter both source and destination cities.")
    else:
        with st.spinner("✨ AI is crafting your perfect trip..."):
            try:
                # Get structured plan
                plan = plan_trip(
                    src=src,
                    dest=dest,
                    days=days,
                    lat=15.25,
                    lon=74.125
                )

                # Get LangChain agent reasoning
                query = f"Plan a trip from {src} to {dest} for {days} days, including flights, hotels, places, weather, and budget."
                agent_response = run_agent(query)
                reasoning = agent_response.get("output", "No reasoning provided.")

                # Calculate budget
                budget = estimate_budget(plan["flight"], plan["hotel"], days)

                st.success("✅ Your Personalized Travel Plan is Ready!")
                st.balloons()

                # ---------------- AI REASONING ----------------
                st.markdown("---")
                st.markdown('<div class="section-header">🤖 AI Travel Insights</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="ai-reasoning">{reasoning}</div>', unsafe_allow_html=True)

                # ---------------- RESULTS LAYOUT ----------------
                st.markdown("---")
                
                # Two Column Layout
                col_left, col_right = st.columns([1, 1])
                
                with col_left:
                    # FLIGHT CARD
                    st.markdown('<div class="section-header">✈️ Flight Details</div>', unsafe_allow_html=True)
                    st.markdown('<div class="flight-card">', unsafe_allow_html=True)
                    
                    if "message" in plan["flight"]:
                        st.warning(f"⚠️ {plan['flight']['message']}")
                    else:
                        st.markdown(f"**Flight:** {plan['flight'].get('flight_number', 'N/A')}")
                        st.markdown(f"**From:** {plan['flight'].get('from', src)}")
                        st.markdown(f"**To:** {plan['flight'].get('to', dest)}")
                        st.markdown(f"**Duration:** {plan['flight'].get('duration', 'N/A')}")
                        st.markdown(f"**Price:** ₹{plan['flight'].get('price', 0):,}")
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # HOTEL CARD
                    st.markdown('<div class="section-header">🏨 Hotel Recommendation</div>', unsafe_allow_html=True)
                    st.markdown('<div class="hotel-card">', unsafe_allow_html=True)
                    
                    hotel = plan["hotel"]
                    
                    # Check if hotel has a message (no hotels found) or actual hotel data
                    if "message" in hotel:
                        st.warning(f"⚠️ {hotel['message']}")
                    else:
                        hotel_search_query = f"{hotel['name']} {hotel['city']}"
                        hotel_maps_link = f"https://www.google.com/maps/search/?api=1&query={hotel_search_query.replace(' ', '+')}"
                        
                        st.markdown(f'<div class="hotel-name">{hotel["name"]}</div>', unsafe_allow_html=True)
                        st.markdown(f"⭐ **{hotel['stars']} Star Hotel** in {hotel['city']}")
                        st.markdown(f'<div class="hotel-price">₹{hotel["price_per_night"]:,} / night</div>', unsafe_allow_html=True)
                        st.markdown(f"**Amenities:** {', '.join(hotel['amenities'])}")
                        st.markdown(f"**Total Stay Cost:** ₹{hotel['price_per_night'] * days:,}")
                        
                        # Add clickable buttons
                        st.markdown(f'''
                        <a href="{hotel_maps_link}" target="_blank" style="
                            display: inline-block;
                            background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
                            color: #2d3748;
                            padding: 0.8rem 2rem;
                            border-radius: 25px;
                            text-decoration: none;
                            font-weight: 700;
                            margin-top: 1rem;
                            transition: all 0.3s ease;
                            box-shadow: 0 4px 15px rgba(255, 215, 0, 0.4);
                        ">
                            📍 View on Google Maps
                        </a>
                        ''', unsafe_allow_html=True)
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # BUDGET CARD
                    st.markdown('<div class="section-header">💰 Budget Breakdown</div>', unsafe_allow_html=True)
                    st.markdown('<div class="budget-card">', unsafe_allow_html=True)
                    
                    st.markdown(f'<div class="budget-item"><span>✈️ Flight Cost</span><span>₹{budget["flight_cost"]:,}</span></div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="budget-item"><span>🏨 Hotel Cost ({days} nights)</span><span>₹{budget["hotel_cost"]:,}</span></div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="budget-item"><span>🍽️ Food & Local</span><span>₹{budget["food_and_local"]:,}</span></div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="budget-total">💳 Total Estimate: ₹{budget["total_cost"]:,}</div>', unsafe_allow_html=True)
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with col_right:
                    # WEATHER CHART
                    st.markdown('<div class="section-header">🌤️ Weather Forecast</div>', unsafe_allow_html=True)
                    
                    weather_data = plan["weather"]
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(
                        x=list(range(1, len(weather_data) + 1)),
                        y=weather_data,
                        mode='lines+markers',
                        name='Temperature',
                        line=dict(color='#667eea', width=3),
                        marker=dict(size=10, color='#764ba2'),
                        fill='tozeroy',
                        fillcolor='rgba(102, 126, 234, 0.2)'
                    ))
                    fig.update_layout(
                        xaxis_title="Day",
                        yaxis_title="Temperature (°C)",
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        font=dict(color='#2d3748', size=12),
                        height=300,
                        margin=dict(l=20, r=20, t=20, b=20)
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # INTERACTIVE MAP
                    st.markdown('<div class="section-header">🗺️ Travel Route</div>', unsafe_allow_html=True)
                    
                    # City coordinates (approximate)
                    city_coords = {
                        "delhi": [28.6139, 77.2090],
                        "goa": [15.2993, 74.1240],
                        "mumbai": [19.0760, 72.8777],
                        "bangalore": [12.9716, 77.5946],
                        "kolkata": [22.5726, 88.3639],
                        "chennai": [13.0827, 80.2707],
                        "hyderabad": [17.3850, 78.4867],
                        "pune": [18.5204, 73.8567],
                        "jaipur": [26.9124, 75.7873],
                        "agra": [27.1767, 78.0081]
                    }
                    
                    src_lower = src.lower().strip()
                    dest_lower = dest.lower().strip()
                    
                    src_coords = city_coords.get(src_lower, [20.5937, 78.9629])  # Default to India center
                    dest_coords = city_coords.get(dest_lower, [20.5937, 78.9629])
                    
                    # Calculate center point for map
                    center_lat = (src_coords[0] + dest_coords[0]) / 2
                    center_lon = (src_coords[1] + dest_coords[1]) / 2
                    
                    # Create map
                    m = folium.Map(
                        location=[center_lat, center_lon],
                        zoom_start=5,
                        tiles='OpenStreetMap'
                    )
                    
                    # Add markers for source and destination
                    folium.Marker(
                        src_coords,
                        popup=f'<b>{src.title()}</b><br>Departure',
                        tooltip=src.title(),
                        icon=folium.Icon(color='green', icon='plane', prefix='fa')
                    ).add_to(m)
                    
                    folium.Marker(
                        dest_coords,
                        popup=f'<b>{dest.title()}</b><br>Destination',
                        tooltip=dest.title(),
                        icon=folium.Icon(color='red', icon='map-marker', prefix='fa')
                    ).add_to(m)
                    
                    # Draw a line between cities
                    folium.PolyLine(
                        [src_coords, dest_coords],
                        color='#667eea',
                        weight=3,
                        opacity=0.8,
                        popup=f'{src.title()} → {dest.title()}'
                    ).add_to(m)
                    
                    # Display map
                    folium_static(m, width=None, height=400)
                    
                    # ITINERARY
                    st.markdown('<div class="section-header">📅 Day-wise Itinerary</div>', unsafe_allow_html=True)
                    
                    for day, places in plan["itinerary"].items():
                        st.markdown(f'<div class="itinerary-day">', unsafe_allow_html=True)
                        st.markdown(f"### {day}")
                        
                        for p in places:
                            icon_map = {
                                "museum": "🏛️",
                                "fort": "🏰",
                                "market": "🛍️",
                                "temple": "🛕",
                                "beach": "🏖️",
                                "park": "🌳"
                            }
                            icon = icon_map.get(p['type'], "📍")
                            
                            # Create Google Maps link for the place
                            place_search_query = f"{p['name']} {dest}"
                            place_maps_link = f"https://www.google.com/maps/search/?api=1&query={place_search_query.replace(' ', '+')}"
                            
                            st.markdown(f'''
                            <a href="{place_maps_link}" target="_blank" style="text-decoration: none; color: inherit;">
                                <div class="place-item" style="cursor: pointer;">
                                    <span style="font-size: 1.5rem;">{icon}</span>
                                    <div style="flex: 1;">
                                        <div style="font-weight: 600; font-size: 1.1rem;">{p['name']}</div>
                                        <div style="color: #666;">⭐ {p['rating']} • {p['type'].title()}</div>
                                    </div>
                                    <div style="
                                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                                        color: white;
                                        padding: 0.5rem 1rem;
                                        border-radius: 20px;
                                        font-size: 0.85rem;
                                        font-weight: 600;
                                    ">
                                        View on Map 🗺️
                                    </div>
                                </div>
                            </a>
                            ''', unsafe_allow_html=True)
                        
                        st.markdown('</div>', unsafe_allow_html=True)
                
                # ---------------- ADDITIONAL FEATURES ----------------
                st.markdown("---")
                st.markdown('<div style="text-align: center; font-size: 2.5rem; font-weight: 800; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 2rem 0;">More Travel Essentials</div>', unsafe_allow_html=True)
                
                # Three column layout for additional features
                feat_col1, feat_col2, feat_col3 = st.columns([1, 1, 1])
                
                with feat_col1:
                    # PACKING CHECKLIST
                    st.markdown('''
                    <div style="
                        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                        border-radius: 20px;
                        padding: 2rem;
                        color: white;
                        box-shadow: 0 10px 40px rgba(240, 147, 251, 0.4);
                        min-height: 350px;
                    ">
                        <div style="font-size: 3rem; margin-bottom: 1rem;">🎒</div>
                        <div style="font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem;">Packing Checklist</div>
                    ''', unsafe_allow_html=True)
                    
                    # Smart packing based on weather
                    avg_temp = sum(plan["weather"]) / len(plan["weather"])
                    packing_items = [
                        "✓ Comfortable walking shoes",
                        "✓ Sunscreen & sunglasses",
                        "✓ Phone charger & power bank",
                        "✓ Camera",
                        "✓ Medications & first aid",
                        "✓ Travel documents & ID"
                    ]
                    
                    if avg_temp > 30:
                        packing_items.extend([
                            "✓ Light cotton clothes",
                            "✓ Hat/cap for sun",
                            "✓ Water bottle"
                        ])
                    elif avg_temp < 20:
                        packing_items.extend([
                            "✓ Warm jacket",
                            "✓ Sweater/hoodie",
                            "✓ Umbrella"
                        ])
                    else:
                        packing_items.extend([
                            "✓ Light jacket",
                            "✓ Mix of casual wear"
                        ])
                    
                    for item in packing_items:
                        st.markdown(f'<div style="padding: 0.3rem 0; font-size: 0.95rem;">{item}</div>', unsafe_allow_html=True)
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with feat_col2:
                    # FOOD RECOMMENDATIONS
                    st.markdown('''
                    <div style="
                        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
                        border-radius: 20px;
                        padding: 2rem;
                        color: #2d3748;
                        box-shadow: 0 10px 40px rgba(250, 112, 154, 0.4);
                        min-height: 350px;
                    ">
                        <div style="font-size: 3rem; margin-bottom: 1rem;">🍽️</div>
                        <div style="font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem;">Must-Try Foods</div>
                    ''', unsafe_allow_html=True)
                    
                    # Location-based food recommendations
                    food_recommendations = {
                        "goa": ["Fish Curry Rice", "Bebinca", "Vindaloo", "Xacuti", "Feni (drink)"],
                        "delhi": ["Butter Chicken", "Chole Bhature", "Paranthas", "Street Chaat", "Kebabs"],
                        "mumbai": ["Vada Pav", "Pav Bhaji", "Bombay Duck", "Misal Pav", "Street Food"],
                        "bangalore": ["Masala Dosa", "Idli Vada", "Filter Coffee", "Bisi Bele Bath", "Mysore Pak"],
                        "jaipur": ["Dal Baati Churma", "Laal Maas", "Ghewar", "Pyaaz Kachori", "Lassi"]
                    }
                    
                    dest_foods = food_recommendations.get(dest.lower().strip(), [
                        "Local cuisine specialties",
                        "Street food delicacies",
                        "Regional sweets",
                        "Traditional dishes",
                        "Fresh local produce"
                    ])
                    
                    for food in dest_foods:
                        st.markdown(f'<div style="background: white; border-radius: 10px; padding: 0.8rem; margin: 0.5rem 0; font-weight: 500;">🍴 {food}</div>', unsafe_allow_html=True)
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with feat_col3:
                    # TRANSPORTATION GUIDE
                    st.markdown('''
                    <div style="
                        background: linear-gradient(135deg, #00d2ff 0%, #3a47d5 100%);
                        border-radius: 20px;
                        padding: 2rem;
                        color: white;
                        box-shadow: 0 10px 40px rgba(0, 210, 255, 0.4);
                        min-height: 350px;
                    ">
                        <div style="font-size: 3rem; margin-bottom: 1rem;">🚕</div>
                        <div style="font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem;">Local Transport</div>
                    ''', unsafe_allow_html=True)
                    
                    transport_options = [
                        "🚖 Uber/Ola Cabs",
                        "🚌 Local Buses",
                        "🏍️ Bike Rentals",
                        "🚲 Bicycle Rentals",
                        "🚇 Metro (if available)",
                        "🛵 Auto-rickshaws"
                    ]
                    
                    for transport in transport_options:
                        st.markdown(f'<div style="padding: 0.5rem 0; font-size: 0.95rem;">{transport}</div>', unsafe_allow_html=True)
                    
                    st.markdown('''
                        <div style="background: rgba(255,255,255,0.2); border-radius: 10px; padding: 1rem; margin-top: 1rem;">
                            <div style="font-weight: 600; margin-bottom: 0.5rem;">💡 Pro Tip:</div>
                            <div style="font-size: 0.9rem;">Download local transport apps before arriving!</div>
                        </div>
                    </div>
                    ''', unsafe_allow_html=True)
                
                # TRAVEL TIPS & SAFETY
                st.markdown("---")
                tips_col1, tips_col2 = st.columns([1, 1])
                
                with tips_col1:
                    st.markdown('''
                    <div style="
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        border-radius: 20px;
                        padding: 2rem;
                        color: white;
                        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.4);
                    ">
                        <div style="font-size: 2.5rem; margin-bottom: 1rem;">💡 Travel Tips</div>
                        <div style="line-height: 2;">
                            ✓ Book accommodations in advance<br>
                            ✓ Keep digital & physical copies of documents<br>
                            ✓ Learn basic local phrases<br>
                            ✓ Stay hydrated throughout the day<br>
                            ✓ Try to blend in with locals<br>
                            ✓ Keep emergency contacts handy<br>
                            ✓ Respect local customs & culture<br>
                            ✓ Use official taxi services
                        </div>
                    </div>
                    ''', unsafe_allow_html=True)
                
                with tips_col2:
                    st.markdown(f'''
                    <div style="
                        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
                        border-radius: 20px;
                        padding: 2rem;
                        color: #2d3748;
                        box-shadow: 0 10px 40px rgba(67, 233, 123, 0.4);
                    ">
                        <div style="font-size: 2.5rem; margin-bottom: 1rem;">🌤️ Best Time to Visit</div>
                        <div style="background: white; border-radius: 15px; padding: 1.5rem; margin-bottom: 1rem;">
                            <div style="font-size: 1.3rem; font-weight: 700; color: #667eea;">Current Weather</div>
                            <div style="font-size: 2.5rem; font-weight: 800; color: #f5576c; margin: 1rem 0;">{avg_temp:.1f}°C</div>
                            <div style="font-size: 1rem;">Average temperature during your trip</div>
                        </div>
                        <div style="background: rgba(255,255,255,0.9); border-radius: 15px; padding: 1.5rem;">
                            <div style="font-weight: 600; margin-bottom: 0.5rem;">Climate Info:</div>
                            <div style="font-size: 0.95rem; line-height: 1.8;">
                                {'🌡️ Hot weather - Stay hydrated!' if avg_temp > 30 else '❄️ Cool weather - Pack warm clothes!' if avg_temp < 20 else '☀️ Pleasant weather - Perfect for sightseeing!'}
                            </div>
                        </div>
                    </div>
                    ''', unsafe_allow_html=True)
                
                # DOWNLOAD BUTTON
                st.markdown("---")
                st.markdown('''
                <div style="text-align: center; margin: 2rem 0;">
                    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); display: inline-block; border-radius: 50px; padding: 1.5rem 3rem; color: white; font-size: 1.2rem; font-weight: 700; box-shadow: 0 10px 40px rgba(102, 126, 234, 0.5); cursor: pointer;">
                        📥 Download Complete Itinerary (Coming Soon!)
                    </div>
                    <div style="color: rgba(255,255,255,0.8); margin-top: 1rem; font-size: 0.9rem;">
                        Share this amazing trip with your friends! ✈️
                    </div>
                </div>
                ''', unsafe_allow_html=True)

            except Exception as e:
                st.error("⚠️ Oops! Something went wrong while generating your plan.")
                st.exception(e)

st.markdown('</div>', unsafe_allow_html=True)  # Close content wrapper

# ---------------- FOOTER ----------------
st.markdown("""
<div style="
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 20px;
    padding: 2rem;
    margin-top: 3rem;
    text-align: center;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
">
    <div style="font-size: 2rem; margin-bottom: 1rem;">✈️ 🌍 🏨 🗺️</div>
    <div style="color: white; font-size: 1.1rem; font-weight: 500; margin-bottom: 0.5rem;">
        Built with ❤️ using
    </div>
    <div style="color: rgba(255,255,255,0.9); font-size: 1rem; font-weight: 400;">
        Python • Streamlit • Claude AI • Folium Maps • Plotly • Open-Meteo API
    </div>
    <div style="color: rgba(255,255,255,0.7); font-size: 0.9rem; margin-top: 1rem;">
        © 2025 Agentic AI Travel Planner | Powered by AI 🤖
    </div>
</div>
""", unsafe_allow_html=True)

