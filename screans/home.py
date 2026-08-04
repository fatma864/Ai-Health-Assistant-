import streamlit as st


def home_page():

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"]{
        font-family:'Poppins',sans-serif;
    }

    .stApp{
        background:#F4FBFF;
    }

    .hero{
        background:linear-gradient(135deg,#0077B6,#0096C7);
        padding:40px;
        border-radius:25px;
        color:white;
        text-align:center;
        margin-bottom:35px;
        box-shadow:0 10px 25px rgba(0,119,182,.18);
    }

    .hero h1{
        font-size:42px;
        font-weight:700;
        margin-bottom:12px;
    }

    .hero p{
        font-size:18px;
        line-height:1.8;
        opacity:.95;
    }

    .section-title{
        text-align:center;
        color:#0077B6;
        font-size:30px;
        font-weight:600;
        margin-top:10px;
        margin-bottom:25px;
    }

    .feature-card{

        background:white;
        border-radius:18px;
        padding:28px;
        height:230px;
        box-shadow:0 6px 20px rgba(0,0,0,.07);
        border:1px solid #DCEEF8;
        transition:.3s;

    }

    .feature-card:hover{

        transform:translateY(-5px);

    }

    .feature-title{

        font-size:22px;
        font-weight:600;
        color:#0077B6;
        margin-bottom:15px;

    }

    .feature-text{

        color:#555;
        line-height:1.8;
        font-size:15px;

    }

    .disease-box{

        background:#EAF7FF;
        padding:30px;
        border-radius:20px;
        border:1px solid #CDE8F8;
        margin-top:35px;
        margin-bottom:30px;

    }

    .disease-title{

        text-align:center;
        color:#0077B6;
        font-size:28px;
        font-weight:600;
        margin-bottom:25px;

    }

    .disease-grid{

        display:grid;
        grid-template-columns:repeat(3,1fr);
        gap:15px;

    }

    .disease-item{

        background:white;
        border-radius:12px;
        padding:18px;
        text-align:center;
        font-weight:500;
        color:#333;
        border:1px solid #D8ECF8;

    }

    .footer{

        margin-top:30px;
        text-align:center;
        color:#666;
        font-size:16px;
        line-height:1.8;

    }

    div.stButton>button{

        background:#0077B6;
        color:white;
        border:none;
        border-radius:12px;
        height:55px;
        font-size:18px;
        font-weight:600;

    }

    div.stButton>button:hover{

        background:#005F8F;
        color:white;

    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""

    <div class="hero">

    <h1>AI Health Assistant</h1>

    <p>

    Predict the risk of common diseases using Artificial Intelligence
    and receive clear health insights with personalized recommendations.

    </p>

    </div>

    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Project Features</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""

        <div class="feature-card">

        <div class="feature-title">

        Disease Prediction

        </div>

        <div class="feature-text">

        Advanced Machine Learning models estimate the probability of
        multiple diseases using the patient's medical information.

        </div>

        </div>

        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""

        <div class="feature-card">

        <div class="feature-title">

        AI Health Summary

        </div>

        <div class="feature-text">

        Generate an easy-to-understand explanation of the prediction,
        possible contributing factors, and personalized health advice.

        </div>

        </div>

        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""

        <div class="feature-card">

        <div class="feature-title">

        Personalized Recommendations

        </div>

        <div class="feature-text">

        Receive practical lifestyle recommendations based on your health
        profile and prediction results.

        </div>

        </div>

        """, unsafe_allow_html=True)

    st.markdown("""

    <div class="disease-box">

    <div class="disease-title">

    Supported Disease Prediction Models

    </div>

    <div class="disease-grid">

    <div class="disease-item">Diabetes</div>

    <div class="disease-item">Heart Disease</div>

    <div class="disease-item">Stroke</div>

    <div class="disease-item">Kidney Disease</div>

    <div class="disease-item">Breast Cancer</div>

    </div>

    </div>

    """, unsafe_allow_html=True)

    st.markdown("""

    <div class="footer">

    This intelligent healthcare assistant combines multiple Machine Learning
    models with Large Language Models (LLMs) to provide accurate disease
    risk prediction, patient-friendly health summaries, and personalized
    recommendations for better health awareness.

    </div>

    """, unsafe_allow_html=True)

    st.write("")

    if st.button(
        "Start Health Assessment",
        use_container_width=True
    ):

        st.session_state.page = "assessment"
        st.rerun()