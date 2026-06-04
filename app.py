import streamlit as st
import pandas as pd
import pickle
import gzip


# PAGE CONFIG

st.set_page_config(
    page_title="Product Recommendation System",
    layout="wide"
)


# CUSTOM CSS

st.markdown("""
<style>

.stApp{
    background-color:#0E1117;
    color:white;
}

h1,h2,h3{
    color:white;
}

div[data-testid="stMetric"]{
    background-color:#1E293B;
    padding:10px;
    border-radius:10px;
}

.stButton>button{
    background-color:#9333EA;
    color:white;
    border:none;
    border-radius:8px;
    padding:10px 20px;
}

</style>
""", unsafe_allow_html=True)

# LOAD DATA

@st.cache_data
def load_data():
    df = pd.read_csv(
        "ratings.csv",
        header=None,
        names=["userId","productId","rating","timestamp"]
    )
    return df

df = load_data()


# LOAD MODEL FILES

@st.cache_resource
def load_model():
    with gzip.open("product_similarity.pkl.gz","rb") as f:
        similarity = pickle.load(f)

    with open("product_ids.pkl","rb") as f:
        product_ids = pickle.load(f)

    return similarity, product_ids

similarity, product_ids = load_model()


# SIDEBAR

st.sidebar.title("🧭 Navigation")

page = st.sidebar.radio(
    "Go To",
    ["Overview","Get Recommendations"]
)


# OVERVIEW PAGE

if page == "Overview":

    st.title(" Product Recommendation System")

    st.write(
        "This system recommends similar products using Item-Item Collaborative Filtering and Cosine Similarity."
    )

    col1,col2,col3 = st.columns(3)

    col1.metric("Users", df["userId"].nunique())
    col2.metric("Products", df["productId"].nunique())
    col3.metric("Ratings", len(df))


# RECOMMENDATION PAGE

if page == "Get Recommendations":

    st.title("🎯 Product Recommendation Dashboard")

    st.markdown("""
    | Stage | Component | Purpose |
    |---------|------------|------------|
    | 1 | Product Selection | Select Product |
    | 2 | Cosine Similarity | Find Similar Products |
    | 3 | Recommendation Engine | Generate Recommendations |
    """)

    selected_product = st.selectbox(
        "Select Product ID",
        product_ids
    )

    top_n = st.slider(
        "Number of Recommendations",
        min_value=1,
        max_value=10,
        value=5
    )

    if st.button("🚀 Generate Recommendations"):

        try:

            idx = product_ids.index(selected_product)

            similarity_scores = list(
                enumerate(similarity[idx])
            )

            similarity_scores = sorted(
                similarity_scores,
                key=lambda x: x[1],
                reverse=True
            )

            similarity_scores = similarity_scores[1:top_n+1]

            recommendations = [
                product_ids[i[0]]
                for i in similarity_scores
            ]

            st.success(
                "Stage 1 — Product Selected Successfully"
            )

            st.success(
                "Stage 2 — Similar Products Retrieved"
            )

            st.success(
                f"Stage 3 — Top {top_n} Recommendations Generated"
            )

            st.subheader(
                "🏆 Recommended Products"
            )

            for i, product in enumerate(
                recommendations,
                start=1
            ):

                st.markdown(
                    f"""
                    <div style="
                    background:#1E293B;
                    padding:15px;
                    margin-bottom:10px;
                    border-radius:10px;
                    ">
                    <b>{i}. {product}</b>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        except Exception as e:
            st.error(f"Error: {e}")
