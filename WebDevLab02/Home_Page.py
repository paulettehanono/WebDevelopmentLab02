import streamlit as st
import info

st.title("Home Page")
st.title("Web Development Lab02")
st.write("---")
st.header("Paulette Hanono Gershon")
st.subheader("Course: CS 1301")
st.write("---")
st.subheader("Pages")
st.write("1.**Portfolio**: This page showcases a little bit about me, including my education, skills, experience, and projects. ")
st.write("2.**Fitness Tracker**: This page allows users to log their steps daily, track their workouts, monitor their calories, and visualize their progress. ")


st.write("---")
st.write("Welcome to my personal portfolio, here you will see a little bit of everything!")

with st.sidebar:
    st.title("📌 Navigation")
    
    # Dark Mode Toggle
    dark_mode = st.toggle("🌙 Dark Mode", value=False)
    
    st.write("---")

    dark_mode_css = """
    <style>
        body, .main, .stApp {
            background-color: #0E1117 !important;
            color: #EAEAEA !important;
        }
        .stButton>button {
            background-color: #30363D !important;
            color: white !important;
            border-radius: 10px;
        }
        .stTextInput>div>div>input {
            background-color: #21262D !important;
            color: white !important;
        }
        .stDataFrame {
            background-color: #30363D !important;
        }
    </style>
"""

light_mode_css = """
    <style>
        body, .main, .stApp {
            background-color: white !important;
            color: black !important;
        }
    </style>
"""

# Apply Dark or Light Mode Based on Toggle
if dark_mode:
    st.markdown(dark_mode_css, unsafe_allow_html=True)
else:
    st.markdown(light_mode_css, unsafe_allow_html=True)