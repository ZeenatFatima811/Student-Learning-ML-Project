
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('student_model.joblib')

# Page configuration
st.set_page_config(
    page_title="Student Pass Prediction",
    page_icon="🎓"
)

st.title("🎓 Student Learning Prediction App")

st.write(
    "Enter student learning details to predict "
    "the demonstration Pass/Fail result."
)

# User inputs
hours_studied = st.number_input(
    "Hours Studied",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=75
)

practice_tests = st.number_input(
    "Practice Tests Completed",
    min_value=0,
    max_value=20,
    value=3
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)

study_method = st.selectbox(
    "Study Method",
    ["self", "video", "group"]
)

# Prediction button
if st.button("Predict Result"):

    student_data = pd.DataFrame({
        'hours_studied': [hours_studied],
        'attendance': [attendance],
        'practice_tests': [practice_tests],
        'sleep_hours': [sleep_hours],
        'study_method': [study_method]
    })

    prediction = model.predict(student_data)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.success("Predicted Result: Pass")
    else:
        st.warning("Predicted Result: Fail")

    st.caption(
        "Demonstration only. This synthetic-data model "
        "must not be used to judge or penalize real students."
    )
