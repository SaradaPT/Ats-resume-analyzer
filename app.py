import os
import streamlit as st
from resume_parser import extract_text_from_pdf
from resume_matcher import calculate_resume_score, generate_feedback



# Configure Streamlit Page
st.set_page_config(page_title="ATS Resume Checker", layout="centered")

st.title("📄 ATS Resume Checker")
st.write("Upload your resume and check its match score with a job description!")

# Upload resume file
uploaded_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

if uploaded_file:
    # Save uploaded file to disk
    resume_path = os.path.join("uploads", uploaded_file.name)
    os.makedirs("uploads", exist_ok=True)
    
    with open(resume_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract text from resume
    resume_text = extract_text_from_pdf(resume_path)

    # Sample job description (Replace this with dynamic input)
    job_description = "Looking for a Data Scientist with Python, NLP, and SQL experience."

    # Calculate resume score
    score = calculate_resume_score(resume_text, job_description)
    feedback = generate_feedback(resume_text, job_description)

    # Display results
    st.subheader("🔍 Resume Match Score")
    st.write(f"✅ Your Resume Score: **{score}%**")

    st.subheader("📢 Feedback")
    st.write(feedback)

    # Cleanup: Delete uploaded file after processing
    os.remove(resume_path)
