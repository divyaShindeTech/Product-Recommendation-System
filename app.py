import streamlit as st
import pandas as pd

# Title
st.title("Product Recommendation System")
st.write("Get product recommendations based on product ID")

# Load dataset
df = pd.read_csv("ratings.csv")  

# Product input
product_id = st.selectbox(
    "Select Product ID",
    df['productId'].unique()
)

# Recommendation Button
if st.button("Recommend"):

    recommendations = df[
        df['productId'] != product_id
    ].sample(5)

    st.subheader("Recommended Products")

    for item in recommendations['productId']:
        st.write(item)
    st.write(df.columns.tolist())
