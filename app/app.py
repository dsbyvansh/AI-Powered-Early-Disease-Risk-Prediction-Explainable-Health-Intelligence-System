import streamlit as st

st.set_page_config(
    page_title="Diabetes Risk Predictor",
    page_icon="🩺",
    layout='wide'
)

st.title("Diabetes Risk Predictor")
st.caption(
    "This tool is for screening only. It flags people for further testing and does not provide a diagnosis."
)


def map_to_age_band(age):
    if age<25: return 1
    elif age < 30: return 2          
    elif age < 35: return 3
    elif age < 40: return 4
    elif age < 45: return 5
    elif age < 50: return 6
    elif age < 55: return 7
    elif age < 60: return 8
    elif age < 65: return 9
    elif age < 70: return 10
    elif age < 75: return 11
    elif age < 80: return 12
    else : return 13 

income_mapping = {
    "Less than $15,000": 1,
    "$15,000 - $25,000": 3,
    "$25,000 - $50,000": 5,
    "$50,000 - $75,000": 7,
    "$75,000 or more": 8
    }

education_mapping = {
    "Never Attended School": 1,
    "Elementary School": 2,
    "High School": 3,
    "High School Graduate": 4,
    "Some College": 5,
    "College Graduate": 6
}
exercise_mapping = {
    "No":0,
    "Yes":1
}

smoke_mapping = {
    "Never Smoked":3.0,
    "Former Smoker":2.0,
    "Smoke Some days":0.0,
    "Smoke Everyday": 1.0 
}

genhlth_mapping = {
    "Excellent": 0.0,
    "Very Good": 1.0,
    "Good": 2.0,
    "Fair": 3.0,
    "Poor": 4.0
}


with st.form("risk_inputs"):
    st.subheader("About You")
    st.caption("Basic demographics help estimate baseline risk.")
    col1, col2, col3, col4,ccol = st.columns(4)       
    
    with col1:
        age = st.slider("How old are you?", 18, 100, 25)
        age_band = map_to_age_band(age)
    with col2:
        sex_option = st.selectbox(
            "What is your biological sex?",
            ("Male", "Female", "Prefer not to say")
        )

    with ccol:
        marital = st.selectbox(
            "Whats your Marital Status",
            ("Single","Married","Prefer not to say")
        )
        if(marital=="Married"):
            children = st.slider("How many Children do you have?",0,5,0)
    
    with col3:
        income = st.selectbox(
            "Annual Household Income",
            (
                "Less than $15,000",
                "$15,000 - $25,000",
                "$25,000 - $50,000",
                "$50,000 - $75,000",
                "$75,000 or more"
            )
        )
    with col4:
        education = st.selectbox(
            "Education Level",
            (
                "Never Attended School",
                "Elementary School",
                "High School",
                "High School Graduate",
                "Some College",
                "College Graduate"
            )
        )

    st.subheader("Your Body")
    st.caption("Height and weight are used to calculate BMI.")
    col5, col6 = st.columns(2)
    with col5:
        height = st.number_input(
            "Enter your height in cm",
            min_value=50.0,
            max_value=250.0,
            value=170.0,
            step=0.5
        )
        height_in_m = height / 100
    with col6:
        weight = st.number_input(
            "Enter your weight in kg",
            min_value=20.0,
            max_value=300.0,
            value=70.0,
            step=0.5
        )

    if height_in_m > 0:
        bmi = weight / (height_in_m ** 2)
        st.caption(f"Calculated BMI: {bmi:.1f}")
        st.caption("BMI is a screening indicator and does not replace clinical assessment.")

    st.subheader("Lifestyle")
    col7,col8,col9 = st.columns(3)
    with col9: 
        exercise = st.selectbox(
            "Did you exercise in the past 30 days?",
            ("Yes","No")
        )
    with col8:
        smoking = st.selectbox(
            "What is your current smoking status?",
            ("Never Smoked","Former Smoker","Smoke Some days","Smoke Everyday")
        )
    with col9:
        alcohol = st.selectbox(
            "Have you had any alcohol in the past 30 days?",
            ("Yes","No")
        )
        if(alcohol=="Yes"):
            alcohol_days = st.slider("How many days did you drink alcohol in the past 30 days?",0,30,0)

    st.subheader("Recent Health")
    col10,col11,col12 = st.columns(3)
    with col10:
        general_health = st.selectbox(
            "How would you rate your general health?",
            ("Excellent","Very Good","Good","Fair","Poor")
        )
    with col11:
        physical_health = st.slider("In the past 30 days, how many days was your physical health not good?",0,30,0)
    with col12:
        mental_health = st.slider("In the past 30 days, how many days was your mental health not good?",0,30,0)

    st.subheader("Medical History")
    c
    submitted = st.form_submit_button("Run Risk Screening")