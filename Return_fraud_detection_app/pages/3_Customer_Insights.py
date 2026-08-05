import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Customer Insights",
    page_icon="📈",
    layout="wide"
)

# ----------------------------
# Base Directory
# ----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

st.title("📈 Customer Insights")

st.markdown("""
This page provides detailed customer behaviour analysis,
risk interpretation and business recommendations generated
from the machine learning models.
""")

st.markdown("---")

# ----------------------------
# Load Dataset
# ----------------------------

@st.cache_data
def load_data():

    df = pd.read_csv(BASE_DIR / "test_clean.csv")

    return df
  
df = load_data()

st.subheader("👤 Customer Overview")

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.metric(
        "Total Customers",
        df["customer_id"].nunique()
    )

with c2:

    st.metric(
        "Average Lifetime Spend",
        f"₹ {df['lifetime_spend'].mean():,.0f}"
    )

with c3:

    st.metric(
        "Average Return Rate",
        f"{df['return_rate'].mean()*100:.2f}%"
    )

with c4:

    st.metric(
        "Average Purchase Frequency",
        round(df["purchase_frequency"].mean(),2)
    )

st.markdown("---")

st.subheader("👥 Customer Segments")

st.success("""

### 🟢 Loyal Low-Return Customers

✔ Long customer tenure

✔ Lowest return behaviour

✔ Stable purchasing pattern

✔ Excellent loyalty candidates

""")

st.warning("""

### 🟡 Active Frequent Shoppers

✔ Highest purchase frequency

✔ Moderate return behaviour

✔ Active customers

✔ Suitable for promotional campaigns

""")

st.error("""

### 🔴 High Value High Return Customers

✔ Highest spending

✔ Highest returns

✔ Highest refund value

✔ High business risk

""")

st.markdown("---")

st.subheader("🛡 Fraud Insights")

fraud = df["fraud_label"].value_counts().reset_index()

fraud.columns=["Status","Count"]

fraud["Status"]=fraud["Status"].replace({

0:"Genuine",

1:"Fraud"

})

fig=px.pie(

fraud,

names="Status",

values="Count",

hole=.45,

title="Fraud Distribution"

)

st.plotly_chart(fig,use_container_width=True)

st.markdown("---")

st.subheader("💼 Business Recommendations")

c1,c2,c3=st.columns(3)

with c1:

    st.success("""

### 🟢 Loyal Customers

Recommended Actions

✔ Loyalty Rewards

✔ Special Discounts

✔ Premium Membership

✔ Referral Programs

""")

with c2:

    st.warning("""

### 🟡 Active Customers

Recommended Actions

✔ Cross Selling

✔ Personalized Offers

✔ Product Recommendations

✔ Seasonal Promotions

""")

with c3:

    st.error("""

### 🔴 High Risk Customers

Recommended Actions

✔ Manual Verification

✔ Refund Review

✔ Product Inspection

✔ Fraud Monitoring

""")

st.markdown("---")

st.subheader("⭐ Customer Behaviour")

left,right=st.columns(2)

with left:

    fig=px.scatter(

        df,

        x="purchase_frequency",

        y="lifetime_spend",

        color="membership_type",

        size="order_amount",

        title="Purchase Frequency vs Lifetime Spend"

    )

    st.plotly_chart(fig,use_container_width=True)

with right:

    fig=px.scatter(

        df,

        x="total_orders",

        y="total_returns",

        color="fraud_label",

        title="Orders vs Returns"

    )

    st.plotly_chart(fig,use_container_width=True)

st.markdown("---")

st.subheader("💰 Revenue Analysis")

c1,c2=st.columns(2)

with c1:

    revenue=df.groupby(

        "category"

    )["order_amount"].sum().reset_index()

    fig=px.bar(

        revenue,

        x="category",

        y="order_amount",

        color="category",

        title="Revenue by Category"

    )

    st.plotly_chart(fig,use_container_width=True)

with c2:

    refund=df.groupby(

        "category"

    )["refund_amount"].sum().reset_index()

    fig=px.bar(

        refund,

        x="category",

        y="refund_amount",

        color="category",

        title="Refund Amount by Category"

    )

    st.plotly_chart(fig,use_container_width=True)

st.markdown("---")

st.subheader("⚠ High Risk Indicators")

risk=pd.DataFrame({

"Indicator":[

"High Return Rate",

"Frequent Returns",

"High Refund Amount",

"Repeated Complaints",

"Packaging Damage",

"Scratches",

"Missing Tags"

],

"Business Impact":[

"High",

"High",

"Medium",

"Medium",

"Medium",

"Medium",

"Low"

]

})

st.table(risk)

st.markdown("---")

st.subheader("📈 Executive Summary")

st.info("""

### Customer Analytics

✔ Understand customer behaviour

✔ Identify valuable customers

✔ Segment customers automatically

✔ Improve marketing campaigns

""")

st.success("""

### Fraud Analytics

✔ Detect fraudulent returns

✔ Reduce refund losses

✔ Improve verification process

✔ Support business decisions

""")

st.warning("""

### Business Benefits

✔ Lower Fraud Loss

✔ Better Customer Experience

✔ Faster Decision Making

✔ Higher Profitability

""")

st.markdown("---")

st.success("""

## 🎯 Conclusion

This intelligent system combines:

✅ Customer Segmentation using KMeans

✅ Fraud Detection using Gradient Boosting

to provide actionable insights for return management, fraud prevention, and customer analytics.

""")

