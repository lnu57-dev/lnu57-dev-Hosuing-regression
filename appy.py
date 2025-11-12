import streamlit as st
import pandas as pd

st.title("🏠 Housing Price Predictions")

df = pd.read_csv("pytorch_predictions.csv")
st.subheader("Predicted Prices Table")
st.dataframe(df)

if st.checkbox("Show summary statistics"):
    st.write(df.describe())
