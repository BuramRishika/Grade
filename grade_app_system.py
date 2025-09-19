import streamlit as st

def calculate_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

st.title("Grade System Application")

student_name = st.text_input("Enter Student Name")
numeric_grade = st.number_input("Enter Numeric Grade", min_value=0, max_value=100, step=1)

if st.button("Calculate Grade"):
    if not student_name:
        st.error("Please enter the student's name.")
    else:
        letter_grade = calculate_letter_grade(numeric_grade)
        st.success(f"{student_name}'s Grade: {letter_grade}")
