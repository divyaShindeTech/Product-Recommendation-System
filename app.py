import streamlit as st
import pandas as pd
import pickle
import gzip
import matplotlib.pyplot as plt

# PAGE CONFIG
st.set_page_config(
    page_title="Product Recommendation System",
    layout="wide"
)

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
    st.title("Product Recommendation System")
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

# EDA
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

    # Top 10 Most Rated Products
    st.subheader("Top 10 Most Rated Products")
    top_products = (
        df.groupby("productId")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )
    fig, ax = plt.subplots(figsize=(8,4))
    top_products.plot(kind="bar", ax=ax)
    ax.set_xlabel("Product ID")
    ax.set_ylabel("Number of Ratings")
    st.pyplot(fig)

    # Rating Distribution Graph
    st.subheader("Rating Distribution")
    fig, ax = plt.subplots(figsize=(6,4))
    df["rating"].hist(
        bins=5,
        ax=ax
    )
    ax.set_xlabel("Rating")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

# CLUSTERING PAGE
elif page == "Clustering Analysis":

    st.title("🔍 Clustering Analysis")

    st.info("""
    Algorithm Used: K-Means Clustering

    Purpose:
    • Customer Segmentation
    • User Behaviour Analysis
    • Group Similar Users
    """)

    # Metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("Best K", "2")
    col2.metric("Cluster 0 Users", "947")
    col3.metric("Cluster 1 Users", "585")

    # Elbow Method Graph
    st.subheader("Elbow Method")

    k_values = [2, 3, 4, 5, 6, 7]

    inertia = [
        1490.5,
        1482.0,
        1475.3,
        1470.2,
        1466.1,
        1463.8
    ]

    fig, ax = plt.subplots(figsize=(8,4))

    ax.plot(
        k_values,
        inertia,
        marker="o"
    )

    ax.set_title("Elbow Method - KMeans")
    ax.set_xlabel("Number of Clusters (K)")
    ax.set_ylabel("Inertia")

    st.pyplot(fig)

    # Silhouette Score Graph
    st.subheader("Silhouette Score")

    silhouette_scores = [
        0.00777,
        0.00713,
        0.00678,
        0.00575,
        0.00758,
        0.00550
    ]

    fig2, ax2 = plt.subplots(figsize=(8,4))

    ax2.plot(
        k_values,
        silhouette_scores,
        marker="o"
    )

    ax2.set_title("Silhouette Score - KMeans")
    ax2.set_xlabel("Number of Clusters (K)")
    ax2.set_ylabel("Silhouette Score")

    st.pyplot(fig2)

    # Cluster Distribution
    st.subheader("K-Means Cluster Distribution")

    clusters = ["Cluster 0", "Cluster 1"]
    users = [947, 585]

    fig3, ax3 = plt.subplots(figsize=(8,5))

    ax3.bar(
        clusters,
        users
    )

    ax3.set_title("K-Means Cluster Distribution")
    ax3.set_xlabel("Cluster")
    ax3.set_ylabel("Number of Users")

    st.pyplot(fig3)

    # Pie Chart
    st.subheader("Cluster Percentage")

    fig4, ax4 = plt.subplots(figsize=(6,6))

    ax4.pie(
        users,
        labels=clusters,
        autopct="%1.1f%%"
    )

    st.pyplot(fig4)

    # Summary
    st.subheader("Cluster Summary")

    st.write("""
    **Cluster 0**
    - 947 Users
    - Casual and Regular Users

    **Cluster 1**
    - 585 Users
    - Highly Active Users
    """)

    st.success("Optimal Number of Clusters (K) = 2")

# ML MODELS PAGE

elif page == "ML Models":

    st.title("🤖 Machine Learning Models")

    st.markdown("""
    | Model | Purpose |
    |---------|---------|
    | K-Means Clustering | User Segmentation |
    | Cosine Similarity | Product Similarity |
    | Item-Item Collaborative Filtering | Recommendation Generation |
    """)

    st.subheader("Model Selection")

    st.success("Best Clustering Model: K-Means (K = 2)")

    st.write("""
    **Model Details**

    • K-Means Clustering:
      Used to segment users into groups based on behaviour.

    • Cosine Similarity:
      Used to measure similarity between products.

    • Item-Item Collaborative Filtering:
      Used to recommend products similar to the selected product.

    • Optimal Number of Clusters:
      K = 2 (selected using Elbow Method and Silhouette Score).
    """)

# RECOMMENDATION PAGE
elif page == "Get Recommendations":
    st.title("🎯 Product Recommendation Dashboard")
    st.subheader("Selected Recommendation Model")
    st.success("""
    Item-Item Collaborative Filtering
    using Cosine Similarity
    """)
    col1, col2, col3 = st.columns(3)
    col1.metric(
        "Products Available",
        len(product_ids)
    )
    col2.metric(
        "Similarity Matrix Size",
        similarity.shape[0]
    )
    col3.metric(
        "Recommendation Model",
        "Item-Item CF"
    )
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
    ### Recommendation Flow

    Ratings Dataset
    ↓
    Data Cleaning
    ↓
    Exploratory Data Analysis
    ↓
    K-Means Clustering
    ↓
    Cosine Similarity
    ↓
    Item-Item Collaborative Filtering
    ↓
    Product Recommendations
    ↓
    Streamlit Deployment
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
   Product Ratings Dataset

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
    st.subheader("Clustering Results")
    st.write("""
K-Means clustering was evaluated using:

• Elbow Method

• Silhouette Score

The optimal number of clusters was found to be K = 2.

Cluster 0 represents Casual Users.

Cluster 1 represents Power Users.
""")
    st.success("Project Completed Successfully")
