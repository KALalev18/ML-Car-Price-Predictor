# Car Price predictor by using Machine Leearning

I made a simple web application for predicting car prices using machine learning. This app allows users to input various features of a car and receive a predicted price based on a pre-trained machine learning model. The application is built using Streamlit and Python, API from [Kaggle](https://www.kaggle.com/datasets/hellbuoy/car-price-prediction?phase=FinishSSORegistration&returnUrl=%2Fdatasets%2Fhellbuoy%2Fcar-price-prediction%2Fversions%2F1%3Fresource%3Ddownload&SSORegistrationToken=CfDJ8F_DuqmsDTJPtLCFEKPd8dzZVg7wPGwHTlpCrwZI9m2juwS1cUqNV2TBSC4-3UEQl1iC-jsqiSBfx1OxQCizAWjhe1jHSoB6a9HVphP0hPJcNg_C1EPF-NBOaxQ5DHZPfM6PhgMBo_woADJdWaAdzJh6jZpBF66a456TecudDzX_tJGzUlQZUgHzcjfNvwdiGf0z7-mVHBLSwWDLoUIy3XGekyJfJyasSkrYWnPHcISpqls9pngBJnGfFQLgwfsUOvRU_nkDf-_4XfJ74VRcAhXPopv9Z_JAaHlTTGaHkqPBly3eo5vC6gUxe68k1kEbUyDu4PrKJfRoNTHNdRvLtj2_o82r-ezh&DisplayName=Kristian+Lalev&messageId=internalError&field=Unspecified).

# Features
      •	Predicting car prices based on input features for car width, car height, and fuel system.
      •	Adjusted predictions based on fuel type (as a non-expert):
              o	gas: no price adjustment
              o	diesel: price increased by 10%
              o	electric: price increased by 20%
              o	hybrid: price increased by 30%
# Requirements
      •	Python 3.6+
      •	Downloading Streamlit, Joblib, NumPy packages
      •	A pre-trained machine learning model saved as model.not

# Installation 

To set up the project, follow these steps:

1. Clone the repository:
  git clone https://github.com/KALalev18/car-price-predictor.git
  cd car-price-predictor

2. Install the required packages:
  pip install streamlit joblib numpy

3. Run the streamlit application:
		streamlit run app.py

4. Open your web browser and navigate to the URL provided by Streamlit (or http://localhost:8501).

5.  Enter the car features:
  •	Car width: Numeric input for the width of the car.
  •	Car height: Numeric input for the height of the car.
  •	Fuel system: From the dropdown menu, select from gas, diesel, electric, or hybrid.

6. Click the "Predict" button to see the estimated car price.

Prerequisites:  
  The Streamlit framework for creating interactive web applications.
  Scikit-learn or other Machine Learning (ML) libraries used for model training (assumed based on context).


