import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# Base Directory
# ----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------
# Load Dataset
# ----------------------------

@st.cache_data
def load_data():
    df = pd.read_csv(BASE_DIR / "test_clean.csv")
    return df

df = load_data()

st.title("📊 E-Commerce Return Risk Dashboard")

st.markdown("---")

# ----------------------------
# Sidebar Filters
# ----------------------------

st.sidebar.header("Dashboard Filters")

membership = st.sidebar.multiselect(
    "Membership Type",
    options=sorted(df["membership_type"].unique()),
    default=sorted(df["membership_type"].unique())
)

category = st.sidebar.multiselect(
    "Category",
    options=sorted(df["category"].unique()),
    default=sorted(df["category"].unique())
)

payment = st.sidebar.multiselect(
    "Payment Method",
    options=sorted(df["payment_method"].unique()),
    default=sorted(df["payment_method"].unique())
)

sentiment = st.sidebar.multiselect(
    "Customer Sentiment",
    options=sorted(df["sentiment"].unique()),
    default=sorted(df["sentiment"].unique())
)

df = df[
    (df["membership_type"].isin(membership)) &
    (df["category"].isin(category)) &
    (df["payment_method"].isin(payment)) &
    (df["sentiment"].isin(sentiment))
]

# ----------------------------
# KPI Cards
# ----------------------------

st.subheader("📌 Key Performance Indicators")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Customers",
        df["customer_id"].nunique()
    )

with c2:
    st.metric(
        "Orders",
        len(df)
    )

with c3:
    st.metric(
        "Fraud Returns",
        int(df["fraud_label"].sum())
    )

with c4:
    fraud_rate = (df["fraud_label"].mean()) * 100

    st.metric(
        "Fraud Rate",
        f"{fraud_rate:.2f}%"
    )

st.markdown("---")

# ----------------------------
# Business KPIs
# ----------------------------

st.subheader("💰 Business Metrics")

a, b, c, d = st.columns(4)

with a:

    st.metric(
        "Lifetime Spend",
        f"₹ {df['lifetime_spend'].mean():,.0f}"
    )

with b:

    st.metric(
        "Average Order Value",
        f"₹ {df['average_order_value'].mean():,.0f}"
    )

with c:

    st.metric(
        "Average Return Rate",
        f"{df['return_rate'].mean()*100:.2f}%"
    )

with d:

    st.metric(
        "Purchase Frequency",
        f"{df['purchase_frequency'].mean():.2f}"
    )

st.markdown("---")

st.subheader("🛡 Fraud Analysis")

left, right = st.columns(2)

with left:

    fraud = df["fraud_label"].value_counts().reset_index()

    fraud.columns = ["Status", "Count"]

    fraud["Status"] = fraud["Status"].replace({
        0: "Genuine",
        1: "Fraud"
    })

    fig = px.pie(
        fraud,
        names="Status",
        values="Count",
        hole=.45,
        title="Fraud vs Genuine Returns"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    fraud_payment = df.groupby(
        "payment_method"
    )["fraud_label"].sum().reset_index()

    fig = px.bar(
        fraud_payment,
        x="payment_method",
        y="fraud_label",
        color="payment_method",
        title="Fraud by Payment Method"
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("👥 Customer Analysis")

c1, c2 = st.columns(2)

with c1:

    fig = px.pie(
        df,
        names="membership_type",
        hole=.4,
        title="Membership Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with c2:

    spend = df.groupby(
        "membership_type"
    )["lifetime_spend"].mean().reset_index()

    fig = px.bar(
        spend,
        x="membership_type",
        y="lifetime_spend",
        color="membership_type",
        title="Average Lifetime Spend"
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

left, right = st.columns(2)

with left:

    category = df["category"].value_counts().reset_index()

    category.columns = ["Category", "Orders"]

    fig = px.bar(
        category,
        x="Category",
        y="Orders",
        color="Category"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    fraud_category = df.groupby(
        "category"
    )["fraud_label"].sum().reset_index()

    fig = px.bar(
        fraud_category,
        x="category",
        y="fraud_label",
        color="category",
        title="Fraud by Category"
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ---------------------------------
# Monthly Trend
# ---------------------------------

st.subheader("📈 Monthly Order Trend")

df['order_date'] = pd.to_datetime(df['order_date'])

df['Month'] = df['order_date'].dt.to_period('M').astype(str)

monthly_orders = df.groupby('Month').size().reset_index(name='Orders')

fig = px.line(
    monthly_orders,
    x='Month',
    y='Orders',
    markers=True,
    title='Monthly Orders'
)

st.plotly_chart(fig,use_container_width=True)

st.markdown("---")

# ---------------------------------
# Monthly Fraud Trend
# ---------------------------------

monthly_fraud = df.groupby('Month')['fraud_label'].sum().reset_index()

fig = px.line(
    monthly_fraud,
    x='Month',
    y='fraud_label',
    markers=True,
    title='Monthly Fraud Returns'
)

st.plotly_chart(fig,use_container_width=True)

st.markdown("---")

st.subheader("📦 Return Analysis")

c1,c2=st.columns(2)

with c1:

    reason=df['return_reason'].value_counts().reset_index()

    reason.columns=['Reason','Count']

    fig=px.bar(
        reason,
        x='Reason',
        y='Count',
        color='Reason',
        title='Return Reasons'
    )

    st.plotly_chart(fig,use_container_width=True)

with c2:

    fig=px.box(
        df,
        x='membership_type',
        y='return_days',
        color='membership_type',
        title='Return Days'
    )

    st.plotly_chart(fig,use_container_width=True)

st.markdown("---")

st.subheader("🏷 Brand Analysis")

c1,c2=st.columns(2)

with c1:

    brand=df['brand'].value_counts().reset_index().head(10)

    brand.columns=['Brand','Orders']

    fig=px.bar(
        brand,
        x='Brand',
        y='Orders',
        color='Orders',
        title='Top 10 Brands'
    )

    st.plotly_chart(fig,use_container_width=True)

with c2:

    fraud_brand=df.groupby('brand')['fraud_label'].sum().reset_index()

    fraud_brand=fraud_brand.sort_values(
        by='fraud_label',
        ascending=False
    ).head(10)

    fig=px.bar(
        fraud_brand,
        x='brand',
        y='fraud_label',
        color='fraud_label',
        title='Top Fraud Brands'
    )

    st.plotly_chart(fig,use_container_width=True)

st.markdown("---")

st.subheader("⭐ Customer Behaviour")

left,right=st.columns(2)

with left:

    fig=px.scatter(
        df,
        x='purchase_frequency',
        y='lifetime_spend',
        color='membership_type',
        title='Purchase Frequency vs Lifetime Spend'
    )

    st.plotly_chart(fig,use_container_width=True)

with right:

    fig=px.scatter(
        df,
        x='total_orders',
        y='total_returns',
        color='fraud_label',
        title='Orders vs Returns'
    )

    st.plotly_chart(fig,use_container_width=True)

st.markdown("---")

st.subheader("💰 Refund Analysis")

left,right=st.columns(2)

with left:

    fig=px.histogram(
        df,
        x='refund_amount',
        nbins=30,
        title='Refund Amount Distribution'
    )

    st.plotly_chart(fig,use_container_width=True)

with right:

    refund=df.groupby('membership_type')['refund_amount'].mean().reset_index()

    fig=px.bar(
        refund,
        x='membership_type',
        y='refund_amount',
        color='membership_type',
        title='Average Refund Amount'
    )

    st.plotly_chart(fig,use_container_width=True)

st.markdown("---")

st.subheader("📄 Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)
