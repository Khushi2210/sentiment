import streamlit as st
import pandas as pd
from PIL import Image
import os

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Trader Performance vs Market Sentiment",
    layout="wide"
)

st.title("📊 Trader Performance vs Market Sentiment")
st.markdown(
    """
    This dashboard presents insights from the analysis of **trader behavior and performance**
    in relation to **Bitcoin market sentiment (Fear/Greed Index)**.
    """
)

# ----------------------------
# Helper Functions
# ----------------------------
def load_image(path):
    if os.path.exists(path):
        return Image.open(path)
    else:
        st.warning(f"Image not found: {path}")
        return None

def load_csv(path):
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        st.warning(f"File not found: {path}")
        return None

# ----------------------------
# Sidebar Navigation
# ----------------------------
st.sidebar.title("📌 Navigation")
section = st.sidebar.radio(
    "Go to section:",
    [
        "Overview",
        "Market Sentiment Analysis",
        "Trading Activity Analysis",
        "Fear vs Greed Comparison",
        "Trader Clustering",
        "Processed Data"
    ]
)

# ----------------------------
# Overview
# ----------------------------
if section == "Overview":
    st.subheader("🔍 Project Overview")
    st.markdown(
        """
        **Objective:**  
        Analyze how market sentiment (Fear vs Greed) affects trader behavior and performance
        on the Hyperliquid trading platform.

        **Key Focus Areas:**
        - Profitability (PnL, win rate)
        - Trading behavior (frequency, size, leverage)
        - Trader segmentation and clustering
        """
    )

# ----------------------------
# Market Sentiment Analysis
# ----------------------------
elif section == "Market Sentiment Analysis":
    st.subheader("📈 Market Sentiment Analysis")

    col1, col2 = st.columns(2)

    with col1:
        img = load_image("outputs/fear_greed_analysis.png")
        if img:
            st.image(img, caption="Fear & Greed Index Over Time")

    with col2:
        img = load_image("outputs/sentiment_distribution.png")
        if img:
            st.image(img, caption="Market Sentiment Distribution")

# ----------------------------
# Trading Activity Analysis
# ----------------------------
elif section == "Trading Activity Analysis":
    st.subheader("📊 Trading Activity Overview")

    img = load_image("outputs/trading_activity_analysis.png")
    if img:
        st.image(img, width=900)

# ----------------------------
# Fear vs Greed Comparison
# ----------------------------
elif section == "Fear vs Greed Comparison":
    st.subheader("⚖️ Trader Performance: Fear vs Neutral vs Greed")

    img = load_image("outputs/fear_vs_greed_comparison.png")
    if img:
        st.image(img, use_container_width=True)

# ----------------------------
# Trader Clustering
# ----------------------------
elif section == "Trader Clustering":
    st.subheader("🧩 Trader Clustering & Segmentation")

    img = load_image("outputs/cluster_optimization.png")
    if img:
        st.image(img, caption="Elbow Method & Silhouette Scores")

# ----------------------------
# Processed Data Section
# ----------------------------
elif section == "Processed Data":
    st.subheader("📁 Processed & Exported Datasets")

    file_options = {
        "Daily Trader Metrics": "processed_data/daily_trader_metrics.csv",
        "Account Clusters": "processed_data/account_clusters.csv",
        "Sentiment Performance Summary": "processed_data/sentiment_performance_summary.csv",
        "Cluster Profiles": "processed_data/cluster_profiles.csv",
    }

    selected_file = st.selectbox(
        "Select a dataset to view:",
        list(file_options.keys())
    )

    df = load_csv(file_options[selected_file])
    if df is not None:
        st.dataframe(df, use_container_width=True)
        st.markdown(f"**Rows:** {df.shape[0]} &nbsp;&nbsp; | &nbsp;&nbsp; **Columns:** {df.shape[1]}")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("Data Science Intern Assignment – Trader Performance vs Market Sentiment")
