import streamlit as st
from utils.resume_parser import extract_text_from_pdf
from utils.skill_gap import skill_gap_analysis

st.set_page_config(page_title="AI Job Application Assistant", layout="wide")

st.title("🤖 AI-Powered Job Application Assistant")

resume_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
jd_text = st.text_area("📝 Paste Job Description", height=200)

if st.button("Analyze"):
    if resume_file is None or jd_text.strip() == "":
        st.error("Please upload resume and paste job description.")
    else:
        resume_text = extract_text_from_pdf(resume_file)

        resume_skills, jd_skills, missing_skills = skill_gap_analysis(
            resume_text, jd_text
        )

        st.subheader("✅ Skills Found in Resume")
        st.write(resume_skills)

        st.subheader("📌 Skills Required in Job Description")
        st.write(jd_skills)

        st.subheader("❌ Missing Skills (Skill Gap)")
        st.write(missing_skills)
