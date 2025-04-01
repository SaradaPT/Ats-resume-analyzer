import os
from flask import Flask, request, render_template, jsonify
from resume_parser import extract_text_from_pdf
from resume_matcher import calculate_resume_score, generate_feedback

app = Flask(__name__)

# Home route to upload resume
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the resume upload and processing
@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['resume']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded file to disk
    resume_path = os.path.join('uploads', file.filename)
    os.makedirs('uploads', exist_ok=True)
    file.save(resume_path)

    # Extract text from resume
    resume_text = extract_text_from_pdf(resume_path)

    if "Error extracting text" in resume_text:
        os.remove(resume_path)
        return jsonify({"error": "Error extracting text from the resume. Please ensure it's a valid PDF file."}), 500

    # Get job description from form (or use a default)
    job_description = request.form.get('job_description', 
                                      "Looking for a Data Scientist with Python, NLP, and SQL experience.")

    # Calculate resume score
    score = calculate_resume_score(resume_text, job_description)
    feedback = generate_feedback(resume_text, job_description)

    # Cleanup: Delete uploaded file after processing
    os.remove(resume_path)

    return jsonify({
        "score": score,
        "feedback": feedback
    })

if __name__ == '__main__':
    app.run(debug=True)
