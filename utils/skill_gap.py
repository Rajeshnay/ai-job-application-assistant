COMMON_SKILLS = [
    "python", "machine learning", "deep learning", "sql",
    "streamlit", "docker", "nlp", "data analysis",
    "pandas", "numpy", "scikit-learn", "tensorflow",
    "pytorch", "power bi", "tableau", "git"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in COMMON_SKILLS:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


def skill_gap_analysis(resume_text, jd_text):
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    missing_skills = list(set(jd_skills) - set(resume_skills))

    return resume_skills, jd_skills, missing_skills
