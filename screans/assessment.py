import streamlit as st



def assessment_page():


    st.markdown(
        """
        <style>


        .title{

            text-align:center;
            color:#0077B6;
            font-size:40px;
            font-weight:bold;

        }



        .subtitle{

            text-align:center;
            color:#555;
            font-size:18px;

        }



        div[data-testid="stVerticalBlockBorderWrapper"]{


            background-color:#EAF7FF;

            border:1px solid #BDE3F7;

            border-radius:20px;

            box-shadow:0px 5px 15px rgba(0,119,182,0.15);

        }



        </style>
        """,
        unsafe_allow_html=True
    )



    if st.button("⬅️ Back to Home"):

        st.session_state.page="home"

        st.rerun()



    st.markdown(
        """
        <div class="title">

        🩺 Health Assessment

        </div>


        <div class="subtitle">

        Enter your health information and choose a disease

        </div>

        """,
        unsafe_allow_html=True
    )



    st.write("")



    st.header(
        "👤 General Health Information"
    )



    col1,col2 = st.columns(2)



    with col1:


        age = st.number_input(
            "Age",
            1,
            120,
            30
        )


        gender = st.selectbox(
            "Gender",
            [
                "Male",
                "Female"
            ]
        )


        height = st.number_input(
            "Height (cm)",
            100,
            250,
            170
        )



    with col2:


        weight = st.number_input(
            "Weight (kg)",
            20,
            250,
            70
        )


        smoking_status = st.selectbox(
            "Smoking Status",
            [
                "never smoked",
                "formerly smoked",
                "smokes",
                "Unknown"
            ]
        )


        physical_activity = st.selectbox(
            "Physical Activity",
            [
                "Low",
                "Medium",
                "High"
            ]
        )



    bmi = weight / ((height/100)**2)


    st.info(
        f"Calculated BMI: {bmi:.2f}"
    )



    family_history = st.selectbox(
        "Family History",
        [
            "No",
            "Yes"
        ]
    )



    st.session_state.general_data = {

        "age":age,

        "gender":gender,

        "bmi":bmi,

        "smoking_status":smoking_status,

        "physical_activity":physical_activity,

        "family_history":family_history

    }



    st.divider()



    st.markdown(
        """
        <div class="title">

        🩺 Choose Health Assessment

        </div>

        """,
        unsafe_allow_html=True
    )



    diseases=[


        {
            "name":"Stroke",
            "icon":"assets/icons/stroke.png",
            "description":"Assess stroke risk"
        },


        {
            "name":"Diabetes",
            "icon":"assets/icons/diabetes.png",
            "description":"Assess diabetes risk"
        },


        {
            "name":"Heart Disease",
            "icon":"assets/icons/heart.png",
            "description":"Assess heart risk"
        },


        {
            "name":"Kidney Disease",
            "icon":"assets/icons/kidney.png",
            "description":"Assess kidney risk"
        },


        {
            "name":"Breast_Cancer Disease",
            "icon":"assets/icons/breast_cancer.png",
            "description":"Assess breast cancer risk"
        }

    ]



    cols=st.columns(3)



    for i,disease in enumerate(diseases):


        with cols[i%3]:


            with st.container(border=True):


                st.image(
                    disease["icon"],
                    width=80
                )


                st.subheader(
                    disease["name"]
                )


                st.write(
                    disease["description"]
                )


                if st.button(
                    "Start",
                    key=disease["name"],
                    use_container_width=True
                ):


                    st.session_state.selected_disease=disease["name"]

                    st.session_state.page="disease"

                    st.rerun()