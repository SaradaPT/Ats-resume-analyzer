# ATS Resume Checker

**ATS Resume Checker** is an AI-powered web application designed to evaluate the match between a resume and a job description. The app provides a **match score** and **personalized feedback** based on the user's uploaded resume and the job description entered.

## Features
- **Resume Upload**: Upload resumes in PDF format.
- **Job Description Matching**: Enter a job description to compare against your resume.
- **Match Score**: Get a percentage score indicating how well your resume matches the job description.
- **Personalized Feedback**: Receive detailed feedback with suggestions to improve your resume.
- **Email Verification**: Users need to register and verify their email before accessing the app.
  
## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run the ATS Resume Checker locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/ATS-Resume-Checker.git
    cd ATS-Resume-Checker
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    - Make sure to set up the required environment variables, such as for email configuration (e.g., SMTP details for sending emails).

5. **Run the application:**
    ```bash
    python app.py
    ```
    The application should now be accessible at `http://127.0.0.1:5000/` on your browser.

---

## Usage

Once the app is running:

1. Go to the homepage of the app.
2. **Register** by providing your email and password.
3. **Verify your email** using the code sent to your email inbox.
4. After successful verification, you can upload your **resume** in PDF format and input the **job description**.
5. The app will generate a **match score** and **feedback** based on the job description.
6. You can then view and improve your resume based on the feedback.

---

## How It Works

The ATS Resume Checker works by:

1. **Resume Parsing**: The app uses **PDFMiner** to extract text from resumes in PDF format.
2. **Text Matching**: It compares the extracted resume text with the job description.
3. **Score Calculation**: A match score is calculated based on the similarity of keywords, skills, and experience in the resume and the job description.
4. **Personalized Feedback**: The app generates feedback on areas for improvement based on the content of the resume.

---

## Technologies Used

This project uses the following technologies:

- **Flask** - Web framework for building the application.
- **Flask-Mail** - For sending verification emails.
- **Flask-Login** - To manage user login and session.
- **Flask-WTF** - For form handling and validation.
- **Python Libraries**:
  - **PDFMiner** - For extracting text from PDF resumes.
  - **Natural Language Processing (NLP)** for text matching (e.g., using libraries like **spaCy** or **NLTK**).
  - **HTML/CSS** - For frontend development.

---

## Contributing

We welcome contributions to improve the ATS Resume Checker! To contribute, follow these steps:

1. Fork the
