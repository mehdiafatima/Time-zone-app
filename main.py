import streamlit as st 
from datetime import datetime 
from zoneinfo import ZoneInfo

TIME_ZONES = [
    "UTC", "Asia/Karachi", "America/New_York", "Europe/London", "Australia/Sydney", "Asia/Tokyo", 
    "America/Los_Angeles", "Europe/Berlin", "Asia/Dubai", "Asia/Kolkata", "Asia/Shanghai", 
    "Asia/Singapore", "Europe/Paris", "America/Chicago", "America/Toronto", "America/Mexico_City", "America/Sao_Paulo"
]

# Custom CSS Styling
st.markdown("""
    <style>
        .main-title { 
            font-size: 40px; 
            font-weight: bold; 
            color: darkgreen; 
            text-align: center;
            margin-top: 10px;
            padding-bottom: 10px;
        }
        @media (max-width: 600px) {
            .main-title {
                font-size: 32px;
                margin-top: 5px;
                padding-bottom: 5px;
            }
        }
        .sub-header {
            font-size: 24px;
            font-weight: bold;
            color: darkgreen;
            margin-top: 20px;
        }
        .stButton>button {
            background-color: darkgreen;
            color: white;
            border-radius: 8px;
            padding: 10px 18px;
            font-size: 18px;
        }
        .stButton>button:hover {
            background-color: green;
        }
        .stSelectbox label, .stMultiSelect label, .stTimeInput label {
            font-size: 18px;
            font-weight: bold;
            color: black;
        }
        .stSuccess {
            background-color: #d4edda;
            color: darkgreen;
            padding: 12px;
            border-radius: 6px;
            font-weight: bold;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>Time Zone Converter</div>", unsafe_allow_html=True)

# Multi-select for time zones
selected_timezone = st.multiselect("Select Time Zones", TIME_ZONES, default=["UTC", "Asia/Karachi"])

st.markdown("<div class='sub-header'>Selected Time Zones</div>", unsafe_allow_html=True)
for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime('%Y-%m-%d %I:%M:%S %p')
    st.write(f"**{tz}**: {current_time}")  

st.markdown("<div class='sub-header'>Convert Time Between Time Zones</div>", unsafe_allow_html=True)
current_time = st.time_input("Current Time", value=datetime.now().time())
from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime('%Y-%m-%d %I:%M:%S %p')
    st.markdown(f"<div class='stSuccess'>Converted Time in {to_tz}: {converted_time}</div>", unsafe_allow_html=True)
