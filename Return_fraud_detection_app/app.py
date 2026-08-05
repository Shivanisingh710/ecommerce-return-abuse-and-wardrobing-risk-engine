import streamlit as st

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="E-Commerce Return Abuse & Wardrobing Risk Engine",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

.main{
    background-color:#F8F9FA;
}

h1,h2,h3,h4{
    color:#0B3C5D;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:15px;
    padding:15px;
    box-shadow:0px 0px 10px rgba(0,0,0,0.08);
}

.stButton>button{
    width:100%;
    height:48px;
    border-radius:12px;
    background:#0B5ED7;
    color:white;
    font-weight:bold;
    font-size:17px;
}

.stButton>button:hover{
    background:#084298;
    color:white;
}

.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.title("🛒 Fraud Return Prediction Engine")

st.sidebar.markdown("---")

st.sidebar.success("Models")

st.sidebar.write("✅ KMeans Customer Segmentation")

st.sidebar.write("✅ Gradient Boosting Fraud Detection")

st.sidebar.markdown("---")

st.sidebar.info("""
### Pages

🏠 Home

📊 Dashboard

🤖 Customer Prediction

📈 Customer Insights
""")

st.sidebar.markdown("---")

st.sidebar.success("Developed using")

st.sidebar.write("• Streamlit")

st.sidebar.write("• Scikit-Learn")

st.sidebar.write("• Plotly")

st.sidebar.write("• Pandas")

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.title("🛒 E-Commerce Return Risk Intelligence System")

st.markdown("""
This application combines **Customer Segmentation**
and **Fraud Return Detection** into a single intelligent
decision support system.

The objective is to identify:

- Customer Segment
- Fraudulent Return Risk
- Customer Behaviour
- Business Insights
""")

st.markdown("---")

# ---------------------------------------------------------
# FEATURES
# ---------------------------------------------------------

st.subheader("✨ Key Features")

col1,col2,col3=st.columns(3)

with col1:

    st.success("### 👥 Customer Segmentation")

    st.write("""
- KMeans Clustering

- Customer Behaviour

- Segment Identification

- Customer Profiling
""")

with col2:

    st.error("### 🛡 Fraud Detection")

    st.write("""
- Gradient Boosting

- Fraud Prediction

- Risk Classification

- Fraud Probability
""")

with col3:

    st.info("### 📊 Dashboard")

    st.write("""
- Interactive Charts

- KPIs

- Business Insights

- Customer Analytics
""")

st.markdown("---")

# ---------------------------------------------------------
# WORKFLOW
# ---------------------------------------------------------

st.subheader("⚙ Workflow")

st.markdown("""

Customer Details

⬇

Data Preprocessing

⬇

KMeans Customer Segmentation

⬇

Gradient Boosting Classification

⬇

Prediction

⬇

Business Recommendation

""")

st.markdown("---")

# ---------------------------------------------------------
# MODELS
# ---------------------------------------------------------

st.subheader("🤖 Machine Learning Models")

c1,c2=st.columns(2)

with c1:

    st.success("""

### KMeans Clustering

Purpose

✔ Customer Segmentation

Algorithm

✔ Unsupervised Learning

Output

✔ Customer Segment

""")

with c2:

    st.error("""

### Gradient Boosting

Purpose

✔ Fraud Detection

Algorithm

✔ Supervised Learning

Output

✔ Fraud Prediction

""")

st.markdown("---")

# ---------------------------------------------------------
# SEGMENTS
# ---------------------------------------------------------

st.subheader("👥 Customer Segments")

st.info("""
🟢 Loyal Low-Return Customers

• Long Customer Tenure

• Low Return Rate

• Stable Buying Behaviour
""")

st.warning("""
🟡 Active Frequent Shoppers

• Frequent Purchases

• Moderate Return Behaviour

• Medium Risk
""")

st.error("""
🔴 High Value High Return Customers

• Highest Spending

• Highest Return Rate

• High Fraud Risk
""")

st.markdown("---")

# ---------------------------------------------------------
# BUSINESS USE CASES
# ---------------------------------------------------------

st.subheader("💼 Business Applications")

left,right=st.columns(2)

with left:

    st.write("""
### Customer Segmentation

✔ Marketing

✔ Customer Retention

✔ Personalised Offers

✔ Customer Profiling
""")

with right:

    st.write("""
### Fraud Detection

✔ Refund Verification

✔ Manual Review

✔ Return Abuse Detection

✔ Business Loss Prevention
""")

st.markdown("---")

# ---------------------------------------------------------
# TECHNOLOGY
# ---------------------------------------------------------

st.subheader("🛠 Technology Stack")

tech1,tech2,tech3,tech4=st.columns(4)

with tech1:
    st.metric("Language","Python")

with tech2:
    st.metric("Framework","Streamlit")

with tech3:
    st.metric("ML Models","2")

with tech4:
    st.metric("Dashboard","Interactive")

st.markdown("---")

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.success("""
### 🚀 Get Started

Use the **left sidebar** to navigate through the application.

📊 Dashboard → Explore customer and fraud analytics.

🤖 Customer Prediction → Predict customer segment and fraud risk.

📈 Customer Insights → Understand customer behaviour and business recommendations.
""")
