import streamlit as st
import pandas as pd

# Page title
st.title("Product Recommendation System")
st.write("Get product recommendations based on Product ID")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv(
        "ratings.csv",
        header=None,
        names=["userId", "productId", "Rating", "timestamp"]
    )
    df.columns = df.columns.str.strip()
    return df

df = load_data()

# Product selection
product_id = st.selectbox(
    "Select Product Id",
    df["productId"].unique()
)

# Recommendation button
if st.button("Recommend"):

    # Filter products excluding selected one
    recommendations = df[
        df["productId"] != product_id
    ]["productId"].drop_duplicates().sample(
        min(5, len(df))
    )

    st.subheader("Recommended Products")

    # Show recommendations
    for item in recommendations:
        st.write(item)
