## Create app.py

%%writefile app.py

import streamlit as st
import pandas as pd
import pickle

# Title
st.title("Product Recommendation System")
st.write("Get product recommendations based on product ID")

# Load dataset
df = pd.read_csv("ratings.csv")   

# Product input
product_name = st.selectbox(
    "Select Product",
    df['product_name'].unique()
)

# Recommendation Button
if st.button("Recommend"):

    recommendations = df[
        df['product_name'] != product_name
    ].sample(5)

    st.subheader("Recommended Products")

    for item in recommendations['product_name']:
        st.write(item)

