import streamlit as st
import pandas as pd
from prophet import Prophet
import os
import pandas as pd

# Dynamically resolve path to sales_data.csv
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'sales_data.csv')

# Load the dataset
df = pd.read_csv(DATA_PATH)

st.title("🛍️ Retail Demand Forecast")

df = df.rename(columns={'date': 'ds', 'sales': 'y'})

model = Prophet()
model.fit(df)

future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

st.line_chart(forecast[['ds', 'yhat']].set_index('ds'))
if not os.path.exists(DATA_PATH):
    st.error("❌ sales_data.csv not found. Please run generate_data.py to create it.")
    st.stop()
