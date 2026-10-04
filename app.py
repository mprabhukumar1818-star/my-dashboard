import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Helper function to load Lottie animations from URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load a sample 3D-style Lottie animation (coding/tech)
lottie_tech = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

st.title("My Student Dashboard")

focus, projects, log = st.tabs(["Focus", "Projects", "Daily Log"])

with focus:
    st.header("Focus Areas")
    st.write("Track your programming languages and AI topics here.")
    st.progress(50, text="Python Mastery")
    st.progress(30, text="Data Structures")
    
    # Display Lottie animation here
    if lottie_tech:
        st_lottie(lottie_tech, height=200, key="focus_anim")

with projects:
    st.header("Project Tracker")
    st.write("Monitor your hackathon projects and internship preparation.")
    st.table({
        "Project Name": ["Hackathon 1", "Internship Prep"],
        "Status": ["In Progress", "Planning"]
    })

with log:
    st.header("Daily Learning Log")
    st.write("Record your coding hours and book reading.")
    st.metric(label="Hours Coded Today", value="3 hrs")