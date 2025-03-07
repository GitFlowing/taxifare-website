import streamlit as st
import datetime
import requests




'''
# TaxiFareModel front
'''

st.markdown('''
# Prediction of taxi fares
''')


default_latitude = 40.730610
default_longitude = -73.935242

date_input = st.date_input(
    "Enter date: ",
    datetime.date(2019, 7, 6))
time_input = st.time_input('Enter time: ', datetime.time(8, 45))

pickup_longitude = st.number_input('Enter your pickup longitude', format="%.6f", value = default_longitude)
pickup_latitude = st.number_input('Enter your pickup latiitude', format="%.6f", value = default_latitude)
dropoff_longitude = st.number_input('Enter your dropoff longitude', format="%.6f", value = (default_longitude +0.01) )
dropoff_latitude = st.number_input('Enter your pickup latitude', format="%.6f", value = (default_latitude +0.01))
passenger_count = st.slider('Select a line count', 1, 8, 1)




parameters = {
    'pickup_datetime': str(date_input) + ' ' + str(time_input),
    'pickup_longitude' : pickup_longitude,
    'pickup_latitude' : pickup_latitude,
    'dropoff_longitude' : dropoff_longitude,
    'dropoff_latitude' : dropoff_latitude,
    'passenger_count' : passenger_count
}


response = requests.get('https://taxifare-245941724758.europe-west1.run.app/predict',
                        parameters).json()

prediction = response
prediction_value = str(round(response['fare'],2))

st.markdown(f'''
## Estimated taxi fares is:
## {prediction_value} €
''')
