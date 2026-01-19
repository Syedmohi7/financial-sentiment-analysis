import streamlit as st
import pandas as pd
import altair as alt

# =====================================================
# PAGE CONFIG (UX FIRST)
# =====================================================
st.set_page_config(
    page_title="Market Sentiment Dashboard",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================
stock_df = pd.read_csv("Data/processed/reliance_stock_cleaned.csv")
sentiment_df = pd.read_csv("Data/processed/reliance_daily_sentiment.csv")

stock_df["Date"] = pd.to_datetime(stock_df["Date"])
sentiment_df["date"] = pd.to_datetime(sentiment_df["date"])

df = pd.merge(
    stock_df,
    sentiment_df,
    left_on="Date",
    right_on="date",
    how="left"
).fillna(0)

# =====================================================
# HEADER
# =====================================================
st.markdown(
    """
    <h1 style="color:#0B132B;">📊 Financial Market Sentiment Intelligence</h1>
    <h4 style="color:#1C2541;">Reliance Industries • NSE • Interactive Dashboard</h4>
    """,
    unsafe_allow_html=True
)

st.markdown("<hr>", unsafe_allow_html=True)

# =====================================================
# KPI CARDS (PREMIUM COLORS)
# =====================================================
k1, k2, k3, k4 = st.columns(4)

k1.markdown(
    "<div style='background:#E0F2FE;padding:20px;border-radius:12px;'>"
    "<h4>📅 Trading Days</h4>"
    f"<h2>{df.shape[0]}</h2></div>",
    unsafe_allow_html=True
)

k2.markdown(
    "<div style='background:#DCFCE7;padding:20px;border-radius:12px;'>"
    "<h4>🧠 Avg Sentiment</h4>"
    f"<h2>{round(df['avg_sentiment_score'].mean(),3)}</h2></div>",
    unsafe_allow_html=True
)

k3.markdown(
    "<div style='background:#FEF3C7;padding:20px;border-radius:12px;'>"
    "<h4>🟢 Positive Days</h4>"
    f"<h2>{int((df['avg_sentiment_score']>0).sum())}</h2></div>",
    unsafe_allow_html=True
)

k4.markdown(
    "<div style='background:#FEE2E2;padding:20px;border-radius:12px;'>"
    "<h4>🔴 Negative Days</h4>"
    f"<h2>{int((df['avg_sentiment_score']<0).sum())}</h2></div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# STOCK PRICE CHART (CLEAR & BOLD)
# =====================================================
st.subheader("📈 Stock Price Trend")

price_chart = alt.Chart(df).mark_line(
    color="#2563EB",
    strokeWidth=4
).encode(
    x=alt.X(
        "Date:T",
        title="Date",
        axis=alt.Axis(
            labelAngle=-45,
            labelFontSize=12,
            titleFontSize=14
        )
    ),
    y=alt.Y(
        "Close:Q",
        title="Close Price (₹)",
        scale=alt.Scale(zero=False),
        axis=alt.Axis(
            labelFontSize=12,
            titleFontSize=14
        )
    ),
    tooltip=[
        alt.Tooltip("Date:T", title="Date"),
        alt.Tooltip("Close:Q", title="Close Price")
    ]
).properties(
    height=380
).interactive()

st.altair_chart(price_chart, use_container_width=True)

# =====================================================
# SENTIMENT CHART (COLORFUL & READABLE)
# =====================================================
st.subheader("🧠 Market Sentiment Trend")

sentiment_chart = alt.Chart(df).mark_area(
    interpolate="monotone",
    line={"color": "#16A34A", "strokeWidth": 3},
    color=alt.Gradient(
        gradient="linear",
        stops=[
            alt.GradientStop(color="#BBF7D0", offset=0),
            alt.GradientStop(color="#16A34A", offset=1)
        ],
        x1=1, x2=1, y1=1, y2=0
    )
).encode(
    x=alt.X(
        "Date:T",
        title="Date",
        axis=alt.Axis(
            labelAngle=-45,
            labelFontSize=12,
            titleFontSize=14
        )
    ),
    y=alt.Y(
        "avg_sentiment_score:Q",
        title="Sentiment Score",
        scale=alt.Scale(domain=[-1, 1]),
        axis=alt.Axis(
            labelFontSize=12,
            titleFontSize=14
        )
    ),
    tooltip=[
        alt.Tooltip("Date:T", title="Date"),
        alt.Tooltip("avg_sentiment_score:Q", title="Sentiment")
    ]
).properties(
    height=320
).interactive()

st.altair_chart(sentiment_chart, use_container_width=True)

# =====================================================
# INSIGHTS
# =====================================================
st.markdown("## 🔍 Key Insights")

st.info(
    "• Negative sentiment often appears before short-term price drops.\n"
    "• Positive sentiment supports upward momentum.\n"
    "• Sentiment works best as a **risk indicator**, not a standalone predictor."
)

# =====================================================
# FOOTER
# =====================================================
st.markdown(
    "<center style='color:#475569;'>Built with Python • Streamlit • Altair • NLP</center>",
    unsafe_allow_html=True
)
