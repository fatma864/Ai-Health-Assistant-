import streamlit as st
print("APP START")

from screans.home import home_page
from screans.assessment import assessment_page
from disease_pages.stroke import stroke_page
from disease_pages.diabetes import diabetes_page
from disease_pages.heart import heart_page_test
from disease_pages.kidney import kidney_page
from disease_pages.breast_cancer import breast_cancer_page


# ==========================
# Page Configuration
# ==========================

st.set_page_config(
    page_title="AI Health Assistant",
    page_icon="🩺",
    layout="wide"
)



# ==========================
# Medical Theme
# ==========================

st.markdown(
    """
    <style>


    .stApp {

        background-color:#F4FBFF;

    }



    /* Sidebar */

    section[data-testid="stSidebar"] {

        background-color:#E8F6FD;

    }



    section[data-testid="stSidebar"] h1 {

        color:#0077B6;

    }



    section[data-testid="stSidebar"] button {

        background-color:white;

        color:#0077B6;

        border-radius:12px;

        border:1px solid #BDE3F7;

    }



    section[data-testid="stSidebar"] button:hover {

        background-color:#0077B6;

        color:white;

    }



    /* Buttons */

    .stButton button {

        background-color:#0077B6;

        color:white;

        border-radius:12px;

        border:none;

    }



    .stButton button:hover {

        background-color:#005F8F;

    }



    </style>

    """,
    unsafe_allow_html=True
)




# ==========================
# Session State
# ==========================

if "page" not in st.session_state:

    st.session_state.page = "home"



if "selected_disease" not in st.session_state:

    st.session_state.selected_disease = None



if "general_data" not in st.session_state:

    st.session_state.general_data = None




# ==========================
# Sidebar
# ==========================

st.sidebar.title(
    "🩺 AI Health Assistant"
)



if st.sidebar.button(
    "🏠 Home",
    use_container_width=True
):

    st.session_state.page = "home"

    st.rerun()



if st.sidebar.button(
    "🩺 Assessment",
    use_container_width=True
):

    st.session_state.page = "assessment"

    st.rerun()



st.sidebar.divider()



if st.session_state.selected_disease:


    st.sidebar.markdown(
        """
        <div style="
        background:#DDF3FF;
        padding:15px;
        border-radius:15px;
        text-align:center;
        color:#0077B6;
        ">

        <b>Current Assessment</b>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.sidebar.info(
        st.session_state.selected_disease
    )




# ==========================
# Router
# ==========================

if st.session_state.page == "home":

    home_page()


elif st.session_state.page == "assessment":

    assessment_page()



elif st.session_state.page == "disease":

    if st.session_state.selected_disease == "Stroke":

        stroke_page(
            st.session_state.general_data
        )


    elif st.session_state.selected_disease == "Diabetes":

        diabetes_page(
            st.session_state.general_data
        )


    elif st.session_state.selected_disease == "Heart Disease":

        heart_page_test(
            st.session_state.general_data
        )


    elif st.session_state.selected_disease == "Kidney Disease":

        kidney_page(
            st.session_state.general_data
        )
        
    elif st.session_state.selected_disease == "Breast_Cancer Disease":
    
            breast_cancer_page(
                st.session_state.general_data
            )


    else:

        st.info(
            f"{st.session_state.selected_disease} page coming soon..."
        )