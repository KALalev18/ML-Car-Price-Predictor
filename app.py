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
fuel_system = st.selectbox(
    "Fuel system", 
    options=["gas", "diesel", "electric", "hybrid"]
)

st.divider()

other_features = [0] * 134
fuel_type_mapping = {"gas": 1, "diesel": 2, "electric": 3, "hybrid": 4}
fuel_type_code = fuel_type_mapping[fuel_system]

a = [car_width, car_height, fuel_type_code] + other_features
prediction_button = st.button("Predict")

if prediction_button:
    try:
        a_array = np.array([a])
        prediction = model.predict(a_array)[0]
        if fuel_system == "diesel":
            prediction *= 1.10
        elif fuel_system == "electric":
            prediction *= 1.20
        elif fuel_system == "hybrid":
            prediction *= 1.30
        st.write(f"Price prediction is {prediction:.2f}")
    except Exception as e:
        st.write(f"Error in prediction: {e}")
else:
    st.write("Please enter the car width and height to get the prediction")

# order of columns: ['carwidth', 'carheight', 'fuelsystem']