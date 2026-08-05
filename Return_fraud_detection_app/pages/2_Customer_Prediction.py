import streamlit as st
import pandas as pd
import numpy as np
import pickle
from datetime import date
from pathlib import Path

st.set_page_config(
    page_title="Customer Prediction",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------
# Base Directory
# ----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

st.title("🤖 Customer Segmentation & Fraud Prediction")

st.markdown("""
Predict

- Customer Segment
- Fraud Return Risk

using **KMeans** and **Gradient Boosting**.
""")

st.markdown("---")

# ----------------------------
# Load Models
# ----------------------------

with open(BASE_DIR / "kmeans.pkl", "rb") as f:
    kmeans = pickle.load(f)

with open(BASE_DIR / "gbc_Fraud_Detection.pkl", "rb") as f:
    gbc = pickle.load(f)

with open(BASE_DIR / "scaler.pkl", "rb") as f:
    scaler = pickle.load(f)
  
cluster_names={

0:"🟢 Loyal Low-Return Customer",

1:"🟡 Active Frequent Shopper",

2:"🔴 High Value High Return Customer"

}

st.subheader("Customer Details")
c1,c2,c3=st.columns(3)

with c1:

    customer_tenure_days=st.number_input(
        "Customer Tenure (Days)",
        min_value=0,
        value=300
    )

    lifetime_spend=st.number_input(
        "Lifetime Spend",
        min_value=0.0,
        value=15000.0
    )

    total_orders=st.number_input(
        "Total Orders",
        min_value=0,
        value=20
    )

    total_returns=st.number_input(
        "Total Returns",
        min_value=0,
        value=2
    )

    return_rate=st.number_input(
        "Return Rate",
        min_value=0.0,
        max_value=1.0,
        value=0.10
    )

with c2:

    average_order_value=st.number_input(
        "Average Order Value",
        min_value=0.0,
        value=900.0
    )

    purchase_frequency=st.number_input(
        "Purchase Frequency",
        min_value=0.0,
        value=3.5
    )

    selling_price=st.number_input(
        "Selling Price",
        min_value=0.0,
        value=1200.0
    )

    delivery_delay=st.number_input(
        "Delivery Delay",
        min_value=0.0,
        value=3.0
    )

    quantity=st.number_input(
        "Quantity",
        min_value=1,
        value=1
    )

with c3:

    order_amount=st.number_input(
        "Order Amount",
        min_value=0.0,
        value=1200.0
    )

    discount=st.number_input(
        "Discount",
        min_value=0.0,
        value=10.0
    )

    return_days=st.number_input(
        "Return Days",
        min_value=0,
        value=5
    )

    refund_amount=st.number_input(
        "Refund Amount",
        min_value=0.0,
        value=1200.0
    )

    complaint_count=st.number_input(
        "Complaint Count",
        min_value=0.0,
        value=1.0
    )

    average_resolution_time=st.number_input(
        "Average Resolution Time",
        min_value=0.0,
        value=24.0
    )

    st.markdown("---")

st.subheader("Customer Information")

c1,c2,c3=st.columns(3)
with c1:

    membership=st.selectbox(

        "Membership Type",

        [

            "Basic",

            "Gold",

            "Silver",

            "Platinum"

        ]

    )

    category=st.selectbox(

        "Category",

        [

            "Electronics",

            "Fashion",

            "Home",

            "Shoes",

            "Sports"

        ]

    )

    luxury=st.selectbox(

        "Luxury Product",

        [

            "No",

            "Yes"

        ]

    )

with c2:

    payment=st.selectbox(

        "Payment Method",

        [

            "Card",

            "COD",

            "UPI",

            "Wallet",

            "NetBanking"

        ]

    )

    coupon=st.selectbox(

        "Coupon Used",

        [

            "No",

            "Yes"

        ]

    )

    sentiment=st.selectbox(

        "Customer Sentiment",

        [

            "Negative",

            "Neutral",

            "Positive"

        ]

    )

with c3:

    return_reason=st.selectbox(

        "Return Reason",

        [

            "Damaged",

            "Defective",

            "Late Delivery",

            "Wrong Item",

            "Wrong Size"

        ]

    )

    item_condition=st.selectbox(

        "Item Condition",

        [

            "Excellent",

            "Good",

            "Fair",

            "Poor"  

        ]

    )

st.markdown("---")

st.subheader("Product Inspection")

c1,c2,c3=st.columns(3)

with c1:

    missing_tags=st.selectbox(
        "Missing Tags",
        ["No","Yes"]
    )

    worn_signs=st.selectbox(
        "Worn Signs",
        ["No","Yes"]
    )

with c2:

    scratches=st.selectbox(
        "Scratches",
        ["No","Yes"]
    )

    stains=st.selectbox(
        "Stains",
        ["No","Yes"]
    )

with c3:

    packaging_damage=st.selectbox(
        "Packaging Damage",
        ["No","Yes"]
    )

st.markdown("---")

st.subheader("Order Dates")

c1,c2,c3=st.columns(3)

with c1:

    order_date=st.date_input(
        "Order Date",
        value=date.today()
    )

with c2:

    delivery_date=st.date_input(
        "Delivery Date",
        value=date.today()
    )

with c3:

    return_date=st.date_input(
        "Return Date",
        value=date.today()
    )

st.markdown("---")

predict=st.button("🚀 Predict Customer")

if predict:

    kmeans_df=pd.DataFrame({

        "customer_tenure_days":[customer_tenure_days],

        "lifetime_spend":[lifetime_spend],

        "total_orders":[total_orders],

        "total_returns":[total_returns],

        "return_rate":[return_rate],

        "average_order_value":[average_order_value],

        "purchase_frequency":[purchase_frequency]

    })

    kmeans_scaled=scaler.transform(kmeans_df)
    cluster=int(kmeans.predict(kmeans_scaled)[0])
    segment=cluster_names[cluster]

    x={

    'customer_tenure_days':customer_tenure_days,

    'lifetime_spend':lifetime_spend,

    'total_orders':total_orders,

    'total_returns':total_returns,

    'return_rate':return_rate,

    'average_order_value':average_order_value,

    'purchase_frequency':purchase_frequency,

    'selling_price':selling_price,

    'delivery_delay':delivery_delay,

    'quantity':quantity,

    'order_amount':order_amount,

    'discount':discount,

    'return_days':return_days,

    'refund_amount':refund_amount,

    'complaint_count':complaint_count,

    'average_resolution_time':average_resolution_time

    }

    x["membership_type_gold"]=1 if membership=="Gold" else 0

    x["membership_type_platinum"]=1 if membership=="Platinum" else 0

    x["membership_type_silver"]=1 if membership=="Silver" else 0

    x["category_electronics"]=1 if category=="Electronics" else 0

    x["category_fashion"]=1 if category=="Fashion" else 0

    x["category_home"]=1 if category=="Home" else 0

    x["category_shoes"]=1 if category=="Shoes" else 0

    x["category_sports"]=1 if category=="Sports" else 0

    x["luxury_flag_yes"]=1 if luxury=="Yes" else 0

    x["payment_method_cod"]=1 if payment=="COD" else 0

    x["payment_method_netbanking"]=1 if payment=="NetBanking" else 0

    x["payment_method_upi"]=1 if payment=="UPI" else 0

    x["payment_method_wallet"]=1 if payment=="Wallet" else 0

    x["return_reason_damaged"]=1 if return_reason=="Damaged" else 0

    x["return_reason_defective"]=1 if return_reason=="Defective" else 0

    x["return_reason_late delivery"]=1 if return_reason=="Late Delivery" else 0

    x["return_reason_wrong item"]=1 if return_reason=="Wrong Item" else 0

    x["return_reason_wrong size"]=1 if return_reason=="Wrong Size" else 0

    x["item_condition_fair"]=1 if item_condition=="Fair" else 0

    x["item_condition_good"]=1 if item_condition=="Good" else 0

    x["item_condition_poor"]=1 if item_condition=="Poor" else 0

    x["missing_tags_yes"] = 1 if missing_tags == "Yes" else 0

    x["worn_signs_yes"] = 1 if worn_signs == "Yes" else 0

    x["scratches_yes"] = 1 if scratches == "Yes" else 0

    x["stains_yes"] = 1 if stains == "Yes" else 0

    x["packaging_damage_yes"] = 1 if packaging_damage == "Yes" else 0

    x["sentiment_neutral"]=1 if sentiment=="Neutral" else 0

    x["sentiment_positive"]=1 if sentiment=="Positive" else 0

    feature_order = [

    'customer_tenure_days',
    'lifetime_spend',
    'total_orders',
    'total_returns',
    'return_rate',
    'average_order_value',
    'purchase_frequency',
    'selling_price',
    'delivery_delay',
    'quantity',
    'order_amount',
    'discount',
    'return_days',
    'refund_amount',
    'complaint_count',
    'average_resolution_time',

    'membership_type_gold',
    'membership_type_platinum',
    'membership_type_silver',

    'category_electronics',
    'category_fashion',
    'category_home',
    'category_shoes',
    'category_sports',

    'luxury_flag_yes',

    'payment_method_cod',
    'payment_method_netbanking',
    'payment_method_upi',
    'payment_method_wallet',

    'return_reason_damaged',
    'return_reason_defective',
    'return_reason_late delivery',
    'return_reason_wrong item',
    'return_reason_wrong size',

    'item_condition_fair',
    'item_condition_good',
    'item_condition_poor',

    'missing_tags_yes',
    'worn_signs_yes',
    'scratches_yes',
    'stains_yes',
    'packaging_damage_yes',

    'sentiment_neutral',
    'sentiment_positive'

    ]

    x = pd.DataFrame([x])

    x = x[feature_order]

    prediction = gbc.predict(x)[0]

    probability = gbc.predict_proba(x)[0][1]

    if probability < 0.30:

        risk = "🟢 Low Risk"

    elif probability < 0.70:

        risk = "🟡 Medium Risk"

    else:

        risk = "🔴 High Risk"

    st.markdown("---")

    st.header("Prediction Results")

    c1,c2 = st.columns(2)

    with c1:

        st.success("Customer Segment")

        st.markdown(f"## {segment}")

        st.write("Cluster Number :", cluster)

    with c2:

        if prediction == 1:

            st.error("⚠ Fraudulent Return Predicted")

        else:

            st.success("✅ Genuine Return")
    st.markdown("---")

    st.subheader("Fraud Probability")

    st.progress(float(probability))

    st.metric(

        "Probability",

        f"{probability*100:.2f}%"

    )
    st.subheader("Risk Level")

    st.info(risk)
    st.markdown("---")

    st.subheader("Customer Summary")

    summary = pd.DataFrame({

        "Feature":[

            "Customer Segment",

            "Fraud Prediction",

            "Risk Level",

            "Purchase Frequency",

            "Return Rate",

            "Lifetime Spend",

            "Average Order Value"

        ],

        "Value":[

            segment,

            "Fraud" if prediction==1 else "Genuine",

            risk,

            purchase_frequency,

            return_rate,

            lifetime_spend,

            average_order_value

        ]

    })

    st.table(summary)

    st.markdown("---")

    st.subheader("Business Recommendation")

    if prediction == 1:

        st.error("""

    ### Recommended Action

    • Perform Manual Verification

    • Verify Customer Identity

    • Verify Returned Product

    • Delay Refund Until Inspection

    • Flag Customer for Monitoring

    """)

    else:

        st.success("""

    ### Recommended Action

    • Approve Refund

    • Process Normally

    • Customer Appears Genuine

    • No Manual Verification Required

    """)
    st.markdown("---")

    st.subheader("Customer Segment Insights")

    if cluster == 0:

        st.success("""

    ### 🟢 Loyal Low-Return Customer

    • Long-term customer

    • Low return behaviour

    • High trust

    • Suitable for loyalty offers

    """)

    elif cluster == 1:

        st.warning("""

    ### 🟡 Active Frequent Shopper

    • Purchases frequently

    • Moderate return behaviour

    • Monitor return trends

    • Good cross-selling opportunity

    """)

    else:

        st.error("""

    ### 🔴 High Value High Return Customer

    • High spending customer

    • High return behaviour

    • High refund exposure

    • Requires additional verification

    """)
