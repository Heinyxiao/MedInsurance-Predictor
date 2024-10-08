import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso  # Or import your final model
import pickle  # For loading the saved model

# Load your trained model (assuming you've saved it)
model = pickle.load(open("lasso_model.pkl", "rb"))

# Create a title and description for the web app
st.title("Healthcare Insurance Charge Predictor")
st.write("""
Enter your personal information to predict your healthcare insurance charges.
""")

# Get user input data
age = st.slider('Age', 18, 100, 30)
sex = st.selectbox('Sex', ('Male', 'Female'))
bmi = st.slider('BMI', 15.0, 50.0, 25.0)
children = st.selectbox('Number of Children', [0, 1, 2, 3, 4, 5])
smoker = st.selectbox('Smoker', ('Yes', 'No'))
region = st.selectbox('Region', ('Southeast', 'Southwest', 'Northeast', 'Northwest'))

# Preprocess user input for the model
def preprocess_input(age, sex, bmi, children, smoker, region):
    # Example transformation; adjust according to your model’s preprocessing steps
    data = np.array([[age, bmi, children, 1 if smoker == 'Yes' else 0, 
                      1 if sex == 'Male' else 0, 
                      1 if region == 'Southeast' else 0, 
                      1 if region == 'Southwest' else 0, 
                      1 if region == 'Northeast' else 0]])
    return data

# Preprocess user data
user_data = preprocess_input(age, sex, bmi, children, smoker, region)

# Predict insurance charges using the model
predicted_charge = model.predict(user_data)

# Display the prediction
st.subheader(f"Predicted Insurance Charge: ${predicted_charge[0]:,.2f}")
