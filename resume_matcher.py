import re
from collections import Counter

def calculate_resume_score(resume_text, job_description):
    """
    Calculates a refined resume score based on keyword matching with the job description.
    This version accounts for keyword frequency and context.
    """
    # Clean and tokenize the text using regex to handle punctuation
    resume_words = re.findall(r'\w+', resume_text.lower())
    job_words = re.findall(r'\w+', job_description.lower())
    
    # Count frequency of each word in both resume and job description
    resume_word_count = Counter(resume_words)
    job_word_count = Counter(job_words)

    # Identify matched words
    matched_keywords = set(resume_words) & set(job_words)
    
    # Calculate the match score based on frequency of matching words
    score = 0
    total_job_keywords = sum(job_word_count.values())
    
    for keyword in matched_keywords:
        # Score based on how frequently the matched keyword appears in both the resume and job description
        score += min(resume_word_count[keyword], job_word_count[keyword]) / total_job_keywords
    
    # Normalize the score to a percentage and round it to two decimal places
    score = round((score / len(job_words)) * 100, 2) if job_words else 0
    
    return score

def generate_feedback(resume_text, job_description):
    """
    Provides a detailed explanation of resume strengths and areas for improvement based on job description.
    This version includes keyword density, content suggestions, and ATS considerations.
    """
    resume_words = re.findall(r'\w+', resume_text.lower())
    job_words = re.findall(r'\w+', job_description.lower())

    matched_keywords = set(resume_words) & set(job_words)
    missing_keywords = set(job_words) - set(resume_words)

    feedback = "**Resume Analysis & Feedback**\n\n"

    # Provide analysis on keyword matching
    feedback += f"✅ **Matched Keywords**: {', '.join(matched_keywords)}\n\n"
    
    # Suggest areas to improve based on missing keywords
    if missing_keywords:
        feedback += "🔴 **Areas to Improve:**\n"
        feedback += "- **Add the following missing keywords** from the job description: " + ", ".join(missing_keywords) + "\n"
        feedback += "    - Ensure that the most relevant technical and soft skills are highlighted in your experience or skills section.\n"
    else:
        feedback += "✅ **Keyword Match:** Your resume contains all the necessary keywords!\n"
    
    # Content-related feedback based on keyword density
    feedback += "\n🔹 **Keyword Density & Relevance:**\n"
    total_resume_words = len(resume_words)
    keyword_density = sum(resume_words.count(keyword) for keyword in matched_keywords) / total_resume_words
    feedback += f"- **Keyword Density**: Your resume has a keyword density of {round(keyword_density * 100, 2)}%. Aim to increase this for high-priority terms like technical skills and core competencies.\n"

    # Formatting & Structure Suggestions
    feedback += "\n🔹 **Formatting & Structure:**\n"
    feedback += "- Ensure your resume is clean and easy to read by using standard headings like 'Experience,' 'Skills,' and 'Education.'\n"
    feedback += "- Avoid using complicated designs or fonts; stick to clean, professional fonts such as Arial, Calibri, or Times New Roman.\n"
    feedback += "- Ensure your contact information (name, phone number, email) is easy to find at the top of the resume.\n"

    # Content & Achievements Suggestions
    feedback += "\n🔹 **Content & Achievements:**\n"
    feedback += "- Quantify your achievements wherever possible. For example: 'Increased sales by 20%' or 'Reduced costs by 15%.'\n"
    feedback += "- Focus on demonstrating impact. Instead of just listing duties, emphasize how you contributed to the company's success.\n"
    feedback += "- Make sure each experience listed on your resume aligns with the job description, showcasing relevant projects and roles.\n"

    # Skills & Certifications Suggestions
    feedback += "\n🔹 **Skills & Certifications:**\n"
    feedback += "- Include a dedicated 'Skills' section that lists both technical skills (e.g., Python, SQL, Tableau) and soft skills (e.g., leadership, communication).\n"
    feedback += "- Add any relevant certifications, particularly those mentioned in the job description, such as data analysis or project management certifications.\n"

    # General Tips & Best Practices
    feedback += "\n🔹 **General Resume Improvement Tips:**\n"
    feedback += "- Keep your resume concise—ideally 1-2 pages. Be selective about what to include, focusing on the most relevant and impactful information.\n"
    feedback += "- Proofread your resume for grammar, spelling, and consistency. ATS systems may not recognize misspelled words as keywords.\n"
    feedback += "- Avoid using images, graphics, or unusual fonts that might confuse ATS systems.\n"
    feedback += "- Tailor your resume for each job application, ensuring you address the specific requirements in the job description.\n"

    return feedback

if __name__ == "__main__":
    # Sample resume and job description for testing
    resume_text = """
    Experienced data scientist skilled in Python, machine learning, and statistical analysis. 
    Proficient with tools like TensorFlow, Scikit-learn, and SQL. Passionate about solving complex business problems.
    """
    job_description = """
    Looking for a data scientist with experience in Python, machine learning, SQL, and data visualization tools like Tableau.
    Must have expertise in Scikit-learn and TensorFlow.
    """
    
    # Calculate resume score
    score = calculate_resume_score(resume_text, job_description)
    print(f"Resume Match Score: {score}%")

    # Generate feedback
    feedback = generate_feedback(resume_text, job_description)
    print("\n" + feedback)
