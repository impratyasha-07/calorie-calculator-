
import streamlit as st
import gzip
import joblib

with gzip.open("calorie_model.joblib.gz", "rb") as f:
    model = joblib.load(f)

# App title
st.title("Calorie Burn Calculator")

# User inputs
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 10, 80, 25)
height = st.slider("Height (cm)", 120, 220, 165)
weight = st.slider("Weight (kg)", 30, 150, 60)
duration = st.slider("Exercise Duration (minutes)", 5, 120, 30)
heart_rate = st.slider("Heart Rate", 60, 200, 120)
body_temp = st.slider("Body Temperature (°C)", 35.0, 40.0, 37.0)

# Convert gender to numeric
gender_val = 1 if gender == "Male" else 0

# Prediction logic
if st.button("Calculate Calories Burned"):
    bmi = weight / ((height / 100) ** 2)
    input_data = [[gender_val, age, height, weight, duration, heart_rate, body_temp, bmi]]
    result = model.predict(input_data)[0]
    st.success(f"Estimated Calories Burned: {result:.2f} kcal")
