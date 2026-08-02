# 🛍️ Product Recommendation System
> A machine learning-based Product Recommendation System using Item-Item Collaborative Filtering, Clustering Techniques, and Similarity-Based Recommendations, deployed as an interactive Streamlit application.

## 🌟 Project Overview
E-commerce platforms use recommendation systems to help customers discover relevant products based on their preferences and previous interactions.
This project develops a Product Recommendation System that analyzes historical user-product ratings to identify similar products and generate personalized recommendations.
The project also explores and compares multiple clustering algorithms to understand user behavior and identify suitable clustering approaches for recommendation-related tasks.
The final recommendation application is deployed using Streamlit, allowing users to select a product and receive similar product recommendations through an interactive interface.


## 🎯 Project Objectives
* 📊 Perform Exploratory Data Analysis (EDA)
* 🧹 Clean and preprocess large-scale rating data
* 🔍 Analyze user-product interaction patterns
* 🤖 Apply multiple clustering algorithms
* 📈 Compare clustering model performance
* 🔄 Build an Item-Item Collaborative Filtering recommendation engine
* 🧠 Explore additional recommendation techniques
* 🚀 Deploy the recommendation system using Streamlit


## 📂 Dataset Information
The project uses a large-scale product ratings dataset containing historical user-product interactions.

### 📌 Dataset Attributes

| Feature     | Description                               |
| ----------- | ----------------------------------------- |
| `userId`    | Unique identifier for each user           |
| `productId` | Unique identifier for each product        |
| `Rating`    | User rating given to a product            |
| `timestamp` | Timestamp of the user-product interaction |

### 📊 Dataset Size
* **7.8+ Million Ratings**
* Large-scale product rating dataset
* **Timestamp** was excluded from recommendation modeling

## 🔎 Exploratory Data Analysis (EDA)
The following analyses were performed to understand the dataset and user-product interactions:
* 📋 Dataset structure and information
* ❓ Missing value analysis
* ♻️ Duplicate value analysis
* ⭐ Rating distribution analysis
* 👤 Ratings per user analysis
* 🛍️ Ratings per product analysis
* 🏆 Top-rated products analysis
* 📊 User-product interaction analysis


## 🤖 Clustering Models Implemented

### 1️⃣ K-Means Clustering
Used to analyze and segment users based on their rating behavior.

**Key Activities:**
* User segmentation
* Cluster formation
* Cluster visualization
* Cluster behavior analysis

### 2️⃣ Hierarchical Clustering
Applied hierarchical clustering techniques to identify relationships between user groups.

**Key Activities:**

* Dendrogram-based analysis
* Cluster formation
* Cluster interpretation
* Cluster evaluation


### 3️⃣ DBSCAN Clustering
A density-based clustering algorithm used to identify groups and detect potential noise or outliers.

**Key Activities:**
* Density-based clustering
* Noise detection
* Outlier identification
* Cluster analysis

## 📊 Clustering Model Comparison
The clustering algorithms were compared based on:
* Number of clusters
* Silhouette Score
* Cluster quality
* Interpretability
* Ability to identify meaningful user segments
The comparative analysis helped identify the most suitable clustering approach for understanding user behavior within the recommendation workflow.

## 🧠 Recommendation System
### 🔄 Item-Item Collaborative Filtering
The primary recommendation engine uses Item-Item Collaborative Filtering to identify products that are similar based on user rating patterns.

### ⚙️ Recommendation Workflow

```text
User-Product Ratings
        ↓
Data Preprocessing
        ↓
User-Product Matrix
        ↓
Calculate Product Similarity
        ↓
Cosine Similarity
        ↓
Product Similarity Matrix
        ↓
Generate Similar Product Recommendations
```

### 🔑 Core Components
* User-Product Matrix
* Cosine Similarity
* Product Similarity Matrix
* Similarity-based product recommendations
The system recommends products by identifying items with similar rating patterns and similarity scores.

## 🧪 Additional Recommendation Techniques
The project also explores different recommendation approaches:
* ⭐ **Popularity-Based Recommendation**
* 👥 **Cluster-Based Collaborative Filtering**
* 🧮 **SVD (Singular Value Decomposition)**
These approaches were explored for comparative analysis and understanding different recommendation strategies.


## 🛠️ Technologies & Tools

| Category            | Technologies        |
| ------------------- | ------------------- |
| 🐍 Programming      | Python              |
| 📊 Data Analysis    | Pandas, NumPy       |
| 📈 Visualization    | Matplotlib, Seaborn |
| 🤖 Machine Learning | Scikit-learn        |
| 🌐 Deployment       | Streamlit           |
| 💾 Model Storage    | Pickle              |
| 📓 Development      | Jupyter Notebook    |


## 📁 Project Structure

```text
Product-Recommendation-System/
│
├── 📄 app.py
├── 📦 product_similarity.pkl.gz
├── 📦 product_ids.pkl
├── 📄 requirements.txt
├── 📓 Product_Recommendation_System.ipynb
└── 📖 README.md
```

## 🚀 Deployment
The recommendation system is deployed using Streamlit and provides an interactive user interface.
### 👤 Users Can:
1. 🛍️ Select a product
2. 🔍 Generate similar product recommendations
3. 📋 View recommended products
4. ⚡ Get recommendations through an interactive application

## 📈 Project Results
✅ Successfully performed EDA on a large-scale product rating dataset
✅ Implemented and analyzed K-Means, Hierarchical, and DBSCAN clustering
✅ Performed comparative analysis of clustering approaches
✅ Built an Item-Item Collaborative Filtering recommendation engine
✅ Implemented similarity-based product recommendations using Cosine Similarity
✅ Explored additional recommendation techniques including Popularity-Based, Cluster-Based, and SVD approaches
✅ Developed an interactive Streamlit recommendation application

## 💡 Key Learnings
Through this project, I gained practical experience in:
* Working with large-scale datasets
* Data preprocessing and exploratory data analysis
* Recommendation system fundamentals
* Collaborative filtering techniques
* Similarity-based recommendation
* Clustering and comparative model analysis
* Machine learning workflow development
* Streamlit application deployment

## 👩‍💻 Author
### **Divya Shinde**

Aspiring Data Scientist | Python | Machine Learning | Data Analytics
🔗 GitHub: `divyaShindeTech`

## ⭐ Support
If you found this project interesting or useful, consider giving the repository a ⭐ **Star** and sharing your feedback!

> ⚠️ **Disclaimer:** This project is created for educational and portfolio purposes to demonstrate the implementation of recommendation systems and machine learning techniques.
