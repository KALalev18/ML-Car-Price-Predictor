import streamlit as st
import joblib
import numpy as np

model = joblib.load('model.not')

st.title("Car price prediction application")
st.divider()

st.write("This app uses Machine Learning to predict car prices with given features. For using this app you can enter these inputs from the UI provided and use the \"Predict\" button")

st.divider()

car_width = st.number_input("Card width", min_value=0, value = 0)
car_height = st.number_input("Car height", min_value=0, value = 0)

st.divider()

other_features = [0] * 135
a = [[car_width, car_height]]+ other_features

prediction_button = st.button("Predict")

if prediction_button:
    a_array = np.array([a])
    prediction = model.predict(a_array)
    st.write(f"Price prediction is {prediction[0]}")
else:
    st.write("Please enter the car width and height to get the prediction")

# order of columns: ['carwidth', 'carheight', 'CarName', 'wheelbase', 'fuelsystem']