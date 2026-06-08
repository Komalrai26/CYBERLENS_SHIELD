import streamlit as st
import pandas as pd
from engine import get_prediction
# Make sure engine.py is in the same directory as app.py

# ... your UI code ...

# 1. Set page configuration for a wide, clean look
st.set_page_config(page_title="CyberLens Shield", layout="wide")

# 2. Inject CSS for the "Neon/Cyber" aesthetic

# Injection of custom CSS for the glowing, dark-tech aesthetic
st.markdown("""
    <style>
    .big-title {
        text-align: center;
        font-size: 60px !important;
        font-weight: bold;
        color: #00f2ff;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        font-size: 24px !important;
        color: #ffffff;
        margin-bottom: 30px;
    }
    .stApp { background-color: #0a0e14; color: #ffffff; }
    .custom-card {
        background-color: #161b22;
        border: 2px solid #00f2ff;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.3);
    }
    .stTextInput > div > div > input {
        background-color: #0a0e14 !important;
        color: #00f2ff !important;
        border: 1px solid #00f2ff !important;
    }
    h1 { color: #00f2ff; text-align: center; }        
    </style>
""", unsafe_allow_html=True)

# 3. Header
st.markdown('<h1 class="big-title">🛡️ CYBERLENS SHIELD</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="sub-title">Advanced Threat Intelligence | Developed by Komal Rai | B.TECH CAPSTONE</h3>', unsafe_allow_html=True)
st.subheader("Web Edition", divider="blue")

# 4. Security Snapshot Section
st.markdown("### 📊 Security Snapshot")
col1, col2, col3 = st.columns(3)

with col1:
    with st.container():
        st.markdown('''
    <div class="custom-card">
        <h4> REAL-TIME MONITORING</h4>
        <p>Status: Active</p>
    </div>
''', unsafe_allow_html=True)
        st.metric(label="Real-Time Status", value="Active", delta="99.8% Uptime")
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.metric(label="Daily Scans", value="1,452", delta="14 Found")
        st.markdown('</div>', unsafe_allow_html=True)

with col3:
    with st.container():
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.metric(label="Threat Index", value="Med-Low", delta="Stable")
        st.markdown('</div>', unsafe_allow_html=True)

# 5. Diagnostic Input
st.write("---")
st.write("### 🔍 URL Diagnostic Input")

# 1. Get the URL from the user
url = st.text_input("Enter URL for detailed diagnostic:", placeholder="https://example.com")

# 2. When the button is clicked, call your engine
if st.button("RUN DIAGNOSTIC", key="diag_btn"):
    with st.spinner("Analyzing URL..."):
        # This calls your model logic from engine.py
        prediction = get_prediction(url) 
        
        # 3. Now display the actual result
        if prediction == 1:
            st.error("⚠️ Phishing Detected!")
        else:
            st.success("✅ Website is Safe.")
