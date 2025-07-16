import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load pre-trained model and scaler (ensure these files are in the same directory as your Streamlit app)
model = joblib.load('./Models/KNeighborsClassifier.pkl')  # Load your pre-trained model
scaler = joblib.load('./Models/scaler.pkl')  # Load your pre-trained scaler

# Function to make predictions
def predict_heart_attack(data):
    # Scale the data using the same scaler used during training
    data_scaled = scaler.transform([data])
    
    # Predict heart attack risk using the trained model
    prediction = model.predict(data_scaled)
    
    return prediction[0]

# Streamlit UI
st.title('Heart Attack Risk Prediction')

# Input Fields for user
st.subheader('Enter the following details')

# Collect user inputs
age = st.number_input('Age', min_value=20, max_value=100, value=50)
sex = st.selectbox('Sex', ['Male', 'Female'])
cholesterol = st.selectbox('Cholesterol Level', ['Normal', 'Above Normal', 'Well Above Normal'])
blood_pressure = st.selectbox('Blood Pressure', ['Normal', 'High', 'Very High'])
heart_rate = st.number_input('Heart Rate', min_value=40, max_value=200, value=70)
diabetes = st.selectbox('Diabetes', ['Yes', 'No'])
family_history = st.selectbox('Family History of Heart Disease', ['Yes', 'No'])
smoking = st.selectbox('Do you smoke?', ['Yes', 'No'])
obesity = st.selectbox('Are you obese?', ['Yes', 'No'])
alcohol = st.selectbox('Do you consume alcohol?', ['Yes', 'No'])
exercise_hours = st.number_input('Exercise Hours per Week', min_value=0.0, max_value=40.0, value=3.0)
diet = st.selectbox('Diet Type', ['Healthy', 'Unhealthy'])
previous_heart_problems = st.selectbox('Previous Heart Problems', ['Yes', 'No'])
medication_use = st.selectbox('Medication Use', ['Yes', 'No'])
stress_level = st.selectbox('Stress Level', ['Low', 'Medium', 'High'])
sedentary_hours = st.number_input('Sedentary Hours per Day', min_value=0.0, max_value=24.0, value=8.0)
income = st.number_input('Income Level', min_value=1000, max_value=1000000, value=50000)
bmi = st.number_input('BMI', min_value=10.0, max_value=50.0, value=25.0)
triglycerides = st.number_input('Triglycerides Level', min_value=50, max_value=500, value=150)
physical_activity_days = st.number_input('Physical Activity Days per Week', min_value=0, max_value=7, value=3)
sleep_hours = st.number_input('Sleep Hours per Day', min_value=0, max_value=24, value=7)
country = st.selectbox('Country', ['USA', 'India', 'UK', 'Canada', 'Australia'])  # Example countries
continent = st.selectbox('Continent', ['North America', 'Asia', 'Europe', 'Oceania'])
hemisphere = st.selectbox('Hemisphere', ['Northern', 'Southern'])

# Prepare the user input data as a list for prediction
user_data = [
    age,
    1 if sex == 'Male' else 0,  # Encoding sex as binary
    1 if cholesterol == 'Above Normal' else (2 if cholesterol == 'Well Above Normal' else 0),  # Encoding cholesterol levels
    1 if blood_pressure == 'High' else (2 if blood_pressure == 'Very High' else 0),  # Encoding BP levels
    heart_rate,
    1 if diabetes == 'Yes' else 0,
    1 if family_history == 'Yes' else 0,
    1 if smoking == 'Yes' else 0,
    1 if obesity == 'Yes' else 0,
    1 if alcohol == 'Yes' else 0,
    exercise_hours,
    1 if diet == 'Healthy' else 0,
    1 if previous_heart_problems == 'Yes' else 0,
    1 if medication_use == 'Yes' else 0,
    1 if stress_level == 'High' else (2 if stress_level == 'Medium' else 0),  # Stress Level encoding
    sedentary_hours,
    income,
    bmi,
    triglycerides,
    physical_activity_days,
    sleep_hours,
    1 if country == 'USA' else 0,  # You could add country encoding if necessary
    1 if continent == 'North America' else 0,  # Similar for continent encoding
    1 if hemisphere == 'Northern' else 0  # Hemisphere encoding
]

# Display prediction when user hits the button
if st.button('Predict Heart Attack Risk'):
    prediction = predict_heart_attack(user_data)
    if prediction == 1:
        st.error("High Risk of Heart Attack!")
    else:
        st.success("Low Risk of Heart Attack!")
