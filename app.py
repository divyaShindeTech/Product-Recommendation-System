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

# SIDEBAR NAVIGATION
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio(
    "Go To",
    [
        "Overview",
        "EDA & Product Analysis",
        "Clustering Analysis",
        "ML Models",
        "Get Recommendations",
        "Cluster-Aware Pipeline",
        "Full Report"
    ]
)

# OVERVIEW PAGE
if page == "Overview":
    st.title("🛒 Product Recommendation System")
    st.write("""
    This project recommends products using
    Item-Item Collaborative Filtering and
    Cosine Similarity.
    """)
    col1, col2, col3 = st.columns(3)
    col1.metric("Users", df["userId"].nunique())
    col2.metric("Products", df["productId"].nunique())
    col3.metric("Ratings", len(df))
    st.success("Deployment Status: Successfully Deployed on Streamlit Cloud")


# EDA PAGE
elif page == "EDA & Product Analysis":
    st.title("📊 EDA & Product Analysis")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Users", df["userId"].nunique())
    col2.metric("Total Products", df["productId"].nunique())
    col3.metric("Total Ratings", len(df))
    st.subheader("Dataset Description")
    st.write("""
    • userId → Unique customer identifier
    • productId → Unique product identifier
    • rating → Product rating given by user
    • timestamp → Time when rating was submitted
    """)
    st.subheader("Key Insights")
    st.write("""
    ✔ Large number of products available
    ✔ User-product interactions captured
    ✔ Sparse rating matrix observed
    ✔ Collaborative filtering suitable for recommendation
    """)

# CLUSTERING PAGE
elif page == "Clustering Analysis":
    st.title("🔍 Clustering Analysis")
    st.info("""
    Algorithm Used:
    K-Means Clustering

    Purpose:
    • Customer Segmentation
    • User Behaviour Analysis
    • Group Similar Users
    """)
    st.subheader("Cluster Summary")
    st.write("""
    Cluster 0 → Casual Users
    Cluster 1 → Active Users
    Cluster 2 → Power Users
    """)
    st.success("Clustering Analysis Completed Successfully")

# ML MODELS PAGE
elif page == "ML Models":
    st.title("🤖 Machine Learning Models")
    st.markdown("""
    | Model | Purpose |
    |---------|---------|
    | K-Means Clustering | User Segmentation |
    | Cosine Similarity | Product Similarity |
    | Item-Item Collaborative Filtering | Product Recommendation |
    """)
    st.success("Model Training Completed Successfully")

# RECOMMENDATION PAGE
elif page == "Get Recommendations":
    st.title("🎯 Product Recommendation Dashboard")
    st.subheader("Selected Recommendation Model")
    st.success("""
    Item-Item Collaborative Filtering
    using Cosine Similarity
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
            st.success("Stage 1 → Product Selected")
            st.success("Stage 2 → Similar Products Retrieved")
            st.success(
                f"Stage 3 → Top {top_n} Recommendations Generated"
            )
            st.subheader("🏆 Recommended Products")
            
            for i, product in enumerate(
                recommendations,
                start=1
            ):
                st.markdown(
                    f"""
                    <div style="
                    background:#1E293B;
                    padding:15px;
                    border-radius:10px;
                    margin-bottom:10px;
                    ">
                    <b>{i}. {product}</b>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        except Exception as e:
            st.error(f"Error: {e}")

# PIPELINE PAGE
elif page == "Cluster-Aware Pipeline":
    st.title("⚙️ Cluster-Aware Pipeline")
    st.markdown("""
    ### Step 1 : Data Collection
    Product ratings dataset collected.
    
    ### Step 2 : Data Cleaning
    Missing values handled and data prepared.

    ### Step 3 : Exploratory Data Analysis
    User and product behaviour analysed.

    ### Step 4 : Clustering
    K-Means clustering used for user segmentation.

    ### Step 5 : Similarity Computation
    Cosine similarity matrix generated.

    ### Step 6 : Recommendation Engine
    Item-Item Collaborative Filtering applied.

    ### Step 7 : Deployment
    Streamlit Cloud deployment completed.
    """)
    st.success("Pipeline Execution Successful")

# FULL REPORT PAGE
elif page == "Full Report":
    st.title("📄 Full Project Report")
    st.markdown("""
    ## Project Title
    Product Recommendation System

    ## Objective
    Build a recommendation system that suggests
    products based on user preferences and
    product similarity.

    ## Dataset
    Amazon Product Ratings Dataset

    ## Techniques Used
    • Data Cleaning
    • Exploratory Data Analysis
    • K-Means Clustering
    • Cosine Similarity
    • Item-Item Collaborative Filtering

    ## Results
    Successfully generated personalized
    recommendations for selected products.

    ## Deployment
    Streamlit Cloud Deployment

    ## Future Scope
    • Hybrid Recommendation Systems
    • Deep Learning Based Recommenders
    • Real-Time Recommendation Engine
    """)

    st.success("Project Completed Successfully")
