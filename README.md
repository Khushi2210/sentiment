# Bitcoin Market Sentiment & Trader Behavior Analysis

## Overview

This project analyzes the relationship between Bitcoin market sentiment (Fear/Greed Index) and trader behavior & performance on the Hyperliquid platform. The goal is to understand how market sentiment impacts trading outcomes and to derive actionable strategy insights from historical data.

The complete analysis is implemented in a single Jupyter Notebook, supported by generated datasets and visual outputs.

---

## Repository Structure

```
├── analysis.ipynb              # Main notebook with data preparation, analysis & insights
├── app.py                      # Streamlit dashboard application
├── processed_data/             # Cleaned and feature-engineered datasets (generated)
├── outputs/                    # Charts, plots, and tables generated from analysis
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation

```

- **outputs/** contains all saved images and visualizations used to support insights
- **processed_data/** contains intermediate and final datasets created during preprocessing

---

## Datasets Used

###1) Bitcoin Market Sentiment (Fear/Greed)
Columns: Date, Classification (Fear / Greed)
Link: https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=sharing

###2) Historical Trader Data (Hyperliquid)
Includes fields like: account, symbol, execution price, size, side, time, start position, event, closedPnL, leverage, etc.
Link: https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=sharing

---

## Key Analysis Performed

### Data Preparation
- ✅ Checked rows, columns, missing values, and duplicates
- ✅ Converted timestamps and aligned datasets by date
- ✅ Created key performance and behavioral metrics:
  - Daily PnL per trader
  - Win rate
  - Trade frequency
  - Leverage distribution
  - Long/short ratio
  - Drawdown proxy
  - Position sizing patterns

### Analysis Components

1. **Sentiment Impact Analysis**
   - Compared trader performance on Fear vs Greed days
   - Statistical testing (t-tests, p-values) for significance
   - Distribution analysis across sentiment categories

2. **Behavioral Pattern Recognition**
   - Studied behavioral changes based on market sentiment
   - Trade frequency variations
   - Position sizing adaptations
   - Long/short bias shifts

3. **Trader Segmentation**
   - K-means clustering to identify distinct trader types
   - Segment characteristics:
     - High vs low leverage traders
     - Frequent vs infrequent traders
     - Large vs small position traders
     - Directional bias patterns

4. **Visual Analytics**
   - All insights are supported with professional charts and tables stored in `outputs/`
   - 10+ high-resolution visualizations (300 DPI)

---

## Actionable Insights

The analysis delivers practical, data-driven insights:

1. **Sentiment-Adaptive Position Sizing**
   - Strategy for adjusting exposure based on Fear/Greed levels
   - Risk management guidelines for volatile periods

2. **Cluster-Specific Optimization**
   - Tailored recommendations for different trader segments
   - Performance improvement tactics

3. **Behavioral Best Practices**
   - Evidence-based trading rules
   - Risk-reward optimization strategies

---

## Requirements

### Python Version
- Python 3.8 or higher

### Dependencies

Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

**Main Dependencies:**
- `pandas` >= 1.3.0
- `numpy` >= 1.21.0
- `matplotlib` >= 3.4.0
- `seaborn` >= 0.11.0
- `scikit-learn` >= 0.24.0
- `scipy` >= 1.7.0
- `jupyter` >= 1.0.0
- `plotly` >= 5.0.0

---

## GitHub Setup & How to Run

### 1. Clone the repository

```bash
git clone <https://github.com/Khushi2210/sentiment>
cd <sentiment>
```

### 2. Create a virtual environment (optional but recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your datasets

Place the following files in the project root directory:
- `fear_greed_index.csv`
- `historical_data.csv`

### 5. Run the notebook

```bash
jupyter notebook
```

Open `analysis.ipynb` and run the cells sequentially from top to bottom.

---
##Running the Streamlit Dashboard

After running the notebook (to generate outputs and processed data), launch the dashboard using:

streamlit run app.py

Streamlit Dashboard Features

📊 Interactive viewing of all analysis charts from outputs/

📁 Tabular exploration of processed datasets from processed_data/

🔍 Easy navigation between sentiment analysis, performance comparison, and trader clustering

🧩 No recomputation — dashboard uses pre-generated results for fast loading

The dashboard allows reviewers to explore insights without opening the notebook, improving clarity and reproducibility.

## Project Workflow

```
Data Loading → Data Cleaning → Feature Engineering → EDA → 
Statistical Analysis → Clustering → Insights → Strategies → Export
```

### Step-by-Step Process:

1. **Data Loading & Inspection**
   - Load both datasets
   - Check data quality and structure
   
2. **Data Preprocessing**
   - Handle missing values
   - Convert timestamps
   - Merge datasets by date
   
3. **Feature Engineering**
   - Calculate performance metrics
   - Engineer behavioral indicators
   - Create aggregate statistics

4. **Exploratory Data Analysis**
   - Visualize distributions
   - Identify patterns and trends
   - Correlation analysis

5. **Comparative Analysis**
   - Fear vs Greed performance comparison
   - Statistical significance testing
   
6. **Trader Segmentation**
   - K-means clustering
   - Cluster validation
   - Profile interpretation

7. **Insights & Strategies**
   - Derive actionable insights
   - Formulate trading strategies
   - Document findings

---

## Outputs

### Generated Artifacts

All analysis outputs are automatically saved to respective directories:

#### Visualizations (`outputs/`)
- `fear_greed_analysis.png` - Market sentiment time series and distribution
- `sentiment_distribution.png` - Pie chart of sentiment categories
- `trading_activity_analysis.png` - Trading patterns overview
- `fear_vs_greed_comparison.png` - Performance metrics comparison
- `cluster_optimization.png` - Elbow and silhouette analysis
- `cluster_characteristics.png` - Trader segment profiles
- Additional supporting charts

#### Processed Data (`processed_data/`)
- `daily_trader_metrics.csv` - Daily aggregated metrics per trader
- `account_clusters.csv` - Trader segmentation results
- `sentiment_performance_summary.csv` - Performance by sentiment
- `cluster_profiles.csv` - Detailed cluster characteristics

### Results Summary

All results are fully reproducible by running the notebook end-to-end. The analysis provides:
- Statistical evidence of sentiment impact on trading
- Clear trader segmentation with actionable profiles
- Data-driven strategy recommendations
