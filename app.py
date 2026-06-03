import streamlit as st
import pandas as pd

# Page title
st.title("Product Recommendation System")
st.write("Get product recommendations based on Product ID")

# Load dataset
@st.cache_data
def load_data():
    # Specify header=None and provide actual column names
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
    sorted(df["productId"].astype(str).unique())
)

# Recommendation button
if st.button("Recommend"):

    # Recommendations
    recommendations = (
        df[df["productId"].astype(str) != str(product_id)]
        ["productId"]
        .astype(str)
        .drop_duplicates()
        .head(5)
        .tolist()
    )

    st.success("Recommendations Generated Successfully!")

    st.subheader("Recommended Products")

    for i, item in enumerate(recommendations, start=1):
        st.write(f"{i}. {item}")
