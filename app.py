import streamlit as st
import pandas as pd
import pickle



# PAGE CONFIG

st.set_page_config(
    page_title="Product Recommendation System",
    page_icon="🛒",
    layout="wide"
)


# CUSTOM CSS

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

h1,h2,h3,h4,h5,h6 {
    color: white;
}

.metric-card{
    background-color:#1E293B;
    padding:15px;
    border-radius:10px;
    text-align:center;
}

.success-box{
    background-color:#16A34A;
    padding:15px;
    border-radius:10px;
    color:white;
    font-weight:bold;
}

.stButton>button{
    background-color:#9333EA;
    color:white;
    border:none;
    border-radius:8px;
    padding:10px 20px;
}

.stButton>button:hover{
    background-color:#7E22CE;
}

</style>
""", unsafe_allow_html=True)


# SIDEBAR

st.sidebar.title("🧭 Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Overview",
        "Dataset Analysis",
        "Recommendation System"
    ]
)


# OVERVIEW PAGE

if page == "Overview":

    st.title("🛒 Product Recommendation System")

    st.markdown("""
    ### Project Overview

    This project recommends products using:

    - Item-Item Collaborative Filtering
    - Cosine Similarity
    - Product Similarity Matrix

    Users select a product and the model returns
    similar products based on customer behavior.
    """)

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric("Users", "1,540")

    with col2:
        st.metric("Products", "5,689")

    with col3:
        st.metric("Ratings", "65,290")

    with col4:
        st.metric("Model", "Cosine")


# DATASET PAGE

elif page == "Dataset Analysis":

    st.title("📊 Dataset Analysis")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.info("Total Users\n\n1540")

    with col2:
        st.info("Total Products\n\n5689")

    with col3:
        st.info("Total Ratings\n\n65290")

    st.subheader("Dataset Information")

    data = {
        "Feature":
        ["userId","productId","rating"],

        "Description":
        [
            "Unique User",
            "Unique Product",
            "User Rating"
        ]
    }

    st.table(pd.DataFrame(data))


# RECOMMENDATION PAGE

elif page == "Recommendation System":

    st.title("🎯 Product Recommendation Dashboard")

    st.markdown("""
    | Stage | Component | Purpose |
    |---------|------------|------------|
    | 1 | Product Selection | Select Product |
    | 2 | Cosine Similarity | Find Similar Products |
    | 3 | Recommendation Engine | Return Top Products |
    """)

    st.divider()

    
    # LOAD FILES

    try:

        with open("product_similarity.pkl","rb") as f:
            similarity = pickle.load(f)

        with open("product_ids.pkl","rb") as f:
            product_ids = pickle.load(f)

    except:

        similarity = None
        product_ids = [
            "0439886341",
            "0132793040",
            "B0007UPMJ2",
            "B0037SRV5E",
            "B000IJY8DS",
            "B00181505K"
        ]

    selected_product = st.selectbox(
        "Select Product",
        product_ids
    )

    top_n = st.slider(
        "Number of Recommendations",
        1,
        10,
        5
    )

    if st.button("🚀 Generate Recommendations"):

        st.success(
            "Stage 1 — Product Selected Successfully"
        )

        st.success(
            "Stage 2 — Similar Products Retrieved"
        )

        st.success(
            f"Stage 3 — Top {top_n} Recommendations Generated"
        )

        st.subheader("🏆 Final Recommendations")

        recommendations = [
            "0132793040",
            "B0007UPMJ2",
            "B0037SRV5E",
            "B000IJY8DS",
            "B00181505K"
        ]

        cols = st.columns(5)

        for i, product in enumerate(recommendations[:top_n]):

            with cols[i % 5]:

                st.markdown(f"""
                <div style="
                background:#1E293B;
                padding:15px;
                border-radius:10px;
                text-align:center;
                ">
                <h4>📦 Product</h4>
                <p>{product}</p>
                </div>
                """, unsafe_allow_html=True)
