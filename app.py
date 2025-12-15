import streamlit as st
from utils.resume_parser import extract_text_from_pdf

st.set_page_config(page_title="AI Job Application Assistant", layout="wide")

st.title("🤖 AI-Powered Job Application Assistant")

resume_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
jd_text = st.text_area("📝 Paste Job Description", height=200)

if st.button("Analyze"):
    if resume_file is None or jd_text.strip() == "":
        st.error("Please upload resume and paste job description.")
    else:
        resume_text = extract_text_from_pdf(resume_file)

        st.subheader("📄 Extracted Resume Text")
        st.text_area("Resume Content", resume_text, height=300)

        st.subheader("📝 Job Description")
        st.text_area("JD Content", jd_text, height=200)
