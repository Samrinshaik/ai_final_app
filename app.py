import streamlit as st
import joblib
import numpy as np


model = joblib.load("model.pkl")

st.title("🚀 Rocket Thrust Predictor")

# inputs (same as your training)
time = st.number_input("Time (s)")
altitude = st.number_input("Altitude (m)")
velocity = st.number_input("Velocity (m/s)")
mass = st.number_input("Mass (kg)")

# prediction
if st.button("Predict Thrust"):
    data = np.array([[time, altitude, velocity, mass]])
    result = model.predict(data)

    st.success(f"Predicted Thrust: {result[0]:.2f} N")
