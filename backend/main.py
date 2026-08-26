from fastapi import FastAPI, UploadFile, File, Form
import fitz

from resume_parser import detect_sections
from skills import extract_skills
from scoring import calculate_score
from job_matcher import match_resume_with_job
from feedback import generate_feedback


app = FastAPI()


# -----------------------------------
# Home
# -----------------------------------

@app.get("/")
def home():
    return {
        "message": "Resume Analyzer API is running!"
    }


# -----------------------------------
# Upload Resume
# -----------------------------------

@app.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...)
):

    contents = await file.read()

    pdf = fitz.open(
        stream=contents,
        filetype="pdf"
    )

    text = ""

    for page in pdf:
        text += page.get_text()

    sections = detect_sections(text)

    skills = extract_skills(text)

    score = calculate_score(
        text,
        sections,
        skills
    )

    feedback = generate_feedback(
        text,
        sections,
        skills
    )

    return {
        "filename": file.filename,
        "score": score,
        "sections": sections,
        "skills": skills,
        "feedback": feedback
    }


# -----------------------------------
# Analyze Resume With Job Description
# -----------------------------------

@app.post("/analyze-job")
async def analyze_job(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    contents = await file.read()

    pdf = fitz.open(
        stream=contents,
        filetype="pdf"
    )

    text = ""

    for page in pdf:
        text += page.get_text()

    sections = detect_sections(text)

    skills = extract_skills(text)

    score = calculate_score(
        text,
        sections,
        skills
    )

    feedback = generate_feedback(
        text,
        sections,
        skills
    )

    job_result = match_resume_with_job(
        skills,
        job_description
    )

    return {
        "filename": file.filename,
        "resume_score": score,
        "resume_skills": skills,
        "feedback": feedback,
        "job_match": job_result
    }