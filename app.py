
import streamlit as st
import numpy as np

st.set_page_config(layout="wide")

st.title("📱 Smart AQI Mobile App")

pm25 = st.slider("PM2.5", 0, 300)
pm10 = st.slider("PM10", 0, 400)
co = st.slider("CO", 0.0, 5.0)

if st.button("Predict AQI"):

    aqi = 0.5*pm25 + 0.3*pm10 + 5*co

    st.metric("Predicted AQI", int(aqi))

    if aqi < 100:
        st.success("Safe Air Quality")
    elif aqi < 200:
        st.warning("Moderate Pollution")
    else:
        st.error("Dangerous Air Quality 🚨")
