import streamlit as st
import pickle
import numpy as np

# load model
model = pickle.load(open("model.pkl", "rb"))

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