import streamlit as st
import datetime

# App Title
st.title("Growth Mindset Skill Tracker")
st.title("BY TASBIHA JAWAID")

# Initialize session state if not present
if "skills" not in st.session_state:
    st.session_state.skills = {}

# Add a new skill
st.header("Set a New Learning Goal")
skill = st.text_input("Enter the skill you want to improve (e.g., Python, Public Speaking)")
duration = st.number_input("How many weeks will you practice?", min_value=1, max_value=52, value=4)
start_date = st.date_input("Start Date", datetime.date.today())

if st.button("Add Goal"):
    if skill:
        st.session_state.skills[skill] = {"duration": duration, "start_date": start_date, "progress": 0}
        st.success(f"Your goal to improve '{skill}' has been added!")

# Display Skills and Track Progress
if st.session_state.skills:
    st.header("Track Your Progress")
    for skill, data in st.session_state.skills.items():
        st.subheader(f"{skill}")
        progress = st.slider(f"Progress for {skill} (0-100%)", 0, 100, data["progress"])
        st.session_state.skills[skill]["progress"] = progress
        
        # Growth mindset messages
        if progress < 30:
            st.warning("Keep going! Every small step counts.")
        elif progress < 70:
            st.info("You're making great progress! Stay consistent.")
        else:
            st.success("Amazing job! You're almost there. Keep pushing!")

# Encourage Consistency
st.header("Growth Mindset Reminder")
st.write("Remember: **Your effort determines your success!** Stay dedicated, and progress will follow.")
