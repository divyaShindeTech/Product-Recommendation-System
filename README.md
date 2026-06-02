# Product Recommendation System

## Project Overview:
E-commerce companies use recommendation systems to provide suggestions to customers. They commonly use Item-Item Collaborative Filtering, which scales efficiently to massive datasets and produces high-quality recommendations in real time.
This recommendation system is an information filtering system that predicts the ratings or preferences a user may have for products based on historical user-product interactions.
The project also explores multiple clustering techniques and performs a comparative analysis to identify the most suitable clustering approach for recommendation tasks.

## Project Objectives:
 Perform Exploratory Data Analysis (EDA)
 Clean and preprocess the dataset
 Apply multiple clustering algorithms
 Compare clustering model performance
 Build a recommendation system using collaborative filtering
 Deploy the recommendation application using Streamlit

## Dataset Information:
Attributes used:
 userId – Unique user identifier
 productId – Unique product identifier
 Rating – User rating for a product
 timestamp – Ignored for recommendation modeling
Dataset Size:
  7.8+ Million Ratings
  Large-scale Amazon Product Dataset

## Exploratory Data Analysis:
The following analyses were performed:
  Dataset structure inspection
  Missing value analysis
  Duplicate value analysis
  Rating distribution analysis
  Ratings per user analysis
  Ratings per product analysis
  Top-rated products analysis

## Clustering Models Implemented:
### 1. K-Means Clustering:
  User segmentation based on rating behavior
  Cluster visualization and analysis

### 2. Hierarchical Clustering:
  Dendrogram-based cluster formation
  Cluster interpretation and evaluation

### 3. DBSCAN Clustering:
 Density-based clustering
 Noise and outlier detection

## Comparative Analysis:
The clustering models were compared using:
  Number of clusters
  Silhouette Score
  Cluster quality
  Interpretability
Based on the analysis, the best-performing clustering approach was selected for recommendation modeling.

## Recommendation System: 
### Item-Item Collaborative Filtering:
The recommendation engine uses:
  User-Product Matrix
  Cosine Similarity
  Product Similarity Matrix
Products are recommended based on similarity scores between items.

## Additional Recommendation Models:
 Popularity-Based Recommendation
 Cluster-Based Collaborative Filtering
 SVD (Singular Value Decomposition)

## Technologies Used:
 Python
 Pandas
 NumPy
 Matplotlib
 Seaborn
 Scikit-Learn
 Streamlit
 Pickle

## Project Structure:
Product-Recommendation-System/
│
├── app.py
├── product_similarity.pkl.gz
├── product_ids.pkl
├── requirements.txt
├── Product_Recommendation_System.ipynb
└── README.md


## Deployment:
The recommendation application is deployed using Streamlit.
Users can:
  Select a product
  Generate recommendations
  View similar products instantly

## Results:
 Successfully implemented three clustering algorithms
 Performed comparative analysis of clustering methods
 Built an item-item collaborative filtering recommendation engine
 Developed a deployable Streamlit application

## Author:
Data Science & Machine Learning Project
Product Recommendation System
