import streamlit as st
import json
import requests

# Title
st.title('Poly Model - Salary Prediction')

# User Inputs
st.write('Please enter the professional`s months of service')
months_of_service = st.slider('Months of Service', min_value=1, max_value=120, value=60, step=1)

st.write(f'Please enter the professional`s seniority level')
seniority = st.slider('Seniority', min_value=1, max_value=10, value=5, step=1)

# Prepare data to API call
input_features = {
  'months_of_service': months_of_service,
  'seniority': seniority
}

# Create a button to call the API
if st.button('Predict Salary'):
  res = requests.post(url = 'http://127.0.0.1:8000/predict/', data=json.dumps(input_features))
  res_json = json.loads(res.text)
  salary_in_brl = round(res_json['salary_in_brl'], 2)
  st.subheader(f'The predicted salary is R$ {salary_in_brl}')