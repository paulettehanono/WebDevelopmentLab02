import streamlit as st
import info
import pandas as pd

# About Me

def about_me_section():
    st.header("🚀 About Me")
    st.image(info.profile_picture, width=200)
    st.write(info.about_me)
    st.write('---')

about_me_section()

# Sidebar Links

def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="Linkedin" width = "75" height="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Checkout my Work")
    github_link = f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt="Github" width = "65" height="65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    st.sidebar.text("Or email me!")
    email_html = f'<a href="mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt="Email" width = "75" height="75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)

links_section()

# Education

def education_section(education_data, course_data):
    st.header("📚 Education")
    st.subheader(f"{education_data['Institution']}")
    st.write(f"**Degree:** {education_data['Degree']}")
    st.write(f"**Graduation Date:** {education_data['Graduation Date']}")
    st.write(f"**GPA:** {education_data['GPA']}")
    st.write(f"**Total Credits:** {education_data['Total Credits']}")
    st.write("**Relevant Coursework:**")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names": "Course Name",
        "semester_taken": "Semester Taken",
        "skills": "My thoughts"
    }, hide_index=True)

education_section(info.education_data, info.course_data)

# First Semester Courses

def first_semester_section(first_semester_data):
    coursework = pd.DataFrame(first_semester_data)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names": "Course Name",
        "semester_taken": "Semester Taken",
        "remarks": "My thoughts"
    }, hide_index=True)
    st.write("---")

first_semester_section(info.first_semester_data)

# Professional Experience

def experience_section(experience_data):
    st.header("🧳 Professional Experience")
    for job_title, (job_description, image) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(image, width=350)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")

experience_section(info.experience_data)

# Projects

def project_section(projects_data):
    st.header("🛠️ Projects")
    for project_name, project_info in projects_data.items():
        with st.expander(f"{project_name}"):
            if isinstance(project_info, dict):
                st.write(project_info["description"])
                st.image(project_info["image"], width=400)
            else:
                st.write(project_info)
    st.write("---")

project_section(info.projects_data)

# Skills

def skills_section(programming_data, spoken_data):
    st.header("👨‍💻 Skills")
    st.subheader("Programming Languages")
    for skill, percentage in programming_data.items():
        st.write(f"{skill}{info.programming_icons.get(skill,'')}")
        st.progress(percentage)
    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        st.write(f"{spoken}{info.spoken_icons.get(spoken,'')}:{proficiency}")
    st.write("---")

skills_section(info.programming_data, info.spoken_data)

# Activities

def activities_section(leadership_data, activity_data):
    st.header("🧗 Activities")
    tab1, tab2 = st.tabs(["Leadership", "Community Service"])
    with tab1:
        st.subheader("🥇 Leadership")
        for title, (details, image) in leadership_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width=350)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("🌍 Community Service")
        for title, (details, image) in activity_data.items():
            expander = st.expander(f"{title}")
            if image:
                expander.image(image, width=450)
            for bullet in details:
                expander.write(bullet)

activities_section(info.leadership_data, info.activity_data)

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