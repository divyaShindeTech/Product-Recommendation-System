import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("ratings.csv")  

# Title
st.title("Product Recommendation System")
st.write("Get product recommendations")

# Product selection
product_name = st.selectbox(
    "Select Product",
   df['productId'].unique()
)
# Recommendation button
if st.button("Recommend"):

    recommendations = df[
        df['productId'] != 'productId'
    ].sample(5)

    st.subheader("Recommended Products")

    for item in recommendations['productId'']:
        st.write(item)

    for item in recommendations['productId']:
        st.write(item)
