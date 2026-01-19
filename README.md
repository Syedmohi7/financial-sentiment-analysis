# 📊 Financial Sentiment Analysis & Market Dashboard

## 📌 Overview

This project analyzes how **financial news sentiment** influences **short-term stock price movement** using **Data Science, NLP, and Machine Learning**.

I built this project end-to-end — from data collection to an **interactive dashboard** — to understand how real-world financial analytics systems are designed.

---

## 🎯 Why This Project

Stock prices are not driven only by numbers.
News, market sentiment, and investor psychology also play a major role.

This project answers:

* Can we convert financial news into numerical signals?
* Does sentiment show any relationship with price movement?
* How can analytics support better decision-making?

---

## 🏢 Use Case

* Investment research
* Risk monitoring
* Market sentiment tracking
* Financial analytics dashboards

---

## 📈 Stock Details

* **Company:** Reliance Industries
* **Market:** NSE (India)
* **Data Period:** Last 1 Year
* **Frequency:** Daily
* **Prediction Task:** Next-day price direction (Up / Down)

---

## 🧠 What I Built (Simple Explanation)

### 1️⃣ Data Collection

* Collected real stock price data using Yahoo Finance
* Prepared a structured dataset of financial news headlines

### 2️⃣ Data Cleaning

* Handled missing values
* Aligned sentiment data with trading days
* Maintained raw and processed data layers

### 3️⃣ Sentiment Analysis (NLP)

* Cleaned news text using NLP techniques
* Applied VADER sentiment analysis
* Classified sentiment as Positive, Negative, or Neutral

### 4️⃣ Feature Engineering

* Daily sentiment aggregation
* Lagged sentiment features
* Rolling sentiment averages

### 5️⃣ Machine Learning

* Framed problem as binary classification
* Built Logistic Regression as a baseline model
* Used time-series-aware train-test split

### 6️⃣ Interactive Dashboard

* Built a **Streamlit dashboard** for visualization
* Added KPI cards and clean time-series charts
* Focused on UX and readability

---

## 📊 Key Insights

* Negative sentiment often appears before short-term price drops
* Positive sentiment supports upward price movement
* Sentiment is noisy but useful as a **risk indicator**
* Best used along with price data, not alone

---

## 💼 Business Value

* Converts unstructured news into measurable insights
* Helps identify potential downside risk early
* Reduces manual news monitoring
* Scalable for real-time market analysis

---

## ⚠️ Limitations

* Limited news volume in prototype stage
* Market prices depend on many external factors
* Not intended for live trading

---

## 🚀 Future Improvements

* Real-time news API integration
* Advanced NLP models (BERT)
* More technical indicators
* Multi-stock and sector-level analysis
* Cloud deployment of dashboard

---

## 🛠 Tech Stack

* Python
* Pandas, NumPy
* NLP: NLTK, VADER
* Machine Learning: Scikit-learn
* Visualization & Dashboard: Streamlit, Altair

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

---

## ✨ Final Note

This project reflects my approach to data problems:
**clean data → clear analysis → simple models → meaningful insights**.

---

### ⭐ If you like this project, feel free to give it a star!


Just tell me 👍
