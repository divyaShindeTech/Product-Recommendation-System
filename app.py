## Create app.py
import streamlit as st
import pandas as pd

# Title
st.title("Product Recommendation System")
st.write("Get product recommendations")

# Load dataset
df = pd.read_csv("ratings.csv")  

# Product selection
product_name = st.selectbox(
    "Select Product",
    df['product_name'].unique()
)

# Recommendation button
if st.button("Recommend"):
    recommendations = df[
        df['product_name'] != product_name
    ].sample(5)

    st.subheader("Recommended Products")

    for item in recommendations['product_name']:
        st.write(item)
