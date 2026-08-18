
from fastapi import FastAPI, UploadFile, File
import fitz

from resume_parser import detect_sections
from skills import extract_skills
from scoring import calculate_score
app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Resume Analyzer API is running!"
    }


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    contents = await file.read()

    pdf = fitz.open(stream=contents, filetype="pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    sections = detect_sections(text)

    skills = extract_skills(text)

    score = calculate_score(sections, skills)

    return {
        "filename": file.filename,
        "score": score,
        "sections": sections,
        "skills": skills
    }