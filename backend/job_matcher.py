import re

from skills import SKILLS


def extract_job_skills(job_description):
    text = job_description.lower()

    found_skills = []

    for skill in SKILLS:
        # Escape special characters such as C++, C#, etc.
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills


def match_resume_with_job(resume_skills, job_description):
    job_skills = extract_job_skills(job_description)

    resume_skills = [skill.lower() for skill in resume_skills]

    matched_skills = []
    missing_skills = []

    for skill in job_skills:
        if skill in resume_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if len(job_skills) > 0:
        match_percentage = round(
            (len(matched_skills) / len(job_skills)) * 100
        )
    else:
        match_percentage = 0

    return {
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": match_percentage
    }