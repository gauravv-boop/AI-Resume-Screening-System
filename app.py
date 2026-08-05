from flask import Flask, render_template, request
import os

from utils.parser import extract_text_from_pdf
from utils.matcher import calculate_match_score
from utils.skills import extract_skills
from utils.suggestions import generate_suggestions
from utils.ats import calculate_ats_score
from utils.strength import resume_strength

app = Flask(__name__)

UPLOAD_FOLDER = "resumes"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    # Check Resume
    if "resume" not in request.files:
        return "No Resume Uploaded!"

    file = request.files["resume"]

    if file.filename == "":
        return "No File Selected!"

    # Job Description
    job_description = request.form["job_description"]

    # Save Resume
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Extract Resume Text
    resume_text = extract_text_from_pdf(filepath)

    # Extract Skills
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    # Matched & Missing Skills
    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))

    # Suggestions
    suggestions = generate_suggestions(missing)

    # AI Match Score
    score = calculate_match_score(resume_text, job_description)

    # ATS Score
    ats_score = calculate_ats_score(matched, missing)

    # Resume Strength
    strength = resume_strength(score)

    # Resume Match Score Color
    if score >= 70:
        score_color = "#28a745"      # Green
    elif score >= 40:
        score_color = "#ffc107"      # Yellow
    else:
        score_color = "#dc3545"      # Red

    # ATS Score Color
    if ats_score >= 70:
        ats_color = "#28a745"
    elif ats_score >= 40:
        ats_color = "#ffc107"
    else:
        ats_color = "#dc3545"

    return render_template(
        "result.html",
        score=score,
        ats_score=ats_score,
        strength=strength,
        score_color=score_color,
        ats_color=ats_color,
        job_description=job_description,
        resume_text=resume_text,
        matched=matched,
        missing=missing,
        suggestions=suggestions
    )


if __name__ == "__main__":
    app.run(debug=True)