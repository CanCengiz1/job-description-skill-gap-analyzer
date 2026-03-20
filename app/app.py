import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.skill_extractor import extract_skills
from src.matcher import match_skills

st.title("Skill Gap Analyzer")

skills = ["python", "sql", "machine learning", "excel", "data analysis"]

job_description = st.text_area("Job Description")
cv_text = st.text_area("Your CV")

if st.button("Analyze"):
    job_skills = extract_skills(job_description, skills)
    cv_skills = extract_skills(cv_text, skills)

    result = match_skills(job_skills, cv_skills)

    st.write("### Job Skills:", job_skills)
    st.write("### CV Skills:", cv_skills)
    st.write("### Result:", result)