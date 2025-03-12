import streamlit as st
import pandas as pd
import json
import time  
import plotly.express as px

def load_data():
    try:
        with open("fitness_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"steps": [], "calories": [], "dates": []}

def save_data(data):
    with open("fitness_data.json", "w") as f:
        json.dump(data, f)

fitness_data = load_data()

if "step_count" not in st.session_state:
    st.session_state["step_count"] = 0
if "calories_burned" not in st.session_state:
    st.session_state["calories_burned"] = 0

st.title("🏋️‍♂️ My Fitness Tracker")
st.write("Track your daily steps, calories, and workouts! Stay motivated and monitor your progress.")
st.header("🚶‍♂️ Step Counter & Workout Logger")


step_input = st.number_input("Enter today's steps:", min_value=0, step=100, value=st.session_state["step_count"])
if st.button("Update Steps"): 
    st.session_state["step_count"] = step_input
    fitness_data["steps"].append(step_input)
    fitness_data["dates"].append(time.strftime("%Y-%m-%d"))  
    save_data(fitness_data)
    st.success("Step count updated!")

workout_type = st.selectbox("Select your workout:", ["Running", "Cycling", "Weight Training", "Yoga","Other"])  
calories_burned = st.slider("Calories burned:", 50, 1000, 200)  #NEW
if st.button("Log Workout"):
    st.session_state["calories_burned"] += calories_burned
    fitness_data["calories"].append({"type": workout_type, "calories": calories_burned})
    save_data(fitness_data)
    st.success(f"{workout_type} workout logged!")

st.metric(label="Total Steps Today", value=st.session_state["step_count"]) #NEW
st.metric(label="Total Calories Burned", value=st.session_state["calories_burned"])

st.header("📊 Fitness Progress")

st.subheader("Weekly Step Count")
if len(fitness_data["steps"]) > 0:
    step_data = pd.DataFrame({"Date": fitness_data["dates"], "Steps": fitness_data["steps"]})
    st.bar_chart(step_data.set_index("Date"))
else:
    st.write("No step data available yet. Start logging!")

st.subheader("Step Count Over Time")
if len(fitness_data["steps"]) > 1:
    st.line_chart(step_data.set_index("Date"))
else:
    st.write("Log multiple days to see trends!")

st.subheader("Calories Burned Breakdown")
if len(fitness_data["calories"]) > 0:
    calorie_df = pd.DataFrame(fitness_data["calories"])
    calorie_summary = calorie_df.groupby("type").sum().reset_index()

    fig = px.pie(calorie_summary, names="type", values="calories", title="Calories Burned by Workout Type")
    st.plotly_chart(fig)
else:
    st.write("No workout data available yet.")

st.write("💪 Keep up the great work! Track daily to see improvements over time.")

st.sidebar.header("⚙️ Settings")

if st.sidebar.button("🔄 Reset All Data", key="reset_button"):
    st.session_state["step_count"] = 0
    st.session_state["calories_burned"] = 0
    empty_data = {"steps": [], "calories": [], "dates": []}
    save_data(empty_data)

    st.sidebar.success("All progress has been reset!")

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

dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=False, key="dark_mode_toggle")

# Apply Dark or Light Mode Based on Toggle
if dark_mode:
    st.markdown(dark_mode_css, unsafe_allow_html=True)
else:
    st.markdown(light_mode_css, unsafe_allow_html=True)

with st.sidebar:
    st.title("📌 Navigation")

    st.header("🎯 Set Your Step Goal")
    goal = st.number_input(
        "Set your step goal for today:",
        min_value=1000,
        max_value=50000,
        step=500,
        value=10000,
        key="step_goal_input"  # ✅ Ensures unique identifier
    )

    # Ensure "step_count" exists in session state
    if "step_count" not in st.session_state:
        st.session_state["step_count"] = 0  

    # Display Progress
    progress = min(st.session_state["step_count"] / goal, 1.0)  # Normalize progress
    st.progress(progress)
    st.write(f"**{st.session_state['step_count']} / {goal} steps completed**")